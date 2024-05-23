import ast,sys
from decimal import Decimal, InvalidOperation
import importlib.util
import os
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
        print(f"The module does not have a '{func_name}' function.")
        return None

def run(term, *args):
    search_term = term
    file_path = "/home/mrrobot/Desktop/blog/Ai"
    
    # Step 1: Search for the term in the file
    line = find_term_in_file(file_path, search_term)
    if not line:
        print(f"Search term '{search_term}' not found in the file.")
        return
    
    # Step 2: Extract URLs from the line
    md_url, py_url = extract_urls_from_line(line)
  
    
    # Step 3: Import the Python file dynamically
    module_name = os.path.basename(py_url).replace('.py', '')
    py_file_path = py_url.replace('https://cybersecctf.github.io/blog/', '/home/mrrobot/Desktop/blog/')  # Adjust this as needed
    
    module = import_function_from_file(module_name, py_file_path)
    
    # Step 4: Run the function from the imported module
    result = run_function_from_module(module, 'run', *args)
    if result is not None:
        return result
 
 
def detect_value_type(value):
    # Check for integer
    try:
        int_value = int(value)
        if '.' not in value and 'e' not in value.lower():
            return 'int'
    except ValueError as e:
        print(f"error in {value}:{str(e)}")

    # Check for Decimal
    try:
        decimal_value = Decimal(value)
        if decimal_value == float(decimal_value):  # Check if decimal and float are equivalent
            return 'float'
        else:
            return 'decimal'
    except InvalidOperation:
        pass

    # Check for float
    try:
        float_value = float(value)
        return 'float'
    except ValueError:
        pass

    # If all conversions fail, it's a string
    return 'string'

def set(val, i=1,type="auto",alert="usage argument -v"):
    
    if i<=0:
          print("argument value should be more than 0 not",i)
          return     
    if len(sys.argv) > i:
       val = sys.argv[i] 
    try:
          if not isinstance(val,str):
              return  val
          if type=="auto" :
              type=detect_value_type(val)
          if type=="float":
             val=float(val)
          elif type=="int":
            val = int(val)
          elif type=="decimal":
             val = Decimal(val)
          elif val.startswith("[") and val.endswith("]") and "," in val:
                         val=ast.literal_eval(val)
          else:
               val=val#do nothing     
    except Exception as e:
                 print(f"exception in val{val}:{str(e)}")
    if len(sys.argv) ==1:
       if alert=="usage argument -v"    :  
        print(alert+" "+str(i)+"th value") 
       else:
          print(alert)
    return val
 