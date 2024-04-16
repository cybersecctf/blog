
<!DOCTYPE html>
<html>

<body>
    <h1>CTF1- Acting Shifty</h1>

    <h2>Challenge Description</h2>
    <p>find hidden ttext in this <a href="https://phantom1ss.github.io/blog/2024/practice/cryptoctf1/crypto-acting-shifty/vinegar_cider.png">image</a>:

 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
         this is asample vigener chipher and we know part of plaintext start with utflag so use this code for find key and decrypt vigener chipher
<pre>
#python
import sys
print("usage $hack chipher -v knowplain(or empty)  key(or empty need key or known plain)"
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
if len(sys.argv)>1:
     knowntext=sys.argv[1]
if len(sys.argv)>2:
     knowcipher=sys.argv[2]
key=""
if len(sys.argv)>3:
   if key!="": 
     key=sys.argv[3]
   else
     key = find_key(knowntext, knowcipher)
decrypted_text = vigenere_decrypt("uiuweg{0jx_0fm_b@vj3ex3}", key)
print("Decrypted message:", decrypted_text)

</pre>
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">utflag{0ji_0qb_x@vj3pi3}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on vigener chipher and key and knowtext</p>
</body>
</html>


