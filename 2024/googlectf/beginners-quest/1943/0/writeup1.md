
<!DOCTYPE html>
<html>

<body>
    <h1>google ctf begginer quest-  1943 -0</h1>

    <h2>Challenge Description</h2>
    <p> We captured enemy spy and intercepted a message 
According to our cryptanalysts, it's encrypted with
 an unbreakable cipher. Fortunately, the spy lacks
key management skills and carried this key: "VGhlIFZlbm9uYSBwcm9qZWN0IHdhcyBhIFVuaXRlZCBTdGF0ZXMgY291bnRlcmludGVsbGlnZW5jZSBwcm9ncmFtIGluaXRpYXRlZCBkdXJpbmcgV29ybGQgV2FyIElJLg=="

</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        decode base 64 with this script
<pre>
#python
import sys,base64,binascii
import blog
def solve(type,text,codecs):
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
codecs="text"
type=blog.set("decode",1,"str","usage -v decode/encode text [text[default] hex base64]")
text=blog.set("VGhlIFZlbm9uYSBwcm9qZWN0IHdhcyBhIFVuaXRlZCBTdGF0ZXMgY291bnRlcmludGVsbGlnZW5jZSBwcm9ncmFtIGluaXRpYXRlZCBkdXJpbmcgV29ybGQgV2FyIElJLg==",2)
codecs=blog.set("text",3)
solve(type,text,codecs)
 
 
 

</pre>
       and get this message
<pre>
    The Venona project was a United States counterintelligence program initiated during World War II.
</pre>
challenge say it is key for message 
so connect socat with this command
<pre>
socat file:`tty`,rawer tcp:otp1.2023-bq.ctfcompetition.com:1337
</pre>
 and enter password Sidney as secret provided in desription
see  start  <img src=" https://cybersecctf.github.io/blog/2024/googlectf/beginners-quest/1943/1/start0.png" alt="ctf quetion image" class="inline"/>
going spamis encrypted when pass  key that is
<pre>
    The Venona project was a United States counterintelligence program initiated during World War II.
</pre>
and press enter show this message
 <img src=" https://cybersecctf.github.io/blog/2024/googlectf/beginners-quest/1943/1/flag0.png" alt="flag" class="inline"/>
that is our flag
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTF{Ace_of_Spies} 
</p>

    <h2>Conclusion</h2>
    <p>this is a     easy chanllenge for  connect socat and base64 decode</p>
</body>
</html>



