<!DOCTYPE html>
<html>
<head>
    
</head>
<body>
    <h1>picopractice(2021)- information Challenge Writeup</h1>

    <h2>Challenge Description</h2>
    <p>AUTHOR: SUSIE

Description
Files can always be changed in a secret way. Can you find the flag? link:cat.jpg
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        <li>in every file in image for get flag is better use command $exiftool cat.jpg or strings and see if can get flag and see hints also)</li>
        <li>on exiftool cat.jpg  license is 'cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9'   that is like base64
<li>use with pytho code<pre>import base64
a = 'cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9'
print(base64.b64decode(a))</pre> for find if is base64 and yes work can use another encodings
    </ol>

    <h2>Flag</h2>
    <p class="flag">picoCTF{the_m3tadata_1s_modified}</p>

    <h2>Conclusion</h2>
    <p>easy ctf for cryptography and forensics and  base64 with  python code</p>
</body>
</html>
