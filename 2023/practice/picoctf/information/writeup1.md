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
     in this challenge i use <pre> 
$exiftool $1
</pre>(if use in file)or <pre>$exiftool  cat.jpg </pre>  

in       exiftool cat.jpg  license is 'cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9'   that is like base64
use with pytho code
<pre>
import base64,sys
try:
 a="cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMWY4MzI2MTV9"
 if len(sys.argv)>1:
  a = sys.argv[1]
 print(base64.b64decode(a))
except:
 print("not a base 64 nymber")
</pre > and run it for get flag from base64
    </ol>

    <h2>Flag</h2>
    <p class="flag">picoCTF{the_m3tadata_1s_modified}</p>

    <h2>Conclusion</h2>
    <p>easy ctf for cryptography and forensics and  base64 with  python code</p>
</body>
</html>
