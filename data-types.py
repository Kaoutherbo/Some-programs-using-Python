# sys is a part of the Python standard library
import sys

# Data types and their sizes in bytes
data_types = {
    "int": sys.getsizeof(0),
    "float": sys.getsizeof(0.0),
    "complex": sys.getsizeof(0j),
    "bool": sys.getsizeof(True),
    "str": sys.getsizeof(""),
    "list": sys.getsizeof([]),
    "tuple": sys.getsizeof(()),
    "dict": sys.getsizeof({}),
    "set": sys.getsizeof(set()),
}

# Print the data types and their sizes
for data_type, size in data_types.items():
    print(f"Size of {data_type}: {size} bytes")
