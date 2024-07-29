 

<!DOCTYPE html>
<html>
 
<body>
    <h1>so many 64s---ctflearn </h1>

    <h2>Challenge Description</h2>
    <p> Help! My friend stole my flashdrive that had the flag on it. When he gave it back the flag was changed! Can you help me decrypt it? https://mega.nz/#!OHhUyIqA!H9WxSdG1O7eVcCm0dffggNB0-dBemSpBAXiZ0OXJnLk
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>we open file and see a lot base64 like text one of them is flag? so search 
on them repeatedly for find text of flag and find flag with this code

<pre>
from io import open
import sys
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
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">ABCTF{pr3tty_b4s1c_r1ght?}

</p>

    <h2>Conclusion</h2>
    <p>this is a problem for find base64 that decoded text have some search in all base64s in file</p>

</body>
</html>
