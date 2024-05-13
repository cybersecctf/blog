
<!DOCTYPE html>
<html>

<body>
    <h1>Hextroadinary - ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> Meet ROXy, a coder obsessed with being exclusively the worlds best hacker. She specializes in short cryptic hard to decipher secret codes. The below hex values for example, she did something with them to generate a secret code, can you figure out what? Your answer should start with 0x.

0xc4115 0x4cf8
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
       in this challenge we should xor two value with ^ and convert it to hex and find value
also can use this code
<pre>
#python
import sys
v1=0xc4115 
v2=0x4cf8
if len(sys.argv)>1:
 v1=sys.argv[1]
if len(sys.argv)>2:
  v2=sys.argv[2]
v3=v1^v2
v4="hex"
if len(sys.argv)>3:
  v4=sys.argv[3]
if v4!="hex":
   print(v3)
else :
   print(hex(v3))
</pre>
    and get flag
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlearn{0xc0ded}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for xor and convert decimal to hex and crypto</p>
</body>
</html>

