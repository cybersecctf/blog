
<!DOCTYPE html>
<html>

<body>
    <h1>PDF by fdpumyp- ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> Hi, just as we talked during a break, you have this file here and check if something is wrong with it. That's the only thing we found strange with this suspect, I hope there will be a password for his external drive
Bye
 <a href="https://ctflearn.com/challenge/download/957">dontopen.pdf</a>
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
after open file and see nothing
     we string it
<pre>
$strings $1
</pre>
and see two base64 below "== SECRET DATA DONT LOOK AT THIS ==
one of them  is flag in base64 after <a href="https://cybersecctf.github.io/blog/2024/practice/ctflearn/charcterencoding/writeup1.md
">decode base64</a> will get our flag

    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag"> CTFlearn{)_1l0w3y0Um00my123}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for string and decode base and crypto/p>
</body>
</html>



