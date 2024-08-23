<title>Random cipher- spcsctf</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Random cipher- spcsctf</h1>

    <h2>Challenge Description</h2>
    <p> 
You have received an encryption procedure that uses random numbers and text encrypted with it.

Restore the original message and find the flag in it

</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
<pre>
from random import *
def encrypt(text):
    key = randint(1, 2 * len(text))
    print (ord(text[0]), key)
    result = []

    for c in text:
        result.append(ord(c) + (ord(c) % key))
        key = key + 1

    return result
def decrypt(d):
 s=d-ord('G')
 s=s^ord('g')
 return s
        
print(decrypt(200))
print(chr(230^200))
</pre>
#grodno     
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">0
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work onsocket code and competetion style </p>
</body>
</html>


