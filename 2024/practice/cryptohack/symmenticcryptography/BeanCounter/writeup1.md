<title>Bean Counter- cryptohack</title>


<html>

<body>
    <h1>Bean Counter- cryptohack</h1>

    <h2>Challenge Description</h2>
    <p>I've struggled to get PyCrypto's counter mode doing what I want, so I've turned ECB mode into CTR myself. My counter can go both upwards and downwards to throw off cryptanalysts! There's no chance they'll be able to read my picture..

Play at <a href="https://aes.cryptohack.org/bean_counter"> https://aes.cryptohack.org/bean_counter</a>
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
For this challenge we have been given encrypt and encrypt_flag function both of which uses OFB(Output feedback) mode of encryption. The first 32 bytes of the return of encrypt_flag is IV(initialisation vector). The encrypt function take the plaintext and gives the ciphertext. As one can see let k = AES(KEY) then ciphertext = plaintext ^ k. So we can say that plaintext = ciphertext ^ k. So we can get the key by XORing the first 16 bytes of the return of encrypt_flag with the ciphertext by providing the ciphertext as the plaintext to the encrypt function.
<pre>
import blog
#python
enc=blog.solveup("strings files","enc")
png_hdr = bytes([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a, 0x00, 0x00, 0x00, 0x0d, 0x49, 0x48, 0x44, 0x52])
encrypted = bytes.fromhex(enc)

keystream = []
for i in range(len(png_hdr)):
    keystream.append(png_hdr[i] ^ encrypted[i])

print(keystream)

png = [0]*len(encrypted)
for i in range(len(encrypted)):
    png[i] = encrypted[i] ^ keystream[i%len(keystream)]

with open('bean_counter.png', 'wb') as fd:
    fd.write(bytes(png))
</pre>        

       it create image that have flag
     <img src=" https://cybersecctf.github.io/blog/2024/practice/cryptohack/symmenticcryptography/BeanCounter/bean_counter.png" alt="ctf quetion image" class="inline"/>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">crypto{hex_bytes_beans}
</p>
    <h2>Conclusion</h2>
    <p>this is a medium challenge for  decrypt hex into png with aes and xored png headers</p>
</body>
</html>



