 

<!DOCTYPE html>
<html>
 
<body>
    <h1>htbctf--sanitycheck Writeup </h1>

    <h2>Challenge Description</h2>
    <p> 94.237.49.212:52765 
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>copy and past flag from   url above in browser .get url after
run duck .every time url address is different.this is a challenge for start htbctf challenges in crypto
in this link in myblog
<a href="https://github.com/cybersecctf/blog/tree/main/2024/htbctf">all challenges</a>
i will add info about team in htb challenges here
<pre>
import blog

import os,subprocess
def solve(url, search=""):

  blog.solveup("inspect",url,search) 

if __name__ == "__main__" :
  print(solve("https://94.237.49.212:52765/"))
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">HTB{onboard1ng_fl4g}.
</p>

    <h2>Conclusion</h2>
    <p>this is a sanity check  chanllenge for check if i start this ctf;)</p>

</body>
</html>
