import psycopg2 as pg
from psycopg2 import extras
from dotenv import dotenv_values
import os

class DataBase:
    _instance = None
    _env = dotenv_values('.env')
    _config = {
        'host': _env['DB_HOST'],
        'user': _env['DB_USER'],
        'password': _env['DB_PASSWORD'],
        'dbname': _env['DB_NAME']
    }
    
    def __new__(cls):
        if DataBase._instance is None: 
            DataBase._instance = object.__new__(cls)
        return DataBase._instance
    
    @classmethod
    def _query(self, query):
        try:
            with pg.connect(**self._config) as connection:
                cursor = connection.cursor(cursor_factory = pg.extras.RealDictCursor) 
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except pg.OperationalError:
            return 'Hay algo malo en la configuración'