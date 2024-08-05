
from Crypto.Cipher import AES
from pwn import xor
import requests
def encrypt():
    url = "http://aes.cryptohack.org//ecbcbcwtf/encrypt_flag/"
    response = requests.get(url)
    return response.json()['ciphertext']
def decrypt(data):
    url = "http://aes.cryptohack.org/ecbcbcwtf/decrypt/"
    response = requests.get(url + data + '/')
    return response.json()['plaintext']
def solvecrypto(data):
 flag = encrypt()
 f = [flag[i:i+32] for i in [0,32,64]]
 vi = f[0:(len(f)-1)]
 f = f[1:]
 for i in range(len(f)):
    f[i] = decrypt(f[i])
 for i in range(len(f)):
    f[i] = xor(bytes.fromhex(f[i]),bytes.fromhex(vi[i]))
 flag = ""
 for i in f:
    flag += i.decode()
 return flag 
def solve(data,key,operation=""):
    # Your provided ciphertext
    if operation=="cryptohack":
         return solvecrypto(data)
         return
    ciphertext = bytes.fromhex(data)
    # Initialization vector and ciphertext blocks
    iv = ciphertext[:16]
    c1 = ciphertext[16:32]
    c2 = ciphertext[32:]
    # Decrypt the blocks
    d1 = decrypted(c1, key)
    d2 = decrypted(c2, key)
    # XOR the decrypted blocks with the previous ciphertext block to get the plaintext
    flag1 = long_to_bytes(bytes_to_long(d1) ^ bytes_to_long(iv))
    flag2 = long_to_bytes(bytes_to_long(d2) ^ bytes_to_long(c1))
    # Combine the plaintext blocks
    flag = flag1 + flag2
    return flag
def decrypt(data):
    url = "http://aes.cryptohack.org/ecbcbcwtf/decrypt/"
    response = requests.get(url + data + '/')
    return response.json()['plaintext']
# Example usage:data from cryptohack
if __name__ == "__main__" :
 data = "d7a86a611700f8cba208533e232082075c6efa40e818dd5b2366982ee2f61c722b2ad5032e96c2e163436e220a03eee9"
 decrypted_data = solve(data,"","cryptohack")
 print(decrypted_data)
