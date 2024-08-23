<title>Export-grade- cryptohack</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Export-grade- cryptohack</h1>

    <h2>Challenge Description</h2>
    <p> 
Alice and Bob are using legacy codebases and need to negotiate parameters they both support. You've man-in-the-middled this negotiation step, and can passively observe thereafter. How are you going to ruin their day this time?

Connect at socket.cryptohack.org 13379
 </p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
Intercepted from Alice: {"supported": ["DH1536", "DH1024", "DH512", "DH256", "DH128", "DH64"]}
Send to Bob: {"supported":["DH64"]}                                                                                                                                     
Intercepted from Bob: {"chosen": "DH64"}
Send to Alice: {"chosen": "DH64"}        
Intercepted from Alice: {"p": "0xde26ab651b92a129", "g": "0x2", "A": "0x637430f37c694fa7"}
Intercepted from Bob: {"B": "0x7249365a2a8c71ff"}                                                                                                                       
Intercepted from Alice: {"iv": "31077c28f19c90297f3da6dff6ca3019", "encrypted_flag": "0ebb53dab97122361cfa8cdbb5ddc092a5af41452aae8def0d27181b6ee89839"}
"""
Here’s the Python code to achieve this:
<pre>
#python
p = "0xde26ab651b92a129"
g = "0x2"
A = "0x637430f37c694fa7"
B = "0x7249365a2a8c71ff"
iv =  "31077c28f19c90297f3da6dff6ca3019"
encrypted_flag = "0ebb53dab97122361cfa8cdbb5ddc092a5af41452aae8def0d27181b6ee89839"

p = int(p, 16)
g = int(g, 16)
A = int(A, 16)
B = int(B, 16)
iv = bytes.fromhex(iv)
encrypted_flag = bytes.fromhex(encrypted_flag)

from Crypto.Cipher import AES
from Crypto.Util import number
import hashlib

def decrypt(secret, iv, cipher):
    sha1 = hashlib.sha1()
    sha1.update(str(secret).encode())
    key = sha1.digest()[:16]
    aes = AES.new(key, AES.MODE_CBC, iv)
    plain = aes.decrypt(cipher)
    print(plain)

"""
A = pow(g, a, p)
B = pow(g, b, p)

ka = pow(B, a, p)
kb = pow(A, b, p)
"""
# Use Discrete logarithm calculator https://www.alpertron.com.ar/DILOG.HTM to find out Alice's secret key ``a``
a = 7596561454821291306
secret = pow(B, a, p)
decrypt(secret, iv, encrypted_flag)
</pre> 
 
 
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">crypto{d0wn6r4d35_4r3_d4n63r0u5}</p>

    <h2>Conclusion</h2>
    <p>this is a    medium chanllenge for Shared Secret Derivation (Diffie-Hellman) and </p>
</body>
</html>







