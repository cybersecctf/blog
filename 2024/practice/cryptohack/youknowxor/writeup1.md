<title>You either know, XOR you don't- cryptohack</title>
 
<!DOCTYPE html>
<html>

<body>
    <h1>You either know, XOR you don't- cryptohack</h1>

    <h2>Challenge Description</h2>
    <p>You either know, XOR you don't 
I've encrypted the flag with my secret key, you'll never be able to guess it.

Remember the flag format and how it might help you in this challenge!


0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
We know that is a XOR-cipher, the first thing we can try, as suggested, it's to look for a part of the key by xoring the first seven character of the FLAG which is "crypto{" and the same number of character from our ciphertext (code section "First Step").
As result we have "myXORke". By using not so much immgination we can try myXORkey as key and by repeating it over the lenght of our ciphertext and xoring with all the cipher we get our flag (code section "Second Step").
<pre>
#python
import sys
from binascii import unhexlify
import blog
def brute(input, key):
    if len(input) != len(key):
        return "Failed!"
    output = b''
    for b1, b2 in zip(input, key):
        output += bytes([b1 ^ b2])
    try:
        return output.decode("utf-8")
    except:
        return "Cannot Decode some bytes"
def solve(data,search="crypto{"):
 cipher = unhexlify(data)
 print("[-] CIPHER: {}".format(cipher))
 # First Step
 key_part = brute(cipher[:7], search.encode())
 print("[-] PARTIAL KEY FOUND: {}".format(key_part))
 # Second Step
 key = (key_part + "y").encode()
 key += key * int((len(cipher) - len(key))/len(key))
 key += key[:((len(cipher) - len(key))%len(key))]
 print("[-] Decoding using KEY: {}".format(key))
 plain = brute(cipher, key)
 return plain 
if __name__ == "__main__" :
 data=blog.set("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104",1)
 search=blog.set("crypto{",2)
 plain=solve(data,search)
 print("\n[*] FLAG: {}".format(plain))
</pre>
 
 
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">crypto{0x10_15_my_f4v0ur173_by7e}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on single byte XOR-cypher with partiak key known</p>
</body>
</html>

