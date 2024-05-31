<!DOCTYPE html>
<html>

<body>
    <h1>Favourite byte- cryptohack</h1>

    <h2>Challenge Description</h2>
    <p> For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles.

I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.

73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
This is a single byte XOR-cypher. In order to break it we need to xor each single byte of our decoded data with one single byte at time. Iterating through all the possible bytes we finally get our flag
<pre>
#python
import blog
from binascii import unhexlify
import string
def single_byte_xor(input, key):
    if len(chr(key)) != 1:
      raise "KEY LENGTH EXCEPTION: In single_byte_xor key must be 1 byte long!"

    output = b''
    for b in input:
        output += bytes([b ^ key])

    try:
        return output.decode("utf-8")
    except:
        return "Cannot Decode some bytes"
def solve(data,key):        
 decoded = unhexlify(data)
 print("[-] HEX_DECODE: {}\n".format(decoded),":",decoded.decode())
 result = {}
 for i in range(256):
    result[i] = (single_byte_xor(decoded, i))
 return "{}".format([s for s in result.values() if key in s])
if __name__ == "__main__" :
 data=blog.set("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d",1)
 key=blog.set("crypto",2)
 print(solve(data,key))
#modified from https://captainmich.github.io/programming_language/CTF/Challenge/CryptoHack/general.html code
</pre>
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">crypto{0x10_15_my_f4v0ur173_by7e}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on single byte XOR-cypher</p>
</body>
</html>

