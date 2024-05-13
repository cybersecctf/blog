from pwn import *

import string
import base64
import itertools

ciphers = [
    "bWqznPKmVMkt0Obu8bAINKvcBYpurA2yC0NKkUTXWw24Y8AtW9eK9+zipS2Cs6qBHDF7Jpn4z2jm2iT/RWXw6QbQgNb2Ty64i5IuVZxpHsZ6GGr860eM7g==",
    "dmrn1eTjXYw8y+bIx4V4buP0UcJ8qhG+X3hGnFiSTFiJZskgTI7Tssv9uDeE/b+QGjVsZdX63X28k0rfanPYvBrFjaL2UWucmIMLX+lyEtZtHGD26EmF9g==",
    "amqiy6HpTN5ox6/fypQqaavmRIRq+0jGF05W2FWWW1+vL84iRoDd5uXzvmOG9v6RDDw1JID73Hjljg7GZj7N/Q6KycvxAjuJmJ8TRbxrHcYzWVL07UWM6g==",
    "A7K+WILzJAdYo41+QSfb/Ud6MvX+cIopvwYoAcP5V3Y+6g2vYtZdzlulJPc1jvu1uDIgz1hjbLxAz6ya6zzIR7zc8Q9xeqJid/8KOg7HPhD/QI7Ohyj4Sg=="
]

crib = b"multi-time pad"

for i, j in itertools.combinations(range(len(ciphers)), 2):
    log.info(f"XORing {i} and {j}")
    xored = xor(base64.b64decode(ciphers[i]), base64.b64decode(ciphers[j]))
    for offset in range(len(xored) - len(crib) + 1):
        output = xor(xored[offset:offset+len(crib)], crib)
        if all(chr(c) in string.printable for c in output):
            log.info(f"Found readable string at offset {offset}: {output}")
