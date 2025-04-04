 
import shlex
import os,subprocess
def solve(file):
 
 
 process = subprocess.run(f"exiftool {file}",
                                    capture_output=True,
                                    text=True,
                                    timeout=10)
 return process.stdout
if __name__ == "__main__" :
 solve("cat.jpg")
