<title>Time Machine- picoctf2024</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Time Machine- picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p> https://artifacts.picoctf.net/c_titan/66/challenge.zip
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
<pre>
$wget https://artifacts.picoctf.net/c_titan/66/challenge.zip
$cd drop-in
$git log
</pre>       
    and see history of git commits and find  flag like this
<pre>
commit 3339c144a0c78dc2fbd3403d2fb37d3830be5d94 (HEAD -> master)
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:10:22 2024 +0000

    picoCTF{t1m3m@ch1n3_d3161c0f}

</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{t1m3m@ch1n3_d3161c0f}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on  git and see history of commits</p>
</body>
</html>

