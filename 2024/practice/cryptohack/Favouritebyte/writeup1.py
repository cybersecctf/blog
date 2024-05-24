#python
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
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