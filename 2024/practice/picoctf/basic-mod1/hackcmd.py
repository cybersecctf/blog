
def modInverse(A, M):
 
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1
import sys
s="432 331 192 108 180 50 231 188 105 51 364 168 344 195 297 342 292 198 448 62 236 342 63"
if len(sys.argv)>1:
   s=sys.argv[1]

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
modn=len(alphabet)
 
if len(sys.argv)>2:
  alphabet=sys.argv[2]
if len(sys.argv)>3:
  modn=int(sys.argv[3])
modn=41
f=""
for x in s.split():
    s=int(x)%modn
    s= modInverse(s,41)
    f+=alphabet[s-1]
print(f)