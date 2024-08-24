
<!DOCTYPE html>
<html>
     <title>Vinegar- n00bz CTF 2024 </title>
<body>

    <h1>Vinegar- n00bz CTF 2024  Writeup </h1>

    <h2>Challenge Description</h2>
    <p> Can you decode this message?
<a href="https://cybersecctf.github.io/blog/2024/practice/n00bzctf2024/venegar/enc.txt">enc.txt</a>
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>we open <a href="https://cybersecctf.github.io/blog/2024/practice/n00bzctf2024/venegar/enc.txt">enc.txt</a>
see this message 

<pre>
import blog

import os,subprocess
def solve(text, key):
   return blog.solveup("vigenere cipher",text,key)

if __name__ == "__main__" :
  print(solve("nmivrxbiaatjvvbcjsf","secretkey"))
</pre>
and warap result  that is vigenerecipherisfun in flag like below
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">n00bz{vigenerecipherisfun}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for vigenere cipher </p>

</body>
</html>
