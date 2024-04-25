<!DOCTYPE html>
<html>

<body>
    <h1>google ctf begginer quest-  1837 -1</h1>

    <h2>Challenge Description</h2>
    <p> Operator, can you decode this telegram for me? The   commander sent it from across enemy lines with my   next orders, but it doesn't seem to be using any code book I know of and certainly isn't using any  commencement word. Maybe you can figure it out?  
  HINT: Pemberton was a Confederate general who used    the Vigenère cipher


<a href="https://cybersecctf.github.io/blog/2024/googlectf/beginners-quest/1837/1/message.txt">message.txt</a>

</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
     we open message code and use normal decrypt morse code and not work so use american  morse code translator with this
<a href="https://cybersecctf.github.io/blog/2024/googlectf/beginners-quest/1837/0/writeup1.md"> python code</a>
give this text:
EOYFPIJPIYBGYNSVSDRPTMIYBJXSEC
that is not real words or answers so see hint say use vigener chipher but we don't know keys.see hints agains say:Pemberton was a Confederate general who used    the Vigenère cipher searchh via google for key with this words and find this <a href="https://cryptiana.web.fc2.com/code/civilwar4.htm">page</a> say It is well-known that the Confederates used a polyalphabetic (Vigenere) cipher during the Civil War. The present article describes its use with various keywords, including those other than the well-known three ("Manchester Bluff", "Complete Victory", "Come Retribution"). In particular, the present author recovered a keyword "Where Liberty Dwells, There Is Our Country" used between the Confederate Secretary of State and a commissioner in France. so use text 
EOYFPIJPIYBGYNSVSDRPTMIYBJXSEC with key MANCHESTERBLUFFCOMPLETEVICTORYCOMERETRIBUTION and run them with this python code or online tools and get flag.
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
after run this python will geet flag below.
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">FLAG{SOLDIERWEHAVEINTERCEPTEDTHEENE}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for decode morse code and convert text with  vigener chpher from it </p>
</body>
</html>



