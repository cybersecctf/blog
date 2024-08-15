
<!DOCTYPE html>
<html>
 
<body>
    <h1>tryhackme encryption101---PGP, GPG and AES Writeup </h1>

    <h2>Challenge Description</h2>
    <p> at is PGP?
PGP stands for Pretty Good Privacy. It’s a software that implements encryption for encrypting files, performing digital signing and more.

What is GPG?
GnuPG or GPG is an Open Source implementation of PGP from the GNU project. You may need to use GPG to decrypt files in CTFs. With PGP/GPG, private keys can be protected with passphrases in a similar way to SSH private keys. If the key is passphrase protected, you can attempt to crack this passphrase using John The Ripper and gpg2john. The key provided in this task is not protected with a passphrase.

The man page for GPG can be found online here.

What about AES?
AES, sometimes called Rijndael after its creators, stands for Advanced Encryption Standard. It was a replacement for DES which had short keys and other cryptographic flaws.

AES and DES both operate on blocks of data (a block is a fixed size series of bits).

AES is complicated to explain, and doesn’t seem to come up as often. If you’d like to learn how it works, here’s an excellent video from Computerphile https://www.youtube.com/watch?v=O4xNJsjtN6E

Answer the questions below
Time to try some GPG. Download the archive attached and extract it somewhere sensible.
No answer needed
Complete
You have the private key, and a file encrypted with the public key. Decrypt the file. What's the secret word?
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>after understand all conectpt and check complete for find password of <a href="https://cybersecctf.github.io/blog/2024/practice/tryhackme/Encryption-Crypto101/PGP-GPG-and-AES/gpg_1593559828557.zip">attached file</a> use this code
and get password  that is Pineapple.
<pre>
import blog

import os,subprocess
def solve(file,key ):
 blog.solveup("garden","unzip gpg_1593559828557.zip","$run")  
 blog.solveup("garden","gpg --import {key}","$run")
 blog.solveup("garden",f"gpgp {file}","$run")
 s=blog.solveup("garden","cat message","$run")
 return s
if __name__ == "__main__" :
  print(solve("message.gpg","tryhackme.key"))
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">Pineapple.
</p>

    <h2>Conclusion</h2>
    <p>this is a medium chanllenge for understand gpg and aes apgp conecept and find passweeord of gpg file with key</p>

</body>
</html>
