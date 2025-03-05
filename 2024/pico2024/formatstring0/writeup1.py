#python
import re
import blog
def find_format_string_vulnerabilities(c_code):
    vulnerabilities = []
    # Regular expression pattern to match printf-like functions
    pattern = r'printf\s*\([^")]*"[^"]*%[^\n]*\)'
    matches = re.finditer(pattern, c_code)
    for match in matches:
        vulnerabilities.append(match.group(0))
    return vulnerabilities


def solve(file_path):
    c_code=""
    with open(file_path, 'r') as file:
        c_code= file.read()
    # Specify the path to the C file
   
    # Search for format string vulnerabilities
    vulnerabilities = find_format_string_vulnerabilities(c_code)
    if vulnerabilities:
     print("Potential format string vulnerabilities found:")
     for vulnerability in vulnerabilities:
        print(vulnerability)
     else:
        print("No potential format string vulnerabilities found.")
if __name__=="__main__":
 file_path="./format-string-0.c"
 solve(file_path)