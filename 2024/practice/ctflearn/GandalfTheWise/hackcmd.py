import base64,sys

a = "xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p"
if len(sys.argv)>1:
 a=sys.argv[1]
else:
 print("usage -v string1(xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p) string2(h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU)")
A = base64.b64decode(a)
b = "h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU"
if len(sys.argv)>2:
 b=sys.argv[2]
B = base64.b64decode(b)
c = []
l = len(A)
i = 0
while i < l:
  c.append(chr(A[i] ^ B[i]))
  i += 1
print("".join(c))
