
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

def generate_key(key_size):
    """Generate a random key with a given size in bytes."""
    return get_random_bytes(key_size)

def encrypt(plaintext, key):
    """Encrypt the plaintext using the given key with AES algorithm."""
    # Generate a random initialization vector (IV)
    iv = get_random_bytes(16)
    # Create an AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Pad the plaintext to be a multiple of the block size
    padded_plaintext = pad(plaintext.encode('utf-8'), AES.block_size)
    # Encrypt the plaintext
    ciphertext = cipher.encrypt(padded_plaintext)
    # Encode the ciphertext and IV in base64 to make it easier to store/transmit
    return base64.b64encode(iv + ciphertext).decode('utf-8')

def decrypt(ciphertext, key):
    """Decrypt the ciphertext using the given key with AES algorithm."""
    # Decode the ciphertext from base64
    ciphertext = base64.b64decode(ciphertext)
    # Extract the IV and the actual ciphertext
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]
    # Create an AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Decrypt the ciphertext and remove padding
    padded_plaintext = cipher.decrypt(actual_ciphertext)
    plaintext = unpad(padded_plaintext, AES.block_size)
    return plaintext.decode('utf-8')
def findpass(file,type,key):
  if type=="AES256":
   return blog.solveup("garden",f"gpg  --decrypt {file}","","")
   
  if type=="AES256-CBC": 
    return blog.solveup("garden",f'gpg aes-256-cbc -d -in {file}',"","")
  if type=="CAMELLIA256": 
   return blog.solveup('garden',f'gpg  --cipher-algo CAMELLIA256 --decrypt {file}',"")
  
  return f"invalid type {type}"
def solve(operation,val,key):
  if "findpass" in operation:
      s=operation.split()
      return findpass(val,s[1],key)   
  if operation=="encrypt":
       return encrypt(val, key)   
  else:
       return decrypt(val,key)      
# Example usage
if __name__ == "__main__":
    # Generate a random 256-bit (32-byte) key
    blog.solveup("garden","unzip intro-to-cryptography.zip","")  
    key = generate_key(32)

    # Define the plaintext message
    plaintext = "This is a secret message."

    # Encrypt the plaintext
    encrypted_message = solve("encrypt",plaintext, key)
    print(f"Encrypted message: {encrypted_message}")

    # Decrypt the message back to plaintext
    decrypted_message = solve("decrypt",encrypted_message, key)
    print(f"Decrypted message: {decrypted_message}")
    
    print(solve("findpass AES256","intro-to-cryptography/task02/quote01.txt.gpg","s!kR3T55"))
    print(solve("findpass AES256-CBC","intro-to-cryptography/task02/quote02","s!kR3T55"))
    print(solve("findpass CAMELLIA256","intro-to-cryptography/task02/quote03.txt.gpg","s!kR3T55"))
           
