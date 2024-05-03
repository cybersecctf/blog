import sys
import base64
from binascii import unhexlify
s='41424354467B34354331315F31355F55353346554C7D'
type="hex"
if len(sys.argv)>1:
 s=sys.argv[1]
if len(sys.argv)>2:
 type=sys.argv[2]

result = unhexlify(s)
if type=="base64":
 result = base64.b64encode(hex)
print(result)