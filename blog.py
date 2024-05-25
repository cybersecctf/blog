import importlib.util
import os
import sys
import ast
from decimal import Decimal, InvalidOperation
isprinted=False
islog=False
def log(str):
  if islog:
   print(str)
def find_term_in_file(file_path, search_term):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        if search_term in line:
            return line.strip()
    return None

def extract_urls_from_line(line):
    parts = line.split(',')
    md_url = parts[-1]
    py_url = md_url.replace('writeup1.md', 'writeup1.py')
    return md_url, py_url

def import_function_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def run_function_from_module(module, func_name, *args):
    if hasattr(module, func_name):
        func = getattr(module, func_name)
        return func(*args)
    else:
        log(f"The module does not have a '{func_name}' function.")
        return None

def solveup(term, *args):
    global isprinted
    if term.endswith("-log"): 
        terms=term[:-4]
        islog=True
    search_term = term
    file_path = "/home/mrrobot/Desktop/blog/Ai"
    
    # Step 1: Search for the term in the file
    line = find_term_in_file(file_path, search_term)
    if not line:
        log(f"Search term '{search_term}' not found in the file.")
        return
    
    # Step 2: Extract URLs from the line
    md_url, py_url = extract_urls_from_line(line)
    #print(f"Markdown URL: {md_url}")
    #print(f"Python URL: {py_url}")
    if not isprinted:
     isprinted=True 
     # Step 3: Import the Python file dynamically
     module_name = os.path.basename(py_url).replace('.py', '')
     py_file_path = py_url.replace('https://cybersecctf.github.io/blog/', '/home/mrrobot/Desktop/blog/')  # Adjust this as needed
     
     module = import_function_from_file(module_name, py_file_path)
    
     # Step 4: Run the function from the imported module
     result = run_function_from_module(module, 'solve', *args)
    if result is not None:
        log(f"Function: solve")
        log(f"Arguments: {args}")
        log(f"Result: {result}")
        return result
    else:
       return None

def detect_value_type(value):
    log(f"Detecting value type for: {value}")
    # Check for integer
    try:
        int_value = int(value)
        if '.' not in value and 'e' not in value.lower():
            return 'int'
    except ValueError as e:
        return  str(e)

    # Check for Decimal
    try:
        decimal_value = Decimal(value)
        if decimal_value == float(decimal_value):  # Check if decimal and float are equivalent
            return 'float'
        else:
            return 'decimal'
    except InvalidOperation as e:
        log(f"Error detecting decimal for {value}: {str(e)}")

    # Check for float
    try:
        float_value = float(value)
        return 'float'
    except ValueError as e:
        log(f"Error detecting float for {value}: {str(e)}")

    # If all conversions fail, it's a string
    return 'string'

def set(val, i=1, type="auto", alert="usage argument -v"):
    log(f"Setting value: val={val}, i={i}, type={type}")
    
    if i <= 0:
        log("Argument value should be more than 0, not", i)
        return     
    if len(sys.argv) > i:
        val = sys.argv[i] 
    try:
        if not isinstance(val, str):
            return val
        if type == "auto":
            type = detect_value_type(val)
        if type == "float":
            val = float(val)
        elif type == "int":
            val = int(val)
        elif type == "decimal":
            val = Decimal(val)
        elif val.startswith("[") and val.endswith("]") and "," in val:
            val = ast.literal_eval(val)
        else:
            val = val  # do nothing     
    except Exception as e:
        log(f"Exception in val {val}: {str(e)}")
    if len(sys.argv) == 1: 
        if alert == "usage argument -v": 
            log(alert + " " + str(i) + "th value") 
        else:
            print(alert)
    return val
