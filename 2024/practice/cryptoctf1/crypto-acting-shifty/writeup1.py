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
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
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