from managers.DBManager import DBManager
from utils.DT_parse import G_type, T
from utils.Attribute import Attribute
from utils.Model import Model

class DBManagerUI:

    def __init__(self):
        self.db_manager = DBManager()

    def menu(self):

        while True:

            print("1. Create a new model")
            print("2. View models")
            print("3. Create a new record")
            print("4. Delete a record")
            print("5. Update a record")
            print("6. Query a record")
            print("7. Create Table")
            print("8. Exit")

            choice = input("Please choose an option: ")

            if choice == "1":
                self.add_model()
            elif choice == "2":
                self.print_models()
            elif choice == "3":
                self.create_record_ui()
            elif choice == "4":
                self.delete_record_ui()
            elif choice == "5":
                self.update_record_ui()
            elif choice == "6":
                self.read_record_ui()
            elif choice == "7":
                self.create_table_ui()
            elif choice == "8":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

    def attribute_input(self):

        attribute_name = input("Enter attribute name: ")

        print("The available types: ")
        print("1) INT")
        print("2) FLOAT")
        print("3) TEXT")
        print("4) DATE")
        print("5) RELATION")

        attribute_data_type = ""
        while True:
            attribute_data_type = input("Enter attribute type by name (ex. int): ")
            attribute_data_type = G_type[attribute_data_type.upper()]
            break

        attribute_default_value = None
        while True:
            attribute_default_value = input("Enter attribute default value (leave blank for None): ")
            if attribute_default_value == "":
                attribute_default_value = None
            else:
                try:
                    attribute_default_value = float(attribute_default_value)
                except ValueError:
                    attribute_default_value = attribute_default_value
            break

        attribute_required = False
        while True:
            action = input("Is attribute null? (yes/no): ")
            if action.lower() == "no":
                attribute_required = True
            break

        return [attribute_name, Attribute(attribute_data_type, attribute_default_value, attribute_required)]

    def add_model(self):

        model_name = input("Enter model name: ")
        attribute_count = int(input("How many attributes you want the model to have?"))
        attributes = {}

        for i in range(attribute_count):
            att = self.attribute_input()
            attributes[att[0]] = att[1]
        
        self.db_manager.add_model(model_name, attributes)

    def print_models(self):
        models = self.db_manager.entities

        for m in models.keys():
            print('-'*20)
            print(f"Model: {m}")
            for a in models[m].attributes.keys():
                att = models[m].attributes[a]
                print(f"  Attribute: {a} | {att.data_type} | {att.default_value} | {att.required}")

            print('-'*20)

    def create_table_ui(self):
        model = input("Enter model name: ")
        self.db_manager.create_table(model)

    def create_record_ui(self):
        
        model_name = input("Enter model name: ")

        if model_name not in self.db_manager.entities:
            print("Model not found")
            return

        record = {}
        
        attributes = self.db_manager.entities[model_name].attributes

        for a in attributes.keys():
            it = 1

            inp = ""
            while (attributes[a].required and inp == "") or it > 0:

                if attributes[a].required is False:
                    print("(you can leave it blank)")
                inp = input(f"Enter {a}: ")


                if inp == "":
                    record[a] = None

                elif attributes[a].data_type in [G_type.INT.value, G_type.RELATION.value]:
                    record[a] = int(inp)
                elif attributes[a].data_type == G_type.FLOAT.value:
                    record[a] = float(inp)
                elif attributes[a].data_type == G_type.TEXT.value:
                    record[a] = inp

                
                it -= 1

        self.db_manager.create_record(model_name, record)

    def read_record_ui(self):
        model = input("Enter model name: ")
        if model is not None:
            print(self.db_manager.read_record(model))

    def update_record_ui(self):
        model = input("Enter model name: ")

        if model not in self.db_manager.entities:
            print("Model not found")
            return

        id = int(input("Enter id: "))

        attributes = self.db_manager.entities[model].attributes
        new_values = {}
        for attribute in attributes:

            inp = input(f"Enter {attribute} (Enter to skip): ")

            if inp == "":
                continue

            if attributes[attribute].data_type == G_type.INT.value:
                new_values[attribute] = int(inp)
            elif attributes[attribute].data_type == G_type.FLOAT.value:
                new_values[attribute] = float(inp)
            elif attributes[attribute].data_type == G_type.TEXT.value:
                new_values[attribute] = inp
            elif attributes[attribute].data_type == G_type.RELATION.value:
                new_values[attribute] = int(inp)
                

        self.db_manager.update_record(model, new_values, {"id": id})

    def delete_record_ui(self):
        pass
