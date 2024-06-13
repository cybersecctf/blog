
<!DOCTYPE html>
<html>

<body>
    <h1>ECB Oracle- cryptohack</h1>

    <h2>Challenge Description</h2>
    <p> ECB is the most simple mode, with each plaintext block encrypted entirely independently. In this case, your input is prepended to the secret flag and encrypted and that's it. We don't even provide a decrypt function. Perhaps you don't need a padding oracle when you have an "ECB oracle"?

Play at <a href="https://aes.cryptohack.org/ecb_oracle">https://aes.cryptohack.org/ecb_oracle</a>
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
ECB is the most simple mode, with each plaintext block encrypted entirely independently. In ECB mode, identical blocks of plaintext are encrypted to identical blocks of ciphertext. So we have to look for pattern in the blocks of ciphertext. To solve this we can think of one example.

Suppose the first 16 bytes are 0 and if the first 17 bytes are 0 in both cases the AES Encryption of first block will always be same as it contains 16 0s.
If the flag starts with crypto{ then if I pad with 15 000000000000000s or with 15 000000000000000c in both the cases the first block will be 000000000000000c and will have same encryption for the starting block.
We just bruteforced the first char of the flag. We can do this for whole flag to find the flag.
<pre>
#python
#this is a code for encrypt and decrypt in aes with key and bruteforce of this cryptohack problem
import requests
import time
import string
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
def encrypt(payload):
    url = "http://aes.cryptohack.org/ecb_oracle/encrypt/"
    r = requests.get(url + payload + '/')
    return r.json()['ciphertext']
def print_blk(hex_blks, sz):
   for i in range(0, len(hex_blks), sz):
       print(hex_blks[i:i+sz], ' ', end='')
   print()

def bruteforce():
    flag = ''
    total = 32 - 1
    alphabet = '_'+'@'+'}'+string.digits+string.ascii_lowercase+string.ascii_uppercase

    while True:
        payload = '1' * (total-len(flag))
        expected = encrypt(payload.encode().hex())
        print('E', '', end='')
        print_blk(expected, 32)
        
        for c in alphabet: 
            res = encrypt(bytes.hex((payload + flag + c).encode()))
            print(c, '', end='')
            print_blk(res, 32)
            if res[32:64] == expected[32:64]:
                flag += c
                print(flag)
                break
            time.sleep(1)

        if flag.endswith('}'): break
def checkkey(key):
    if len(key) not in [16, 24, 32]:
            # Ensure the key is of valid length (16, 24, or 32 bytes)
             #and getcipher      
        raise ValueError("Key must be 16, 24, or 32 bytes long.")
    else:     
        cipher = AES.new(key, AES.MODE_ECB)
        return cipher             
def solve(operation, value, key):
    
    if operation == 'encode':
        # Encrypt the value
        cipher=checkkey(key) 
        encrypted_value = cipher.encrypt(pad(value, AES.block_size))
        return encrypted_value.hex()
    elif operation == 'decode':
        # Decrypt the value
        cipher=checkkey(key)                
        decrypted_value = unpad(cipher.decrypt(bytes.fromhex(value)), AES.block_size)
        return decrypted_value.decode()
    elif operation=="bruteforce":
               bruteforce()     
    else:
        raise ValueError("Operation must be 'encode' or 'decode'.")
if __name__ == "__main__" :
  # Example usage:
  # Encoding (encryption)
  key = b'DefaultKey123456'
  message= b'This is a secret message.'
  encrypted_message = solve('encode', message,key)
  print("Encrypted:", encrypted_message)
  # Decoding (decryption)
  decrypted_message = solve('decode', encrypted_message,key)
  print("Decrypted:", decrypted_message)
  print("flag is",solve("bruteforce","",""))
</pre>        
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">crypto{p3n6u1n5_h473_3cb}
</p>

    <h2>Conclusion</h2>
    <p>this is a medium chanllenge for work on ecb decrypt encrypt bruteforce</p>
</body>
</html>


