
<!DOCTYPE html>
<html>

<body>
    <h1>Character Encoding- ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> In the computing industry, standards are established to facilitate information interchanges among American coders. Unfortunately, I've made communication a little bit more difficult. Can you figure this one out? 41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
      we can use this code to convert hex to asscii
<pre>
#python
#usage -v  hexnumbers [hex/base64 default hex]
import sys
import base64
from binascii import unhexlify
s='41424354467B34354331315F31355F55353346554C7D'
type='hex'
if len(sys.argv)>1:
 s=sys.argv[1]
if len(sys.argv)>2:
 type=sys.argv[2]
result = unhexlify(s)
if type=='base64':
  result = base64.b64encode(result)
print(result) 
</pre>
       
    and after run code can get flag
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">ABCTF{45C11_15_U53FUL}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for convt hex to ascii or base64</p>
</body>
</html>

