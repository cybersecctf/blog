
import re

def find_format_string_vulnerabilities(c_code):
    vulnerabilities = []
    # Regular expression pattern to match printf-like functions
    pattern = r'printf\s*\([^")]*"[^"]*%[^\n]*\)'
    matches = re.finditer(pattern, c_code)
    for match in matches:
        vulnerabilities.append(match.group(0))
    return vulnerabilities

# Read C code from a file
def read_c_code_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Specify the path to the C file
c_file_path = 'format-string-0.c'

# Read the C code from the file
c_code = read_c_code_from_file(c_file_path)

# Search for format string vulnerabilities
vulnerabilities = find_format_string_vulnerabilities(c_code)
if vulnerabilities:
    print("Potential format string vulnerabilities found:")
    for vulnerability in vulnerabilities:
        print(vulnerability)
else:
    print("No potential format string vulnerabilities found.")