
<!DOCTYPE html>
<html>

<body>
    <h1>ctf event- challengename Challenge Writeup(first save it)</h1>

    <h2>Challenge Description</h2>
    <p>  
Phew, that was close... but you decrypted that one and  escaped the ambush in time! Sidney Rilley, you've done it again. They almost got lucky this one time. The  nemy continues to use unbreakable encryption. Hopefully, they made at least one mistake and you'll be able t o find and exploit it. If they keep reusing the cipher , just like they repeatedly use your name, maybe we can eventually find a way to defeat it. Login to your terminal (your password is 'Sidney'). Maybe you can decr ypt at least one of the messages. Connect with the command: "socat file:`tty`,rawer tcp:otp1.2023-bq.ctfcompetition.com:1337".Ah, and by the way, our crypto experts said to try crib dragging but we couldn't find any infants around.HINT: "multi-time pad" is a decent crib. The enemy thinks that the multi-time pad can't be broken.
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
  sample_string_bytes = text.encode("ascii") 
  base64_bytes = base64.b64encode(sample_string_bytes) 
  print( "encoded in base64:",base64_bytes.decode("ascii") )
 else:
   base64_bytes = text.encode("ascii") 
   print("decoded from base64:",base64.b64decode(base64_bytes) )
 
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



