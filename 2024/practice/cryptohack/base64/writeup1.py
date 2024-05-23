import base64,sys
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
def run(hex_string,type="base64"):
 bytes_value = bytes.fromhex(hex_string)
 encodings = ['utf-8', 'latin1', 'ascii', 'cp1252']
 if type!="base64":
  for encoding in encodings:
    try:
        ascii_value = bytes_value.decode(encoding)
        print(f"The decoded string in {encoding} is: {ascii_value}")
    except UnicodeDecodeError:
        print(f"Unable to decode the string using {encoding}")
 else:
   print(base64.b64encode(bytes_value))
print("-v vlaue base64/ascii")
type="base64"
hex_string=blog.set("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf",1)
type=blog.set("base64",1)
run(hex_string,type)