from .db import DataBase
from psycopg2 import errors 

def _excecute_query(query):
    try:
        result = DataBase._query(query)
        return Exception('No hay datos') if len(result) == 0 else result
    except errors.UndefinedTable as error:
        return Exception(f'La tabla no existe {error}')
    except errors.UndefinedColumn as error:
        return Exception(f'Una columna no existe {error}')
    except errors.InvalidTextRepresentation as error:
        return Exception('Error en un tipo de dato')
    except errors.UniqueViolation as error:
        return Exception('Este elemento ya existe')
    except Exception as error:
        print(type(error))

def select(table, columns=[], where=None, join={'empty': ['','']}, group_by=None):
    """
    Whitout param @columns get all columns or [column_1, column_2, column_3 ... column_n]
    param @where is the condition
    param @join is a dic where key is the name of table to join, values is array with two primary keys
    param @group_by is the colum to group
    """
    name_columns = ',' # column_1, column_2, column_3 ... column_n
    name_join = ''     # INNER JOIN {...}, INNER JOIN {...} ...
    if len(columns) == 0:
        name_columns = '*'
    else:
        name_columns = name_columns.join(columns) 

    if 'empty' not in join:
        for tabla_join in join.keys():
            name_join += f'INNER JOIN {tabla_join} ON {join[tabla_join][0]} = {join[tabla_join][1]}'
    
    query = f"""
    SELECT {name_columns} FROM {table} 
    {name_join} 
    {f'WHERE {where}' if where != None else ''}
    {f'GROUP BY {group_by}' if group_by != None else ''}
    """
    return _excecute_query(query)

def insert(table, data):
    name_columns = ','.join(data.keys())
    name_values = ''
    for col in data.values():
        if (type(col) != str):
            name_values += f"{str(col)},"
        else:
            name_values += f"'{col}',"
    query = f"""
    INSERT INTO {table} ({name_columns}) VALUES ({name_values[:-1]})
    """
    return _excecute_query(query)