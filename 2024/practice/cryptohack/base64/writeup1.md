
<!DOCTYPE html>
<html>

<body>
    <h1>Base64- cryptohack</h1>

    <h2>Challenge Description</h2>
    <p>Another common encoding scheme is Base64, which allows us to represent binary data as an ASCII string using an alphabet of 64 characters. One character of a Base64 string encodes 6 binary digits (bits), and so 4 characters of Base64 encode three 8-bit bytes.

Base64 is most commonly used online, so binary data such as images can be easily included into HTML or CSS files.

Take the below hex string, decode it into bytes and then encode it into Base64.

72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
with this code can convert hex to asci and base64 and get flag
<pre>
import base64,sys

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
import blog
 
hex_string=blog.set("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf",1)
type=blog.set("base64",2,"str")
run(hex_string,type)

</pre>
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">crypto/Base+64+Encoding+is+Web+Safe/
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for convert hex to ascii and base64</p>
</body>
</html>

