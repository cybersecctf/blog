
<!DOCTYPE html>
<html>

<body>
    <h1>Passwords as Keys- cryptohack</h1>

    <h2>Challenge Description</h2>
    <p> It is essential that keys in symmetric-key algorithms are random bytes, instead of passwords or other predictable data. The random bytes should be generated using a cryptographically-secure pseudorandom number generator (CSPRNG). If the keys are predictable in any way, then the security level of the cipher is reduced and it may be possible for an attacker who gets access to the ciphertext to decrypt it.

Just because a key looks like it is formed of random bytes, does not mean that it necessarily is. In this case the key has been derived from a simple password using a hashing function, which makes the ciphertext crackable.

For this challenge you may script your HTTP requests to the endpoints, or alternatively attack the ciphertext offline. Good luck!

Play at <a href="https://aes.cryptohack.org/passwords_as_keys">https://aes.cryptohack.org/passwords_as_keys</a>
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
we open link and get see source in source is link and get cipher and wordlist and do attack for get flag and key like this code
<pre>
import hashlib
import random
from Crypto.Cipher import AES
import requests
import sys
import binascii
import blog
# /usr/share/dict/words from
# https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words



#@chal.route('/passwords_as_keys/decrypt/<ciphertext>/<password_hash>/')
def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


#@chal.route('/passwords_as_keys/encrypt_flag/')
def encrypt_flag():
    cipher = AES.new(KEY, AES.MODE_ECB)
    encrypted = cipher.encrypt(FLAG.encode())

    return {"ciphertext": encrypted.hex()}

def solve(ciphertext_hex,wordlist):

 with open(wordlist) as f:
    words = [w.strip() for w in f.readlines()]
 keyword = random.choice(words)
 KEY = hashlib.md5(keyword.encode()).digest()
 FLAG = ""
 with open('words', 'r') as f:
    for word in f:
        word = word.strip()
        attempted_key = hashlib.md5(word.encode()).hexdigest()
        ciphertext = bytes.fromhex(ciphertext_hex)
        key = bytes.fromhex(attempted_key)
        cipher = AES.new(key, AES.MODE_ECB)
        try:
            decrypted = cipher.decrypt(ciphertext)
            result = binascii.unhexlify(decrypted.hex())
            if result.startswith('crypto{'.encode()):
                print("key is %s" % word)
                print(result.decode('utf-8'))
                return
        except ValueError as e:
            print(str(e))
            continue
if __name__ == "__main__" :
  s=blog.set("c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66",1)
  wordlist=blog.set("words",2)

  solve(s,wordlist)
</pre>
      
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">crypto{k3y5__r__n07__p455w0rdz?}

</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for aes attack for find key and decrypt cipher hex to text in aes</p>
</body>
</html>


