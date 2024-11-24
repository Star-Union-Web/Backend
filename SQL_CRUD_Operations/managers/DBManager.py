from utils.Model import *
from pathlib import Path
import json

__dir__ = Path(__file__).parent.parent.resolve()


class DBManager:

    def __init__(self):
        self.entities : dict[str, Model] = {}
        self.fetch_models()


    def fetch_models(self):
        with open('./db/models.json', 'r') as f:
            entities = json.load(f)
            for entity in entities:
                attributes = {}
                for attribute in entity["attributes"]:
                    attributes[attribute["name"]] = Attribute(
                        attribute["type"], attribute["default"], attribute["required"]
                    )

                self.entities[entity['name']] = Model(entity['name'], attributes)

    def add_model(self, model_name : str, attributes : dict[str, Attribute]):

        self.entities[model_name] = Model(model_name, attributes)

        with open("./db/models.json", 'w') as f:
            json.dump([
                {"name": m, "attributes": 
                    [ {
                        "name": a,
                        "type": self.entities[m].attributes[a].data_type,
                        "default": self.entities[m].attributes[a].default_value,
                        "required": self.entities[m].attributes[a].required
                    } for a in self.entities[m].attributes.keys()
                    ]
                }
                for m in self.entities.keys()
            ], f)

    def create_table(self, model_name: str):
        if model_name not in self.entities:
            print("Model not found")
            return
        
        self.entities[model_name].create_table()

    def create_record(self, model : str, values : dict):
        if model not in self.entities:
            print("Model not found")
            return
        
        self.entities[model].insert(values)

    def read_record(self, model : str, filter : dict = {}):

        if model not in self.entities:
            print("Model not found")
            return

        return self.entities[model].fetch(filter)
    
    def update_record(self, model : str, values : dict, filter : dict = {}):

        if model not in self.entities:
            print("Model not found")
            return

        if "id" in filter:
            self.entities[model].update_by_id(filter["id"], values)
        else:
            self.entities[model].update(filter, values)

    def delete_record(self, model : str, id : int):
        
        if model not in self.entities:
            print("Model not found")
            return
        
        self.entities[model].delete_by_id(id)

