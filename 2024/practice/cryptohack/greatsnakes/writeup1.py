#python
import ast
import sys
# import this
print("custom usage -v listinstring hex")
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
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
blog.run("hex to base64","72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")