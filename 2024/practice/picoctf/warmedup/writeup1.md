<title>picoctf 2019- Warmed Up Challenge Writeup</title>

<!DOCTYPE html>
<html>

<body>
    <h1>picoctf 2019- Warmed Up Challenge Writeup</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: SANJAY C/DANNY TUNITIS

Description
What is 0x3D (base 16) in decimal (base 10)?
  
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        <li> we can use this python code<pre>
#python
import sys
val='0x3D'
if len(sys.argv)>1:
    val=sys.argv[1]
print(int(val,16))</pre> </li>
        <li>or use online tool for convert them
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">flag{61}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on cryptography and convert decimal to python ir online</p>
</body>
</html>
