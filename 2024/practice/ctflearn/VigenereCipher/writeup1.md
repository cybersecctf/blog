
<!DOCTYPE html>
<html>

<body>
    <h1>Vigenere Cipher- ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> The vignere cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers based on the letters of a keyword.<br />

I’m not sure what this means, but it was left lying around: blorpy

gwox{RgqssihYspOntqpxs}
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        this is Vigenere Cipher with key can use any online tool like <a href="https://gchq.github.io/CyberChef/>CyberChef</a>
        or code from this <a href="https://cybersecctf.github.io/blog/2024/practice/cryptoctf1/crypto-acting-shifty/writeup1.md">writeup</a>
    and run  this code
<pre>
#python 
# -v "uiuweg{0jx_0fm_b@vj3ex3}" "utflag(if have key or chipher)" "uiuweg plaintext if not key"
import blog
def find_key(known_plaintext, known_ciphertext):
    key = ''
    for i in range(len(known_plaintext)):
        shift = (ord(known_ciphertext[i].lower()) - ord(known_plaintext[i].lower())) % 26
        key += chr(shift + ord('a'))  # Assuming lowercase alphabet
    return key

def solve(ciphertext, key="",knownplain="",knownchipher=""):
    if key=="":
     key = find_key(knownplain, knownchipher)
    plaintext = ''
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - ord('a')
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            plaintext += decrypted_char
            key_index += 1
        else:
            plaintext += char
    return plaintext
print("usage $hack chipher -v   fullcipher   knowplain( or key)    knowncipher ") 
cipher=blog.set("gwox{RgqssihYspOntqpxs}",1)
knownplain=blog.set("",2)
knownchipher=blog.set("",3)

decrypted_text = solve(cipher, "blorpy",knownplain,knownchipher)
print("Decrypted message:", decrypted_text)

</pre>
with parmeters <pre>-v gwox{RgqssihYspOntqpxs} blorpy</pre>
and get flag
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">flag{CiphersAreAwesome}

</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for vigener chipher with key and crypto</p>
</body>
</html>



