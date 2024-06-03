import importlib.util
import os
import sys
import ast
from decimal import Decimal, InvalidOperation

isprinted = False
islog = False
results = []

class Result:
    def __init__(self, md_url, py_url, score=0):
        self.md_url = md_url
        self.py_url = py_url
        self.score = score
        self.code = None

    def add_score(self, points):
        self.score += points

    def set_code(self, code):
        self.code = code

    def __str__(self):
        return f"URL: {self.md_url}, Score: {self.score}, Code: {self.code}"

def log(message):
    if islog:
        print(message)

def find_terms_in_file(file_path, search_terms):
    global results
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        for term in search_terms:
            if term in line:
                results.append(line.strip())
                break
    return results

def extract_urls_from_line(line):
    parts = line.split(',')
    md_url = parts[-1]
    py_url = md_url.replace('.md', '.py')
    return md_url, py_url

def import_function_from_file(module_name, file_path):
    if " " in file_path:
        file_path = file_path.split(" ")[1].strip()
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

class Blog:
    def __init__(self, file_path="/home/mrrobot/Desktop/blog/Ai"):
        self.file_path = file_path

    def search_and_process(self, terms):
        results = []
        lines = find_terms_in_file(self.file_path, terms)
        for line in lines:
            md_url, py_url = extract_urls_from_line(line)
            result = Result(md_url, py_url)
            results.append(result)
        return results

    def evaluate_results(self, results, words):
        for result in results:
            line_part_before_comma = result.md_url.split(',')[0]
            line_whole = result.md_url

            # Score +100 for each term found before the comma
            for word in words:
                if word in line_part_before_comma:
                    result.add_score(100)

            # Score +1 for each term found in the whole line
            for word in words:
                if word in line_whole:
                    result.add_score(1)

        # Sort the results by score in descending order
        results.sort(key=lambda x: x.score, reverse=True)
        return results

    def solveup(self, term, *args):
        global isprinted, islog

        if term.endswith("-log"):
            term = term[:-4]
            islog = True

        search_terms = term.split(" ")
        results = self.search_and_process(search_terms)

        if not results:
            log(f"Search term '{term}' not found in the file.")
            return

        evaluated_results = self.evaluate_results(results, search_terms)
        if evaluated_results:
            best_result = evaluated_results[0]
            print(f"Best Result: {best_result}")

            # Import and run the solve function for the best result
            module_name = os.path.basename(best_result.py_url).replace('.py', '')
            py_file_path = best_result.py_url.replace('https://cybersecctf.github.io/blog/', '/home/mrrobot/Desktop/blog/')  # Adjust this as needed
               
            try:
                module = import_function_from_file(module_name, py_file_path)
                code_result = run_function_from_module(module, 'solve', *args)
                print("r",code_result)
                best_result.set_code(code_result)
                print(code_result)
                # If the code_result includes a call to solveup, handle it
                if isinstance(code_result, str) and 'solveup' in code_result:
                    # Extract the term from the solveup call
                    new_term = code_result.split('solveup("')[1].split('"')[0]
                    log(f"Calling solveup recursively with term: {new_term}")
                    return self.solveup(new_term, *args)

            except FileNotFoundError as e:
                log(f"File not found: {e}")
            except Exception as e:
                log(f"Error running solve function: {e}")

            return best_result
        else:
            return None

    def detect_value_type(self, value):
        log(f"Detecting value type for: {value}")
        try:
            int_value = int(value)
            if '.' not in value and 'e' not in value.lower():
                return 'int'
        except ValueError as e:
            return str(e)

        try:
            decimal_value = Decimal(value)
            if decimal_value == float(decimal_value):
                return 'float'
            else:
                return 'decimal'
        except InvalidOperation as e:
            log(f"Error detecting decimal for {value}: {str(e)}")

        try:
            float_value = float(value)
            return 'float'
        except ValueError as e:
            log(f"Error detecting float for {value}: {str(e)}")

        return 'string'

    def set(self, val, i=1, type="auto", alert="usage argument -v"):
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
                type = self.detect_value_type(val)
            if type == "float":
                val = float(val)
            elif type == "int":
                val = int(val)
            elif type == "decimal":
                val = Decimal(val)
            elif val.startswith("[") and val.endswith("]") and "," in val:
                val = ast.literal_eval(val)
            else:
                val = val
        except Exception as e:
            log(f"Exception in val {val}: {str(e)}")
        if len(sys.argv) == 1:
            if alert == "usage argument -v":
                log(alert + " " + str(i) + "th value")
            else:
                print(alert) 
        return val
blog=Blog()
print(blog.solveup("string reverse","hi")) 