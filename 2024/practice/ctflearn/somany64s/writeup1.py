
from io import open
import sys
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
import base64
import os,subprocess
import base64

def solve(file, search="", max_attempts=100):
    base64s = "" 
    with open(file, encoding='utf-8') as f:
        base64s = f.read()

    attempts = 0
    while attempts < max_attempts:
        base64s = base64.b64decode(base64s)
        if search in str(base64s):
            print(base64s.decode("utf-8"))
            break
        attempts += 1
    else:
        print(f"Search string not found after maximum {max_attempts} attempts.")

if __name__ == "__main__":
    solve("flag.txt", "CTF{")
