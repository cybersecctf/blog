import binascii as bs
text='12'.encode()
print(bs.hexlify(bytes(text)))