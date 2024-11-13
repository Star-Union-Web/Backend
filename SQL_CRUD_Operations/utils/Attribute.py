from utils.DT_parse import *


class Attribute:

    def __init__(self, data_type : G_type, default_value=None, required : bool = False) -> None:
        self.data_type = data_type.value
        
        self.default_value = default_value
            
        self.required = required