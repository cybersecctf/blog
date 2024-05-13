#!/usr/bin/python3 -u
import os.path

KEY_FILE = "key"
KEY_LEN = 50000
FLAG_FILE = "flag"

def encrypt(key_location):
    ui = input("What data would you like to encrypt? ").rstrip()
    if len(ui) == 0 or len(ui) > KEY_LEN:
        return -1

    start = key_location
    stop = key_location + len(ui)

    kf = open(KEY_FILE, "rb").read()

    if stop >= KEY_LEN:
        stop = stop % KEY_LEN
        key = kf[start:] + kf[:stop]
    else:
        key = kf[start:stop]
    key_location = stop

    result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), ui, key))
    encrypted_result = "".join(result)

    print("Here ya go!\n{}\n".format(encrypted_result))

    # Decrypt the input and print it
    decrypted_result = "".join(chr(int(hex_str, 16) ^ key[i]) for i, hex_str in enumerate(result))
    print("Decrypted input: {}\n".format(decrypted_result))

    return key_location
def startup(key_location):
    ui = input("What data would you like to encrypt? ").rstrip()
    if len(ui) == 0 or len(ui) > KEY_LEN:
        return -1

    start = key_location
    stop = key_location + len(ui)

    kf = open(KEY_FILE, "rb").read()

    if stop >= KEY_LEN:
        stop = stop % KEY_LEN
        key = kf[start:] + kf[:stop]
    else:
        key = kf[start:stop]
    key_location = stop

    result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), ui, key))
    encrypted_result = "".join(result)

    print("Here ya go!\n{}\n".format(encrypted_result))

    # Decrypt the input and print it
    decrypted_result = "".join(chr(int(hex_str, 16) ^ key[i]) for i, hex_str in       enumerate(result))
    print("Decrypted input: {}\n".format(decrypted_result))

    return key_location
  

print("******************Welcome to our OTP implementation!******************")
c = startup(0)
while c >= 0:
    c = encrypt(c)
