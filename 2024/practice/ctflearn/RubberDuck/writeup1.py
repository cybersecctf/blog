
import subprocess
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
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

     
