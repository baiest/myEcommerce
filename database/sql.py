from .db import DataBase
from psycopg2 import errors 

def select( table, columns=[], where=None, join={'empty': ['','']}, group_by=None):
    """Whitout param @columns get all columns"""
    name_columns = ','
    name_join = ''
    if len(columns) == 0:
        name_columns = '*'
    else:
        name_columns = name_columns.join(columns) 

    if 'empty' not in join:
        for tabla_join in join.keys():
            name_join += f'INNER JOIN {tabla_join} ON {join[tabla_join][0]} = {join[tabla_join][1]}'
    
    try:
        query = f"""
        SELECT {name_columns} FROM {table} 
        {name_join} 
        {f'WHERE {where}' if where != None else ''}
        {f'GROUP BY {group_by}' if group_by != None else ''}
        """
        print(query)
        result = DataBase._query(query)
        return Exception('No hay datos') if len(result) == 0 else result
    except errors.UndefinedTable as error:
        return Exception(f'La tabla no existe {error}')
    except errors.UndefinedColumn as error:
        return Exception(f'Una columna no existe {error}')
    except Exception as error:
        print(error)
