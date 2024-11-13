import sqlite3 as sql
from pathlib import Path

__dir__ = Path(__file__).parent.parent.resolve()

class Connection:
    
    __connection = sql.connect("./db/memory.db")
    __cursor = __connection.cursor()
        
    @staticmethod
    def get_connection():
        return Connection.__connection
        
    @staticmethod
    def get_cursor():
        return Connection.__cursor
        
    @staticmethod
    def execute(*args):
        return Connection.__cursor.execute(*args)

    @staticmethod
    def connect(db_path):
        __connection = sql.connect(db_path)
        __cursor = __connection.cursor()

    @staticmethod
    def commit():
        Connection.__connection.commit()

    @staticmethod
    def close():
        Connection.__connection.close()