<title>Rubber Duck- ctflearn</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Rubber Duck- ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> Find the flag! Simple forensics challenge to get started with.
https://ctflearn.com/challenge/download/933

 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        this time there is no mention to exiftool like <a href="https://cybersecctf.github.io/blog/2024/practice/ctflearn/exif/writeup1.md 
">this</a> but still i try exiftool from it and it work and find in meta
of this image
 <img src=" https://cybersecctf.github.io/blog/2024/practice/ctflearn/RubberDuck/RubberDuck.jpg" alt="RubberDuck" class="inline"/>
or use  this command 
<pre>
import subprocess
import blog
def solve(file, search=""):
    commands = {
        "exiftool": ["exiftool", file],
        "file": ["file", file],
        "strings": ["strings", file]
        
    }
    
    results = {}
    
    for cmd_name, cmd in commands.items():
        try:
            output = subprocess.check_output(cmd, text=True)
            lines = output.splitlines()
            for line in lines:
                if search in line:
                    results[cmd_name] = line
                    return line
        except subprocess.CalledProcessError as e:
            results[cmd_name] = f"Error: {e}"
    
    return results
if __name__ == "__main__" :
 file_path =blog.set("RubberDuck.jpg",1)
 search_term = blog.set("CTF",2)
 print(solve(file_path, search_term))

     
</pre>

       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlearn{ILoveJakarta}.
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on exiftool and forensics</p>
</body>
</html>



