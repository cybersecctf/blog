
<!DOCTYPE html>
<html>

<body>
    <h1>ctf event- challengename Challenge Writeup(first save it)</h1>

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
import sys,base64
try:
 type="decode"
 text =" VGhlIFZlbm9uYSBwcm9qZWN0IHdhcyBhIFVuaXRlZCBTdGF0ZXMgY291bnRlcmludGVsbGlnZW5jZSBwcm9ncmFtIGluaXRpYXRlZCBkdXJpbmcgV29ybGQgV2FyIElJLg=="
 if len(sys.argv)>1:
     type=sys.argv[1]
 else:
      print("usage -v decode/encode text")
 if len(sys.argv)>2:
    text=sys.argv[2]
 if type=="encode":
  print("encoede base64:",base64_string.encode(text) )
 else:
   print("decoded base64:",base64.b64decode(base64_bytes) )
 
except Exception as   e:
 print("error:"+str(e)) 
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



