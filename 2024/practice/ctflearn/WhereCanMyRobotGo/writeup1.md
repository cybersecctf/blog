 

<!DOCTYPE html>
<html>
 
<body>
    <h1>ctflearn---Where Can My Robot Go? Writeup </h1>

    <h2>Challenge Description</h2>
    <p>  Where Can My Robot Go?

Where do robots find what pages are on a website?

Hint:

What does disallow tell a robot?
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>we use this site for inspect site and find robots.txt and content and open disallowed site and see flag

<pre>
import blog

import os,subprocess
def solve(url, search=""):
     s=blog.solveup("inspect",url+"/robots.txt","/")
     d=s.replace("Disallow: ","")
     d="https://ctflearn.com"+d.strip()
     
     print(d)
     s=blog.solveup("inspect",d,search)
    
     return s

if __name__ == "__main__" :
  s=solve("https://ctflearn.com/","{")
  
  
  print(s)
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlearn{r0b0ts_4r3_th3_futur3}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for find robots and open disallowed urls</p>

</body>
</html>
