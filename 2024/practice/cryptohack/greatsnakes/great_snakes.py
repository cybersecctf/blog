#!/usr/bin/env python3
import ast
import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

if len(sys.argv)>1:
  ords=sys.argv[1]
  ords= ast.literal_eval(ords)

else:
  ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]
hexs="0x32" 
if len(sys.argv)>2:
  hexs=sys.argv[2]
print(ords)
for x in ords:
  print(x)
print("Here is your flag:")

hexs = int(hexs, 16)
print("".join(chr(o ^ hexs) for o in ords))
