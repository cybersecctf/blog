
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
    and this code
<pre>
#python 
# -v "uiuweg{0jx_0fm_b@vj3ex3}" "utflag(if have key or chipher)" "uiuweg plaintext if not key"
import sys
def find_key(known_plaintext, known_ciphertext):
    key = ''
    for i in range(len(known_plaintext)):
        shift = (ord(known_ciphertext[i].lower()) - ord(known_plaintext[i].lower())) % 26
        key += chr(shift + ord('a'))  # Assuming lowercase alphabet
    return key

def vigenere_decrypt(ciphertext, key):
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
cipher="uiuweg{0jx_0fm_b@vj3ex3}"
knownplain="utflag"
knownchipher="uiuweg"
key=""
if len(sys.argv)>1:
   cipher=sys.argv[1]
if len(sys.argv)>2:
   key=sys.argv[2]
if len(sys.argv)>3:
   knownplain=sys.argv[2]
   knownchipher= sys.argv[3]
   key=""   
known_ciphertext="uiuweg"
if key=="":
  key = find_key(knownplain, knownchipher)
  print("key is",key)
decrypted_text = vigenere_decrypt(cipher, key)
print("Decrypted message:", decrypted_text)

</pre>
with parmeters <pre>gwox{RgqssihYspOntqpxs} blorpy</pre>
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



