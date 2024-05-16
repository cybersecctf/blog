#python
import sys
from binascii import unhexlify
import string
#python 
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
data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
key="crypto"
if len(sys.argv)>1:
   data=sys.argv[1]  
else:
   print("usage -v hex search(text in text{ for example")  
if len(sys.argv)>2:
   search=sys.argv[2]                
decoded = unhexlify(data)

print("[-] HEX_DECODE: {}\n".format(decoded),":",decoded.decode())

result = {}
for i in range(256):
    result[i] = (single_byte_xor(decoded, i))
    #print("[-] KEY: {}\nSTRING: {}".format(i,single_byte_xor(decoded, i)))

print("[*] FLAG: {}".format([s for s in result.values() if key in s]))
#modified from https://captainmich.github.io/programming_language/CTF/Challenge/CryptoHack/general.html code
