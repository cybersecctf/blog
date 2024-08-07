
<!DOCTYPE html>
<html>
 
<body>
    <h1>picoctf2019-glory of garden  Writeup </h1>

    <h2>Challenge Description</h2>
    <p> This garden contains more than it seems.
garden:https://jupiter.challenges.picoctf.org/static/43c4743b3946f427e883f6b286f47467/garden.jpg
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>after using binawalk and exiftool not working using 

<pre>
#python
import os
import subprocess
import blog
def solve(file_path, search="{",home_dir=""):
    if not os.path.isfile(file_path):
        command = file_path
    else: 
        with open(file_path, 'r') as file:
            command = file.read().strip()
  
                 
    full_command = f"{command} > temp.sh && chmod +x temp.sh && strings temp.sh"
    if home_dir!="":
      os.chdir(home_dir)
    try:
        result = subprocess.run(full_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=15)
        combined_output = result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        combined_output = "Command timed out after 15 seconds."
    except subprocess.CalledProcessError as e:
        combined_output = e.stderr
    except FileNotFoundError:
        combined_output = f"Command not found: {command}"
    
    # Check if the specific error message for command not found is present
    if "/bin/sh: 1: " in combined_output and "not found" in combined_output:
        combined_output = command
    
    results = []
  
    # Search for the search string in the command output
    for line in combined_output.splitlines():
        if search in line:
            results.append(line)
    
    # If no results found and the file exists, process the file content itself
    file_content=""
    if len(results) == 0 and os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            file_content = file.read()
    for line in file_content.splitlines():
            if search in line:
                results.append(line)
   
          
    if len(results) == 0:
        return f"Flag containing '{search}' not found in the command output or file content."
    else:
        return "\n".join(results)

if __name__ == "__main__": 
  command=blog.set("strings garden.jpg",1)
  search=blog.set("",2)
  print(solve(command,search))



 


 
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{more_than_m33ts_the_3y3657BaB2C}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on develper tools in in chrome and web exploitations</p>
</body>
</html>
