
<!DOCTYPE html>
<html>

<body>
    <h1>Symmetry- cryptohack</h1>

    <h2>Challenge Description</h2>
    <p>Some block cipher modes, such as OFB, CTR, or CFB, turn a block cipher into a stream cipher. The idea behind stream ciphers is to produce a pseudorandom keystream which is then XORed with the plaintext. One advantage of stream ciphers is that they can work of plaintext of arbitrary length, with no padding required.

OFB is an obscure cipher mode, with no real benefits these days over using CTR. This challenge introduces an unusual property of OFB.

Play at <a href=" https://aes.cryptohack.org/symmetry"> https://aes.cryptohack.org/symmetry</a>
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
For this challenge we have been given encrypt and encrypt_flag function both of which uses OFB(Output feedback) mode of encryption. The first 32 bytes of the return of encrypt_flag is IV(initialisation vector). The encrypt function take the plaintext and gives the ciphertext. As one can see let k = AES(KEY) then ciphertext = plaintext ^ k. So we can say that plaintext = ciphertext ^ k. So we can get the key by XORing the first 16 bytes of the return of encrypt_flag with the ciphertext by providing the ciphertext as the plaintext to the encrypt function.
<pre>
#python
flag="40d5846aafd4cb777e621bb1a4deccd49157cf23e4be8facb141092287312a6975125e497715e944ce74f8588bdf3290ab"
import requests
import json
from pwn import *

url = 'http://aes.cryptohack.org/symmetry/'

def encrypt(plain, iv):
    r = requests.get(url + "encrypt/" + plain + "/" + iv + "/")
    res = r.json()['ciphertext']
    return res

ef = "40d5846aafd4cb777e621bb1a4deccd49157cf23e4be8facb141092287312a6975125e497715e944ce74f8588bdf3290ab"
iv = ef[:32]
cip = ef[32:]

ret = encrypt(cip, iv)
print(bytes.fromhex(ret))
</pre>        
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">crypto{0fb_15_5ymm37r1c4l_!!!11!}
</p>

    <h2>Conclusion</h2>
    <p>this is a medium challenge for </p>
</body>
</html>


