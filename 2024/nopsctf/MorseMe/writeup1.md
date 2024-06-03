
<!DOCTYPE html>
<html>

<body>
    <h1>Morse Me- n0pctf 2024</h1>

    <h2>Challenge Description</h2>
    <p>biiip biiip biiip biiip biiip bip biiip bip bip bip bip bip
<a href="https://cybersecctf.github.io/blog/2024/nopsctf/MorseMe/challenge.txt">challenge.txt</a>
Author: algorab
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
we run this code for convert morse code from challenge to hex and then string
<pre>
import blog
import os
def solve(morse):
 s=morse
 
 if os.path.exists(morse):
    with open(morse, "r+") as f:
       s=f.read()
 s=blog.solveup("morse",s) 
 if " " in s:
  n=2
  hex=" ".join([s[i:i+n] for i in range(0, len(s), n)])
 return blog.solveup("jojo1",s)
if __name__ == "__main__" :
 s=blog.set("challenge.txt",1)
 solve(s)
</pre>  
 
     
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">N0PS{M0rS3_D3c0d3R_Pr0}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for decode morse</p>
</body>
</html>


