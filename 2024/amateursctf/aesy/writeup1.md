<title>aesy- amateurctf2024</title>

<!DOCTYPE html>
<html>

<body>
    <h1>aesy- amateurctf2024</h1>

    <h2>Challenge Description</h2>
    <p> Please aes-decrypt the flag for me: key: 8e29bd9f7a4f50e2485acd455bd6595ee1c6d029c8b3ef82eba0f28e59afcf9f ciphertext: abcdd57efb034baf82fc1920a618e6a7fa496e319b4db1746b7d7e3d1198f64f
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
we use this python code for get flag and print it as described in challenge
or any aes decrypt with key online or offline way
<pre>
#python
from Crypto.Cipher import AES
import binascii,sys

def aes_decrypt(key_hex, ciphertext_hex):

    key = binascii.unhexlify(key_hex)
    ciphertext = binascii.unhexlify(ciphertext_hex)
    
    cipher = AES.new(key, AES.MODE_ECB)
    
    decrypted_bytes = cipher.decrypt(ciphertext)
    return decrypted_bytes

def hex_to_ascii(hex_string):

    ascii_string = bytes.fromhex(hex_string).decode('utf-8')
    return ascii_string


ciphertext = 'abcdd57efb034baf82fc1920a618e6a7fa496e319b4db1746b7d7e3d1198f64f'
if len(sys.argv)>1:
     ciphertext=sys.argv[1]
key = '8e29bd9f7a4f50e2485acd455bd6595ee1c6d029c8b3ef82eba0f28e59afcf9f'
if len(sys.argv)>2:
 key=sys.argv[2]
decrypted_bytes = aes_decrypt(key, ciphertext)
decrypted_hex = binascii.hexlify(decrypted_bytes).decode()

decrypted_text = hex_to_ascii(decrypted_hex[:-2])

print(f"Decrypted text: {decrypted_text}")
</pre>
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">amateursCTF{w0w_3cb_a3s_1s_fun}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on develper tools in in chrome and web exploitations</p>
</body>
</html>

