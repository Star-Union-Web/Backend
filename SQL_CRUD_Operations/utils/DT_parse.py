from enum import Enum

class G_type(Enum):
    INT = "INTEGER"
    FLOAT = "FLOAT"
    TEXT = "TEXT"
    DATE = "DATE"
    RELATION = "INTEGER"

class T(Enum):
    INTEGER = int
    FLOAT = float
    TEXT = str
    DATE = str

if __name__ == "__main__":
    print(G_type.INT.value)
