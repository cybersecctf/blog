def vigenere_decrypt_custom(ciphertext, key, alphabet):
    decrypted_text = ""
    key_length = len(key)
    for i in range(len(ciphertext)):
        shift = alphabet.index(key[i % key_length])
        decrypted_char = alphabet[(alphabet.index(ciphertext[i]) - shift) % len(alphabet)]
        decrypted_text += decrypted_char
    return decrypted_text
ciphertext = "UFJKXQZQUNB"
key = "SOLVECRYPTO"
custom_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

decrypted_text = vigenere_decrypt_custom(ciphertext, key, custom_alphabet)
print("Decrypted text:", decrypted_text)
