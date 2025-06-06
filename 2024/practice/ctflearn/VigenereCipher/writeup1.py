
#python 
# -v "uiuweg{0jx_0fm_b@vj3ex3}" "utflag(if have key or chipher)" "uiuweg plaintext if not key"
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
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

