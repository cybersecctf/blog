
#python
import sys,base64,binascii
from pyzbar.pyzbar import decode
from PIL import Image
import codecs

decodes="text"
text =" VGhlIFZlbm9uYSBwcm9qZWN0IHdhcyBhIFVuaXRlZCBTdGF0ZXMgY291bnRlcmludGVsbGlnZW5jZSBwcm9ncmFtIGluaXRpYXRlZCBkdXJpbmcgV29ybGQgV2FyIElJLg=="
type="decodes"
if len(sys.argv)>1:
     type=sys.argv[1]
else:
      print("usage -v decodes/encode text [text[default] hex base64]")
if len(sys.argv)>2:
    text=sys.argv[2]
if len(sys.argv)>3:
    decodes=sys.argv[3]       
try:

 
 
 if type=="encode":
  sample_string_bytes = text.encode("ascii") 
  base64_bytes = base64.b64encode(sample_string_bytes) 
  if decodes=="hex":
     print(binascii.hexlify(base64_bytes))
  elif  decodes=="rot13":
      print(codecs.encode(text, 'rot_13'))
  else:  
   print( base64_bytes.encode("ascii") )
 
 elif type=="decode":
   base64_bytes = text.encode("ascii") 
   if decodes=="hex":
     print(binascii.hexlify(base64_bytes))
   elif  decodes=="rot13":
      print(codecs.decode(text, 'rot_13'))
   else: 
    print(base64.b64decode(base64_bytes) )
 else:
  # Load the image from a file
  img = Image.open('qrcode.png')
  # Decode the QR code 
  decodesd_objects = decode(img)
  # Print the result
  for obj in decodesd_objects:
    print('Type: ', obj.type)
    print('Data: ', obj.data.decode('utf-8'))
except Exception as   e:
  print("error:"+str(e))

