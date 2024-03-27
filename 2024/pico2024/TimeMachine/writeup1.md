
<!DOCTYPE html>
<html>
 
<body>
    <h1>Super SSH-picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p>AUTHOR: JEFFERY JOHN

Description
What was I last working on? I remember writing a note to help me remember...
You can download the challenge files here:
challenge.zip:https://artifacts.picoctf.net/c_titan/160/challenge.zip
</p>
ssh
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
 this is like this competion do this
<pre>
$wget https://artifacts.picoctf.net/c_titan/66/challenge.zip
$unzip challenge.zip
$git log (see commits)
$git show 3899edb7f3110d613c72ad40083fd8feeef703d0(see special commit have flag
in this competetion can see flag without git show
</pre>
and get flag
<pre>
┌──(kali㉿kali)-[~/…/2024/pico2024/TimeMachine/drop-in]
└─$ git log                                          
commit 3339c144a0c78dc2fbd3403d2fb37d3830be5d94 (HEAD -> master)
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:10:22 2024 +0000

    picoCTF{t1m3m@ch1n3_d3161c0f}
</pre>
     </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">   picoCTF{t1m3m@ch1n3_d3161c0f}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work in github and commit history
</body>
</html>

