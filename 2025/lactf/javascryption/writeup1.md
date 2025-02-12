<title>lactf2025---rev/javascryptionWriteup </title>
 

<!DOCTYPE html>
<html>
 
<body>
    <h1>ctfzone2024---rev/javascryption Writeup </h1>

    <h2>Challenge Description</h2>
    <p>  
You wake up alone in a dark cabin, held captive by a bushy-haired man demanding you submit a "flag" to leave. Can you escape?

javascryption.chall.lac.tf
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li> 
we open site and see this image   <img src="https://cybersecctf.github.io/blog/2025/lactf/javascryption/Capturecabin.PNG" alt="ctf writeup" width="500" height="600"/> this a textbox that   enter flag it means we can find it on source of site in here js file
and reverse js in here for example btoa(flag) to aotb(flag)... steps are in image below and do in console developer tools    
<img src="https://cybersecctf.github.io/blog/2025/lactf/javascryption/cabin2.PNG" alt="ctf writeup" width="500" height="600"/> 
or use python ccode for  this blog tools and use them later..
<pre>
import base64
import urllib.parse


def solve(encrypted_flag = "JTNEJTNEUWZsSlglNUJPTERfREFUQSU1RG85MWNzeFdZMzlWZXNwbmVwSjMlNUJPTERfREFUQSU1RGY5bWI3JTVCT0xEX0RBVEElNURHZGpGR2I="):
 # Reverse the operations step by step
 # Step 1: Base64 decode
 step1 = base64.b64decode(encrypted_flag).decode('utf-8')
 # Step 2: URL decode
 step2 = urllib.parse.unquote(step1)
 # Step 3: Replace "[OLD_DATA]" with "Z"
 step3 = step2.replace("[OLD_DATA]", "Z")
 # Step 4: Reverse the string
 step4 = step3[::-1]
 # Step 5: Base64 decode again
 original_flag = base64.b64decode(step4).decode('utf-8')
 return original_flag
# Output the flag
if __name__=='__main__':
 print(f"Flag: {solve()}")

</pre>
</li
 
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">lactf{no_grizzly_walls_here}

</p>

    <h2>Conclusion</h2>
    <p>this is a easy chanllenge for easy reverse javascript base64 and url encoding in python and javascrypt</p>
</body>
</html>
