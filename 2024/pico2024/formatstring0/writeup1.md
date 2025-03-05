<title>format string 0-picoctf2024</title>

<!DOCTYPE html>
<html>

<body>
    <h1>format string 0-picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p> Can you use your knowledge of format strings to make the customers happy?
Download the  <a href="https://artifacts.picoctf.net/c_mimas/67/format-string-0">  binary</a>.
Download the <a href="https://artifacts.picoctf.net/c_mimas/67/format-string-0">  source</a> here.
Additional details will be available after launching your challenge instance.
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
      
we use  this code we check c  code have format string volunerbility or no that say this code have in two input
       <pre>
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
if __name__=="__main__":
 file_path=blog.set("./format-string-0.c",1,"str")
 solve(file_path)
</pre>
but only can use three value and not values like %%% .
so see inputs when see input see this two value Gr%114d_Cheese
and Cla%sic_Che%s%steak  have many %so check them and can get flag 
 

    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_74f6c0e7}

</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on format string volunerbility</p>
</body>
</html>


