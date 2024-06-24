
from pwn import *
import binascii
import warnings
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
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
  #solve()
  # Placeholder ciphertext and key for the purpose of this example
  ciphertext =blog.set( b'\x01\x02\x03\x04\x05\x06\x07\x08',1)
  key = blog.set(b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10',2)
  print(solve(challenge=ciphertext, key=key, online=False).hex())

