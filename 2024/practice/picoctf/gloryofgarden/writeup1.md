 
<!DOCTYPE html>
<html>
     <title>picoctf2019--glory of garden  Writeup </title>

<body>
    <h1>picoctf2019--glory of garden  Writeup </h1>

    <h2>Challenge Description</h2>
    <p> This garden contains more than it seems.
garden:https://jupiter.challenges.picoctf.org/static/43c4743b3946f427e883f6b286f47467/garden.jpg
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>we use this code for string garden.jpg and get flag and also search on all command

<pre>
#python
import os
import subprocess
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
def solve(file_path, search="{",home_dir=""):
    print("s")
    if ">" in file_path or "<" in file_path or search=="$run":
         d=[]
         result = subprocess.run(file_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=15)
         s=result.stdout.splitlines()
         for x in s:
          if x!="":
            d.append(x)
         return d
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
    
    print(results)

if __name__ == "__main__": 
  command=blog.set("strings garden.jpg",1)
 
  search=blog.set("pico",2)
  print("command",command,search)
  print(solve(command,search))



 


 

</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{more_than_m33ts_the_3y3657BaB2C}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for misc and search on linux command</p>

</body>
</html>
