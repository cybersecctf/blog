
import hashlib
import json
from math import gcd
from random import randint
from pwn import *
# Assuming the values of n0 and c0 are given or read from param.py
n0 = 0  # Replace with actual n0 value from param.py
c0 = 0  # Replace with actual c0 value from param.py

def hash(s):
    m = b''
    for si in s:
        sib = int.to_bytes(si, (int(si).bit_length() + 7) // 8, 'big')
        sil = int.to_bytes(len(sib), 2, 'big')
        m += sil
        m += sib
    return hashlib.md5(m).digest()
def verify(n, c, proof):
    s = proof.get('s')
    z = proof.get('z')
    h = int.from_bytes(hash(s), 'big')
    b = [(h>>i)&1 for i in range(127, -1, -1)]
    if len(s) != 128: return False
    if len(z) != 128: return False
    if len(b) != 128: return False

    for si, zi, bi in zip(s, z, b):
        if gcd(si, n) != 1: return False
        if pow(zi, 2, n) != si * pow(c, bi, n) % n: return False
    return True
def generate_proof(n, c):
    s = []
    z = []

    for _ in range(128):
        while True:
            si = randint(2, n - 1)
            if gcd(si, n) == 1:
                break
        zi = pow(si, (n + 1) // 4, n)  # This is a guess based on Rabin cryptosystem properties
        s.append(si)
        z.append(zi)

    proof = {'n': n, 'c': c, 's': s, 'z': z}
    return proof

def hash(s):
    m = b''
    for si in s:
        sib = int.to_bytes(si, (int(si).bit_length() + 7) // 8, 'big')
        sil = int.to_bytes(len(sib), 2, 'big')
        m += sil
        m += sib
    return hashlib.md5(m).digest()

def generate_proof(n, c):
    # Set si to 0
    si = 0
    # Choose any valid zi (e.g., gcd(zi, n) = 1)
    zi = 1
    s = [si] * 128
    z = [zi] * 128

    proof = {'n': n, 'c': c, 's': s, 'z': z}
    return proof

def main():
    # Server address and port
    address = 'zkpok.2024.ctfcompetition.com'
    port = 1337

    # Generate the proof
    proof = generate_proof(n0, c0)

    # Send the proof to the server
    send_proof(proof, address, port)

if __name__ == '__main__':
    main()