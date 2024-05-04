
<!DOCTYPE html>
<html>

<body>
    <h1>Base 2 2 the 6- ctflearn</h1>
    <h2>Challenge Description</h2>
    <p> There are so many different ways of encoding and decoding information nowadays... One of them will work! Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
we first convert to base 2 or 6 and not work.see describe maybe 2 2 and 6 means base64?so  we   code in this  <a href="https://cybersecctf.github.io/blog/2024/googlectf/beginners-quest/0000/0/writeup1.md">writeup</a> for convert from base 64
<pre>
#python
import sys,base64,binascii
codecs="text"
text =" VGhlIFZlbm9uYSBwcm9qZWN0IHdhcyBhIFVuaXRlZCBTdGF0ZXMgY291bnRlcmludGVsbGlnZW5jZSBwcm9ncmFtIGluaXRpYXRlZCBkdXJpbmcgV29ybGQgV2FyIElJLg=="
type="decode"
if len(sys.argv)>1:
     type=sys.argv[1]
else:
      print("usage -v decode/encode text [text[default] hex base64]")
if len(sys.argv)>2:
    text=sys.argv[2]
if len(sys.argv)>3:
    codecs=sys.argv[3]       
try:

 
 
 if type=="encode":
  sample_string_bytes = text.encode("ascii") 
  base64_bytes = base64.b64encode(sample_string_bytes) 
  if codecs=="hex":
     print(binascii.hexlify(base64_bytes))
  else:  
   print( "encoded in base64:",base64_bytes.decode("ascii") )
 
 else:
   base64_bytes = text.encode("ascii") 
   if codecs=="hex":
     print(binascii.hexlify(base64_bytes))
   else: 
    print("decoded from base64:",base64.b64decode(base64_bytes) )
 
except Exception as   e:
 print("error:"+str(e)) 
</pre>
and after run it with parameters <pre>decode Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9</pre>    will get flag   
 also can use online base convertor like   <a href="https://gchq.github.io/CyberChef/">CyberChef</a> for convert any base
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTF{FlaggyWaggyRaggy}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for  </p>
</body>
</html>



