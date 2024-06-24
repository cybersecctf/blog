import signal
import os
import sys
from Crypto.Cipher import DES3

class Desfunctional:
    def __init__(self):
        self.key = os.urandom(24)
        self.iv = os.urandom(8)
        self.challenge = os.urandom(64)
        self.counter = 128

    def get_flag(self, plain):
        if plain == self.challenge:
            with open("flag.txt", "rb") as f:
                FLAG = f.read()
            return FLAG
        raise Exception("Not quite right")

    def get_challenge(self):
        cipher = DES3.new(self.key, mode=DES3.MODE_CBC, iv=self.iv)
        return cipher.encrypt(self.challenge)

    def decrypt_without_corruption(self, text: bytes):
        self.counter -= 1
        if self.counter < 0:
            raise Exception("Out of balance")
        cipher = DES3.new(self.key, mode=DES3.MODE_CBC, iv=self.iv)
        return cipher.decrypt(text)

if __name__ == "__main__":
    chall = Desfunctional()
    signal.alarm(128)

    try:
        # Option 1: Get challenge
        encrypted_challenge = chall.get_challenge()
        print("Challenge (hex):", encrypted_challenge.hex())

        # Option 2: Decrypt the challenge (without corruption)
        decrypted_challenge = chall.decrypt_without_corruption(encrypted_challenge)
        print("Decrypted Challenge (hex):", decrypted_challenge.hex())

        # Option 3: Get the flag
        flag = chall.get_flag(decrypted_challenge)
        print("Flag:", flag.decode())
        sys.exit(0)
    except Exception as e:
        print(e)
        sys.exit(1)
