<title>Image Editing--ctflearn  Writeup </title>
 

<!DOCTYPE html>
<html>
 
<body>
    <h1>Image Editing--ctflearn  Writeup </h1>

    <h2>Challenge Description</h2>
    <p> I sent a couple of images to my friend,
 Leslie S. Brown, to edit.
 The only problem is that she only sent back 1 image! Can you help me figure out what happened to the other image? Also,
 for whatever reason, the image has a red tinge to it. Image: https://mega.nz/#!nGg2DIxA!zL1BLCoPpRB6KPTBrDqHWXyphBn-SRl1qs_kpcyIS4k
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>
we extract and exiftool and strings file nothing working but use stegsolve and after options is work
this images show steps in stegsolve and inviroment of software
<img src=" https://cybersecctf.github.io/blog/2024/practice/ctflearn/imageediting/stegsolve.png" alt="stegsolve" width="500" height="600" class="inline"/>
<img src=" https://cybersecctf.github.io/blog/2024/practice/ctflearn/imageediting/stegsolve-options.png" alt="stegsolve good options" width="500" height="600" class="inline"/>
and after zsteg run see text like this 1_kn3W_tH3_r3D_w4s_0ff that is our flag
<pre>
import blog

import os,subprocess
def solve(file, search=""):
    try:
        # Run stegsolve command
        if search=="stegsolve" or search=="":
         blog.solveup("garden","java -jar stegsolve.jar","")#analysis  data extract  options in pic
         if search=="":
           return
        result=blog.solveup("garden",f"zsteg {file}","")#analysis  data extract  options in pic
        print(result)
        
    except Exception as e:
        print(f"Error running zsteg: {e}")
   

if __name__ == "__main__" :
 file="writeup1.png" 
 solve(file,"stegsolve")

 solve(file,"zsteg")
 #extract_binwalk(file)
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlearn{1_kn3W_tH3_r3D_w4s_0ff}
</p>

    <h2>Conclusion</h2>
    <p>this is a hard challeng for work on stegsolve and zsteg</p>

</body>
</html>
