<!DOCTYPE html>
<html>

<body>
    <h1>BruXOR- ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> There is a technique called bruteforce. Message: q{vpln'bH_varHuebcrqxetrHOXEj No key! Just brute .. brute .. brute ... :D
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
       this is using xor bruteforce technic that is decrypt/encrypt with XOR cipher (eXclusive OR), a moder cryptographic method that consists in encrypting a binary message with a repeated key using a XOR multiplication.you can use online tool like <a href="https://www.dcode.fr/xor-cipher">this</a> or python code like this
<pre>
from itertools import cycle
import blog

def solve(ciphertext, search, key_length):
    # Generate all possible keys
    keys = [bytes([i]) * key_length for i in range(256)]
    
    for key in keys:
        plaintext = ''.join(chr(c ^ k) for c, k in zip(ciphertext.encode(), cycle(key)))
        if plaintext.startswith(search):
            return f"Key: {key}, Message: {plaintext}"
    return "flag not found"
if __name__ == "__main__" :
 ciphertext = blog.set("q{vpln'bH_varHuebcrqxetrHOXEj",1)
 search = blog.set('flag',2)
 key_length = blog.set(1,3)  # replace with your key length
 print(solve(ciphertext, search, key_length))

</pre>
and after run it can get flag and key
<pre>Key: b'\x17', Message: flag{y0u_Have_bruteforce_XOR}
</pre>
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">flag{y0u_Have_bruteforce_XOR}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on d XOR cipher  brutuforce and crypto</p>
</body>
</html>


