#python
import ast
import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

if len(sys.argv)>1:
  ords=sys.argv[1]
  if ords.startswith("[") and ords.endswith("]") and "," in ords:
   ords= ast.literal_eval(ords)
  else:
    d=[]
    for x in ords:
      d.append(ord(x))
    ords=d

else:
  ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

hexs="0x32" 
type="int"
if len(sys.argv)>2:
  hexs=sys.argv[2]
if len(sys.argv)>3:
  type=sys.argv[3]
print(ords)
for x in ords:
  print(x)
print("Here is your flag:")
if type=="int":
   hexs=hex(int(hexs))
hexs = int(hexs, 16)
print("".join(chr(o ^ hexs) for o in ords))
