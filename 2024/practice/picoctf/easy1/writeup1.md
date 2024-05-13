
<!DOCTYPE html>
<html>

<body>
    <h1>Easy1- picoctf2021</h1>

    <h2>Challenge Description</h2>
    <p>AUTHOR: ALEX FULTON/DANNY

Description
The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this table to solve it?.
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
we can use any online too like this:https://www.dcode.fr/vigenere-cipher or 
use this python code
  <pre>
import sys
def vigenere_decrypt_custom(ciphertext, key, alphabet):
    decrypted_text = ""
    key_length = len(key)
    for i in range(len(ciphertext)):
        shift = alphabet.index(key[i % key_length])
        decrypted_char = alphabet[(alphabet.index(ciphertext[i]) - shift) % len(alphabet)]
        decrypted_text += decrypted_char
    return decrypted_text

ciphertext = "UFJKXQZQUNB"
if len(sys.argv)>1:
  ciphertext=sys.argv[1]
key = "SOLVECRYPTO"
if len(sys.argv)>2:
  ciphertext=sys.argv[2]
custom_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if len(sys.argv)>3:
  custom_alphabet=sys.argv[3]
decrypted_text = vigenere_decrypt_custom(ciphertext, key, custom_alphabet)
print("Decrypted text:", decrypted_text)
</pre>
and get flag and wrap it with picoCTF{} for have correct flag
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">flag{CRYPTOISFUN}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for   crypt and vigener chipher with key</p>
</body>
</html>

