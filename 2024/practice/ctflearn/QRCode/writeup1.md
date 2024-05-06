<!DOCTYPE html>
<html>

<body>
    <h1>QR Code- ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> Do you remember something known as QR Code? Simple. Here for you : <br /> https://mega.nz/#!eGYlFa5Z!8mbiqg3kosk93qJCP-DBxIilHH2rf7iIVY-kpwyrx-0
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
we download image 
<img src=" https://cybersecctf.github.io/blog/2024/practice/ctflearn/QRCode/qrcode.png" alt="ctf quetion image" class="inline"/>
that is a qrcode
get text from qrcode that is base64 and convert it to text that is rot13 and get flag
with this code 
<pre>
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

</pre>
    and parameters<pre> qr qrcode.png</pre> get text that is base64 with parameters<pre> decode base64text base64</pre> 
and finally with <pre> decode rot13text rot13</pre> decoded from rto13 and convert to flag.with this harder can use for all qrcodes  and values or use 
easy online tools
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlearn{n0_body_f0rget_qr_code}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on qrcodes and convert types and crypto</p>
</body>
</html>


