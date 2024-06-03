
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
and get flag
<pre>
#python 
# -v "uiuweg{0jx_0fm_b@vj3ex3}" "utflag" "uiuweg"
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
import blog
print("usage $hack chipher -v   fullcipher   knowplain( or key)    knowncipher ") 
def  solve(cipher,key="",knownplain="",knownchipher=""):
 if key=="":
  key = find_key(knownplain, knownchipher)
 
 decrypted_text = vigenere_decrypt(cipher, key)
 return "Decrypted message:"+decrypted_text+"\nkey:"+key
if __name__ == "__main__" :
 cipher=blog.set("uiuweg{0jx_0fm_b@vj3ex3}",1)
 knownplain=blog.set("utflag",2)
 knownchipher=blog.set("uiuweg",3)
 key=blog.set("",1)
 print(solve(cipher,key,knownplain,knownchipher))
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


