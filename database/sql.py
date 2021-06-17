from .db import DataBase
from psycopg2 import errors 

def select( table, columns=[], where=None):
    """Whitout param @columns get all columns"""
    name_columns = ''
    if len(columns) == 0:
        name_columns = '*'
    else:
        for col in columns:
            name_columns += col + ', '    
    try:
        result = DataBase._query(f"SELECT {name_columns} FROM {table} {f'WHERE {where}' if where != None else ''}")
        return Exception('No hay datos') if len(result) == 0 else result
    except errors.UndefinedTable:
        return 'La tabla no existe'
