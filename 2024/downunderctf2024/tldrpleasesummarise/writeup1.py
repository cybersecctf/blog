
#python
import re
import subprocess
import os
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
def solve(file_path, search="DUCTF"):
  results=[]
  try:
    command=""   
    if not os.path.isfile(file_path):
        command=file_path
    else: 
     # Read the command from the file
     with open(file_path, 'r') as file:
        command = file.read().strip()
 
    # Append commands to save output to temp.sh and run strings on it
    full_command = f"{command} > temp.sh && chmod +x temp.sh && strings temp.sh"
    
    
    
    # Execute the full command and capture the output
    result = subprocess.run(full_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Combine stdout and stderr to cover all output
    combined_output = result.stdout + result.stderr

    
    # Search for the search string in the command output
    for line in     combined_output.splitlines() : 
     if search in line:
        results.append(line)
    if len(results)==0:
        return f"Flag containing '{search}' not found in the command output."
    else:
        for x in  results:
             print(x)
  except Exception as e:
     for line in command.splitlines() : 
      if search in line:
        results.append(line)
     return results 
      

if __name__ == "__main__" :
 # Example usage
 command = blog.set("curl -sL https://pastebin.com/raw/ysYcKmbu | base64 -d",1)
 search = blog.set("DUCTF",2)

 print(solve(command,search))



