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
decrypted_text = vigenere_decrypt(cipher, key)
print("Decrypted message:", decrypted_text)