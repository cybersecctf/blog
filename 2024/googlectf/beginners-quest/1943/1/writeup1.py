
#python
from pwn import *


import string
import base64
import itertools

ciphers = [
    "0529242a631234122d2b36697f13272c207f2021283a6b0c7908",
    "2f28202a302029142c653f3c7f2a2636273e3f2d653e25217908",
    "322921780c3a235b3c2c3f207f372e21733a3a2b37263b313012",
    "2f6c363b2b312b1e64651b6537222e37377f2020242b6b2c2d5d",
    "283f652c2b31661426292b653a292c372a2f20212a316b283c09",
    "29232178373c270f682c216532263b2d3632353c2c3c2a293504",
    "613c37373531285b3c2a72273a67212a277f373a243c20203d5d",
    "243a202a633d205b3c2d3765342236653a2c7423202f3f652a18",
    "2239373d6f740a1e3c651f207f2c212a247f3d2e65262430791c",
    "263e203d63232f0f20653f207f332065262c3168313722367918",
    "2f2f372133202f142665212637222220733e383f2426386b",
]

crib = b"multi-time pad"
c=0
for i, j in itertools.combinations(range(len(ciphers)), 2):
    log.info(f"XORing {i} and {j}")
    xored = xor(ciphers[i], ciphers[j])
    base64_xored = base64.b64encode(xored).decode("utf-8")  
    if base64_xored.startswith('1b'):  
     print(c,base64_xored)
    c+=1
