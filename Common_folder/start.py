import sys
import importlib
import re
from datetime import datetime
import os
import json
import pathlib
import M_04_functions as imported_file
import xml.etree.ElementTree as ET
import argparse

# import all modules from previous tasks
sys.path.append(r'M_04_functions.py')
#string_function = importlib.import_module("Functions")
sys.path.append(r'M_05_Classes.py')
#newsfeed = importlib.import_module("newsfeed")
sys.path.append(r'M_06_Files.py')
#text_parser = importlib.import_module("text_parser")
sys.path.append(r'M_07_csv.py')
#csv.parsing = importlib.import_module("csv.parsing")
sys.path.append(r'M_08_JSON.py')
#json_parser = importlib.import_module("json_parser")
sys.path.append(r'M_09_XML.py')
#xml_parser = importlib.import_module("xml_parser")
sys.path.append(r'M_10_db.py')
#db_work = importlib.import_module("dbconnect")
