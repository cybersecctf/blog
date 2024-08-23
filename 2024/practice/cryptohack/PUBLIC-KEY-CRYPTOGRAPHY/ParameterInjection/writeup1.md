<title>Parameter Injection- cryptohack</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Parameter Injection- cryptohack</h1>

    <h2>Challenge Description</h2>
    <p> 
You're in a position to not only intercept Alice and Bob's DH key exchange, but also rewrite their messages. Think about how you can play with the DH equation that they calculate, and therefore sidestep the need to crack any discrete logarithm problem.

Use the script from "Diffie-Hellman Starter 5" to decrypt the flag once you've recovered the shared secret.

Connect at socket.cryptohack.org 13371
 </p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
this challenge is about :
Shared Secret Derivation (Diffie-Hellman):
Alice and you both generate secret integers: (a) (Alice’s secret) and (b) (your secret).
Calculate the public keys:
Alice’s public key: (A = g^a \mod p)
Your public key: (B = g^b \mod p)
The shared secret is derived as follows:
Shared secret: (s = A^b \mod p = B^a \mod p)
Decrypting the Ciphertext:
Alice sends you the ciphertext and IV (Initialization Vector).
You can use the shared secret as the AES key to decrypt the ciphertext.
Here’s the Python code to achieve this:
<pre>
import pwn
import json
import hashlib
import blog
from Crypto.Cipher import AES
host = "socket.cryptohack.org"
port = 13371
def solve(p=0,g=0,a=0,B=0):
    pr = pwn.connect(host, port)
    try:
        pr.readuntil(": ")
        line = json.loads(pr.readline().strip().decode())
        #p = int(line['p'][2:].strip('f'), 16)
        p = int(line['p'], 16)
        g = int(line['g'], 16)
        A = int(line['A'], 16)

        payload = json.dumps({"p":hex(p),"g":hex(g),"A":hex(p)})
        print(payload, len(payload))
        pr.sendlineafter(": ", payload)

        pr.readuntil(": ")
        line = json.loads(pr.readline().strip().decode())
        B = int(line['B'], 16)

        payload = json.dumps({"B":hex(p)})
        print(payload, len(payload))
        pr.sendlineafter(": ", payload)

        pr.readuntil(": ")
        line = json.loads(pr.readline().strip().decode())
        print(line)

        iv = bytes.fromhex(line['iv'])
        encrypted_flag = bytes.fromhex(line['encrypted_flag'])
        sha1 = hashlib.sha1()
        secret = 0
        sha1.update(str(secret).encode())
        key = sha1.digest()[:16]
        aes = AES.new(key, AES.MODE_CBC, iv)
        print(aes.decrypt(encrypted_flag))
    finally:
        pr.close()

exploit()
 
</pre> 
 
 
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">crypto{n1c3_0n3_m4ll0ry!!!!!!!!}</p>

    <h2>Conclusion</h2>
    <p>this is a    medium chanllenge for Shared Secret Derivation (Diffie-Hellman) and intercept message with it</p>
</body>
</html>







