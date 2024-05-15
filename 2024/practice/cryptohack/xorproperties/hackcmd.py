from pwn import *
import sys
# needed for the xor()

type="hex"
a="a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
b="37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
if len(sys.argv)>1:
  a=sys.argv[1]
if len(sys.argv)>2:
  b=sys.argv[2]
if len(sys.argv)>3:
  type=sys.argv[3]
a = bytes.fromhex(a)
b = bytes.fromhex(b)
s=xor(a, b)
if type=="hex":
 print(s.hex())
else:
  print(s.decode())           