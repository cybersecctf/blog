
<!DOCTYPE html>
<html>

<body>
    <h1>DESFUNCTIONAL- googlectf2024</h1>

    <h2>Challenge Description</h2>
    <p> A newbie friend of mine was trying to implement a secure server
for DES encryption and decryption but there seem to be some errors
unexpectedly creeping in the key. It is getting frustrating, please help 

<a href="https://cybersecctf.github.io/blog/2024/googlectf/googlectf2024/desfunctional/attachment.zip">attachment</a>
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
 this code below  being used here is DES3 (Triple DES), which is a symmetric-key block cipher that applies the Data Encryption Standard (DES) cipher algorithm three times to each data block.

In the context of your code, the challenge can be considered as the ciphertext that you want to decrypt, and the key is the secret information that allows you to decrypt the ciphertext or encrypt the plaintext. However, it’s important to note that the actual encryption and decryption using DES3 are not explicitly implemented in the provided code. Instead, the code communicates with a remote service or a local process that performs the encryption and decryption but for find correct encrypt and decrypt and keys should do it offline for find flag related to challenge on server.this code do local and server process on key ana  challenge.on online don't need import key and challenge should calculate and get it online
<pre>
from pwn import *
import blog
import binascii
import warnings
from Crypto.Cipher import DES3

# Connect to the remote service
host = 'desfunctional.2024.ctfcompetition.com'
port = 1337

def decrypt_offline(ciphertext, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def get_challenge(connection):
    connection.sendline(b'1')
    print(f"(1) Requesting Challenge...")
    response = connection.recvline().strip()
    return bytes.fromhex(response.decode())

def decrypt(connection, ciphertext):
    connection.sendline(b'2')
    connection.recvuntil(": ")
    connection.sendline(ciphertext.hex())
    response = connection.recvline().strip()
    return bytes.fromhex(response.decode())

def get_flag(connection, plaintext):
    connection.sendline(b'3')
    connection.recvuntil(": ")
    connection.sendline(plaintext.hex())
    response = connection.recvline().strip()
    return response

def detect_cycle(connection, to_decrypt):
    decrypts = set()
    decrypted_with_f = "0"
    for i in range(100):
        decrypted_text = decrypt(connection, bytes.fromhex(to_decrypt))
        decrypted_with_f = decrypted_text
        if decrypted_text in decrypts:
            break
        decrypts.add(decrypted_text)
    return decrypted_with_f

def solve(challenge=None, key=None, online=True):
    if online:
        connection = remote(host, port)
    else:
        return decrypt_offline(challenge, key)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        prompt = connection.recvuntil("flag\n")
        print(prompt.decode())
    
        if challenge is None:
            challenge = get_challenge(connection)
        print(f"[-] Received Challenge: {challenge.hex()}")

        prompt = connection.recvuntil("flag\n")
        print(prompt.decode())
        print( blog.solveup("cryptohack hex","encode",str(prompt)))  
        decrypted_with_f = detect_cycle(connection, "000000000000000000000000000000000000000000000000")
        iv = bytes(i ^ j for i, j in zip(decrypted_with_f[:8], decrypted_with_f[-8:]))
        print(f"[-] Calculated IV: {iv.hex()}")
        
        print("\n============= Repeat with masked challenge... ====================\n")
        trying = "f"*128
        masked_challenge = bytes(i ^ j for i, j in zip(bytes.fromhex(trying),challenge))
        decrypted_with_f = detect_cycle(connection, masked_challenge.hex())
        unmask_plaintext1 = bytes(i ^ j for i, j in zip(decrypted_with_f, bytes.fromhex(128*"f")))[:8]
        
        plaintext = unmask_plaintext1.hex()+decrypted_with_f[8:].hex()
      
   
        print(f"\nSummary:")
        print(f"[-] Calculated Plaintext: {plaintext}")
        print(f"[-] Calculated IV: {iv.hex()}")
        print("\n============= Getting the flag... ====================\n")

        if key is not None:
            plaintext = key

        flag_response = get_flag(connection, bytes.fromhex(plaintext))
        print(f"[-] Received Flag Response: {flag_response.decode()}")

if __name__ == "__main__" :
  solve()
  # Placeholder ciphertext and key for the purpose of this example
  ciphertext = b'\x01\x02\x03\x04\x05\x06\x07\x08'
  key = b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10'
  print(solve(challenge=ciphertext, key=key, online=False).hex())

</pre>        
       blog.solveup("cryptohack hex","decode",hex))
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTF{y0u_m4y_NOT_g3t_th3_k3y_but_y0u_m4y_NOT_g3t_th3_c1ph3rt3xt_as_w3ll}
</p>

    <h2>Conclusion</h2>
    <p>this is a medium  chanllenge for work on DES3 (Triple DES) with cipher and key</p>
</body>
</html>


