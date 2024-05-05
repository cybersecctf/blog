#python
import sys
v1=0xc4115 
v2=0x4cf8
if len(sys.argv)>1:
 v1=sys.argv[1]
if len(sys.argv)>2:
  v2=sys.argv[2]
v3=v1^v2
v4="hex"
if len(sys.argv)>3:
  v4=sys.argv[3]
if v4!="hex":
   print(v3)
else :
   print(hex(v3))