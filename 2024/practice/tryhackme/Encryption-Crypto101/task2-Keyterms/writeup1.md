 

<!DOCTYPE html>
<html>
 
<body>
    <h1>tryhackme---Key terms  Writeup </h1>

    <h2>Challenge Description</h2>
    <p> Many of these key terms are shared with https://tryhackme.com/room/hashingcrypto101, so you might be able to skip over some if you're already familiar.

Ciphertext - The result of encrypting a plaintext, encrypted data

Cipher - A method of encrypting or decrypting data. Modern ciphers are cryptographic, but there are many non cryptographic ciphers like Caesar.

Plaintext - Data before encryption, often text but not always. Could be a photograph or other file

Encryption - Transforming data into ciphertext, using a cipher.

Encoding - NOT a form of encryption, just a form of data representation like base64. Immediately reversible.

Key - Some information that is needed to correctly decrypt the ciphertext and obtain the plaintext.

Passphrase - Separate to the key, a passphrase is similar to a password and used to protect a key.

Asymmetric encryption - Uses different keys to encrypt and decrypt.

Symmetric encryption - Uses the same key to encrypt and decrypt

Brute force - Attacking cryptography by trying every different password or every different key

Cryptanalysis - Attacking cryptography by finding a weakness in the underlying maths

Alice and Bob - Used to represent 2 people who generally want to communicate. They’re named Alice and Bob because this gives them the initials A and B. https://en.wikipedia.org/wiki/Alice_and_Bob for more information, as these extend through the alphabet to represent many different people involved in communication.

WARNING: This room is very theory heavy. Cryptography is a big topic, and this room is designed to just scratch the surface.

Answer the questions below
I agree not to complain too much about how theory heavy this room is.
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>this is a solution for get answer by terminal and search here

<pre>
import blog

import os,subprocess
def search_json(term,file="def.json"):
    a=blog.set("def.json",1,"file")
    return a.get(term, "Term not found")

def solve( search="Cryptanalysis"):
    return search_json(search)
   
     
if __name__ == "__main__" :
  print(solve("Alice and Bob"))
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{more_than_m33ts_the_3y3657BaB2C}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on develper tools in in chrome and web exploitations</p>

</body>
</html>
