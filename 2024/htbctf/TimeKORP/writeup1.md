 

<!DOCTYPE html>
<html>
 
<body>
    <h1>HTBCTF2024---TimeKORP  Writeup </h1>

    <h2>Challenge Description</h2>
    <p> Are you ready to unravel the mysteries and expose the truth hidden within 
KROP's digital domain? Join the challenge and prove your prowess in the world of cybersecurity.
 Remember, time is money, but in this case, the rewards may be far greater than you imagine.
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>after using binawalk and exiftool not working using 

<pre>
import blog

import os,subprocess
def solve(file, search=""):
   blog.islog=True
   return blog.solveup("find zip password",file)  
if __name__ == "__main__" :
  print(solve("web_timecorp.zip"))
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{more_than_m33ts_the_3y3657BaB2C}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on develper tools in in chrome and web exploitations</p>

</body>
</html>
