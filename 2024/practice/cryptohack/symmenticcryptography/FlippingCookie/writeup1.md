
<!DOCTYPE html>
<html>

<body>
    <h1>Flipping Cookie- cryptohack</h1>

    <h2>Challenge Description</h2>
    <p> https://aes.cryptohack.org/flipping_cookie <a href="https://aes.cryptohack.org/flipping_cookie">https://aes.cryptohack.org/flipping_cookie</a>
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
we see link get_cookie returns a cipher text of plain text containing "admin=False", notice that the IV is returned along with the cipher text, the first 16 bytes of the cipher text are IV used for encryption. In check_admin the input cipher text is decrypted with giving IV, it returns the flag if the decrypted text include string "admin=True".
<code>

</code>
<pre>
#python
from datetime import datetime, timedelta
import requests
import blog
def print_blk(hex_blks, sz):
   for i in range(0, len(hex_blks), sz):
       print(hex_blks[i:i+sz], ' ', end='')
   print()

def flip(cookie, plain):
    start = plain.find(b'admin=False')
    cookie = bytes.fromhex(cookie)
    iv = [0xff]*16
    cipher_fake = list(cookie)
    fake = b';admin=True;'
    for i in range(len(fake)):
       cipher_fake[16+i] = plain[16+i] ^ cookie[16+i] ^ fake[i]
       iv[start+i] = plain[start+i] ^ cookie[start+i] ^ fake[i]

    cipher_fake = bytes(cipher_fake).hex()
    iv = bytes(iv).hex()
    return cipher_fake, iv

def request_cookie():
    r = requests.get("http://aes.cryptohack.org/flipping_cookie/get_cookie/")
    return r.json()["cookie"]

def request_check_admin(cookie, iv):
    r = requests.get("http://aes.cryptohack.org/flipping_cookie/check_admin/{}/{}/".format(cookie, iv))
    return r.json()
def solve(plain):
 
 cookie = request_cookie()
 cookie, iv = flip(cookie, plain)
 return request_check_admin(cookie, iv)
if __name__ == "__main__" :
 expires_at = (datetime.today() + timedelta(days=1)).strftime("%s")
 plain = blog.set(f"admin=False;expiry={expires_at}".encode(),1)
 print(solve(plain))
</pre>        
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">crypto{4u7h3n71c4710n_15_3553n714l}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on AES-CBC, decryption on web and cookie and admin cookie</p>
</body>
</html>


