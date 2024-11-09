import sqlite3
import json

class ORM:
    CONNECTION : sqlite3.Connection
    CURSOR : sqlite3.Cursor
    CONFIG : dict[str: dict]
    
    @staticmethod
    def _load_config(file_path):
        with open(file_path, 'r') as file:
            ORM.CONFIG = json.load(file)

    @staticmethod
    def __init__():
        ORM._load_config('config.json')
        ORM.CONNECTION = sqlite3.connect(ORM.CONFIG['database']['name'])
        ORM.CURSOR = ORM.CONNECTION.cursor()

    @staticmethod
    def _get_sql_type(python_type: type) -> str:
        """Convert Python types to SQLite types"""
        type_mapping = {
            str: 'TEXT',
            int: 'INTEGER',
            float: 'REAL',
            bool: 'INTEGER',
        }
        return type_mapping.get(python_type, 'TEXT')  # Default to TEXT if type is unknown

    @staticmethod
    def _get_fields_query(class_attributes: dict) -> str:
        list_fields = []
        for field_name, field_type in class_attributes.items():
            sql_type = ORM._get_sql_type(field_type)
            list_fields.append(f"{field_name} {sql_type}")

        return ", ".join(list_fields)

    @classmethod
    def _create_table(cls: type):
        class_name = cls.__name__
        class_attributes = cls.__annotations__

        query_fields = cls._get_fields_query(class_attributes)
        ORM.CURSOR.execute(f"""CREATE TABLE IF NOT EXISTS {class_name} (
                                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                                {query_fields}
                               )""")
        ORM.CONNECTION.commit()

    @staticmethod
    def _migrate():
        for child in ORM.__subclasses__():
            child._create_table()

    @classmethod
    def fetch_object(cls: type, id: int) -> object:
        ORM.CURSOR.execute(f"SELECT * FROM {cls.__name__} WHERE id = ?", (id,))
        record = ORM.CURSOR.fetchone()

        if record is None:
            return None

        id, *record = record
        obj = cls(*record)
        obj._id = id

        return obj
    
    @classmethod
    def get_objects(cls: type) -> list:

        ORM.CURSOR.execute(f"SELECT * FROM {cls.__name__}")
        rows = ORM.CURSOR.fetchall()

        objects = []
        for record in rows:
            id, *record = record
            obj = cls(*record)
            obj._id = id
            objects.append(obj)

        return objects
    
    @staticmethod
    def migrate():
        ORM.__init__()
        ORM._migrate()

    def update(obj: object, field: str, value):
        obj.CURSOR.execute(f"UPDATE {obj.__class__.__name__} SET {field} = ? WHERE id = ?", (value, obj._id))
        obj.CONNECTION.commit()


    def save(self: object) -> int:
        """
        Takes an object and inserts it into the table of the object's class
        """
        object_dict = self.__dict__
        string_fields = ", ".join(object_dict.keys())
        number_fields = ", ".join("?" * len(object_dict.keys()))
        tuple_values = tuple(object_dict.values())

        try:
            ORM.CURSOR.execute(f"INSERT INTO {self.__class__.__name__} ({string_fields}) VALUES ({number_fields})", tuple_values)
            self._id = ORM.CURSOR.lastrowid
            ORM.CONNECTION.commit()

        except sqlite3.OperationalError as e:
            print(e)
            print(f"Error: table {self.__class__.__name__} does not exist")
            print("Please make sure to run latest migration")


