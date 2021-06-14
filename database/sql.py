from .db import DataBase
from psycopg2 import errors 

def select(table, columns=None):
    """Whitout param @columns get all columns"""
    name_columns = ''
    if not columns:
        name_columns = '*'
    else:
        for col in columns:
            name_columns += col + ', '    
    try:
        return DataBase._query(f"SELECT {name_columns} FROM {table}")
    except errors.UndefinedTable:
        return 'La tabla no existe'
