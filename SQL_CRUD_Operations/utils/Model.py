from utils.DT_parse import *
import sqlite3 as sql
from pathlib import Path
from utils.Connection import Connection
from utils.Attribute import Attribute    

class Model:

    def __init__(self, model_name, attributes : dict[str, Attribute]):
        self.model_name = model_name
        self.attributes = attributes

    def __create_table_q(self):
        columns = ",\n        ".join(
            f"{a} {self.attributes[a].data_type} "
            f"{'NOT NULL' if self.attributes[a].required else ''} "
            f"{f'DEFAULT {self.attributes[a].default_value}' if self.attributes[a].default_value is not None else ''}"
            for a in self.attributes
        )
        
        return f'''CREATE TABLE IF NOT EXISTS {self.model_name} (
            id INTEGER PRIMARY KEY,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            {columns}
        );'''
    
    def __add_attribute_q(self, title:str, attribute : Attribute):
        return f'''ALTER TABLE {self.model_name} ADD COLUMN {title} {attribute.data_type} 
                {'NOT NULL' if attribute.required else ''} {'DEFAULT {attribute.default_value}' if
                attribute.default_value is not None else ''};
                '''

    def __insert_q(self, row : dict):
        columns = ", ".join(row.keys())
        placeholders = ", ".join(["?"] * len(row))
        return f"INSERT INTO {self.model_name} ({columns}) VALUES ({placeholders})"

    def __fetch_q(self, filter : dict):
        columns = ", ".join(self.attributes.keys())
        conditions = " AND ".join(f"{k} = ?" for k in filter.keys())
        return f"SELECT {columns}, created_at, updated_at FROM {self.model_name} {f'WHERE {conditions}' if len(conditions) > 0 else ''}"

    def __update_q(self, filter : dict, values : dict):
        columns = ", ".join(self.attributes.keys())
        conditions = " AND ".join(f"{k} = ?" for k in filter.keys())

        return f"""UPDATE {self.model_name} SET updated_at = CURRENT_TIMESTAMP,
        {', '.join(f'{k} = ?' for k in values.keys())}
        {f'WHERE {conditions}' if len(conditions) > 0 else ''}"""

    def __delete_q(self, filter : dict):
        conditions = " AND ".join(f"{k} = ?" for k in filter.keys())
        return f"DELETE FROM {self.model_name} {f'WHERE {conditions}' if len(conditions) > 0 else ''}"

    def add_attribute(self, title : str, attribute : Attribute):
        self.attributes[title] = attribute
        Connection.execute(self.__add_attribute_q(title, attribute))  

    def create_table(self):
        query = self.__create_table_q()
        Connection.execute(query)
        Connection.commit()

    def insert(self, row : dict): 
        query = self.__insert_q(row)
        Connection.execute(query, tuple(row.values()))
        Connection.commit()

    def fetch(self, filter = {}):
        query = self.__fetch_q(filter)
        Connection.execute(query, tuple(filter.values()))
        return Connection.get_cursor().fetchall()
    
    def update_by_id(self, id, new_values : dict):
        query = self.__update_q({"id": id}, new_values)
        Connection.execute(query, tuple(new_values.values()))
        Connection.commit()

    def update(self, filter : dict, new_values : dict):
        query = self.__update_q(filter, new_values)
        Connection.execute(query, tuple(new_values.values()) + tuple(filter.values()))
        Connection.commit()

    def delete_by_id(self, id):
        query = self.__delete_q({id: id})
        Connection.execute(query, (id))
        Connection.commit()

