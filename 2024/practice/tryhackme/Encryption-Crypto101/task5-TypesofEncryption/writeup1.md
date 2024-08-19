 

<!DOCTYPE html>
<html>
 <title>tryhackme---tas5-Types of Encryption  Writeup </title> 
<body>
    <h1>tryhackme---tas5-Types of Encryption  Writeup </h1>

    <h2>Challenge Description</h2>
    <p> The two main categories of Encryption are symmetric and asymmetric.

Symmetric encryption uses the same key to encrypt and decrypt the data. Examples of Symmetric encryption are DES (Broken) and AES. These algorithms tend to be faster than asymmetric cryptography, and use smaller keys (128 or 256 bit keys are common for AES, DES keys are 56 bits long).

Asymmetric encryption uses a pair of keys, one to encrypt and the other in the pair to decrypt. Examples are RSA and Elliptic Curve Cryptography. Normally these keys are referred to as a public key and a private key. Data encrypted with the private key can be decrypted with the public key, and vice versa. Your private key needs to be kept private, hence the name. Asymmetric encryption tends to be slower and uses larger keys, for example RSA typically uses 2048 to 4096 bit keys.

RSA and Elliptic Curve cryptography are based around different mathematically difficult (intractable) problems, which give them their strength. More about RSA later.
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>after using binawalk and exiftool not working using 

<pre>
import blog
import os,subprocess
def solve(term, file="sol.json"):
    return blog.solveup("search json",term,file)
if __name__ == "__main__" :
  print(solve("Should you trust DES? Yea/Nay"))
  print(solve("What was the result of the attempt to make DES more secure so that it could be used for longer?"))
  print(solve("Is it ok to share your public key? Yea/Nay"))
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
