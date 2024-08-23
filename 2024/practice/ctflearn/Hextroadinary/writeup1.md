<title>Hextroadinary - ctflearn</title>

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
import blog

def solve(v1,v2):
 v3=v1^v2
 v4="hex"
 if len(sys.argv)>3:
  v4=sys.argv[3]
 if v4!="hex":
   return v3
 else :
   return hex(v3)
if __name__ == "__main__" :
 v1=blog.set(0xc4115,1) 
 v2=blog.set(0x4cf8,2)
 print(solve(v1,v2))
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

