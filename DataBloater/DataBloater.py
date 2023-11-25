import csv
from DataBloater.CsvReader import CsvReader
from importlib import import_module
from DataBloater.schema import *

class DataBloater:
    def __init__(self, file):
        class_name = file.split(".")[0]
        module = import_module("DataBloater.schema")
        class_schema = getattr(module, class_name)
        class_definition = getattr(class_schema, class_name.capitalize())
        with open(file, 'r', newline=None) as csv_file:
            reader = CsvReader(csv.reader(csv_file, delimiter=','))
            for row in reader:
                row = class_definition(row)
                print(row)
