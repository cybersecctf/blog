<title>First Grep- challengename Challenge Writeup(first save it)</title>

<!DOCTYPE html>
<html>

<body>
    <h1>First Grep- challengename Challenge Writeup(first save it)</h1>

    <h2>Challenge Description</h2>
    <p> Tags: 
AUTHOR: ALEX FULTON/DANNY TUNITIS

Description
Can you find the flag in 
<a href="https://jupiter.challenges.picoctf.org/static/495d43ee4a2b9f345a4307d053b4d88d/file">file</a>? This would be really tedious to look through manually, something tells me there is a better way.
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
       we download file and grep pico from file with run this command and get flag
<pre>
#!/bin/bash
strings $1|grep $2
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{grep_is_good_to_find_things_dba08a45}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge  for grep flag from file</p>
</body>
</html>

