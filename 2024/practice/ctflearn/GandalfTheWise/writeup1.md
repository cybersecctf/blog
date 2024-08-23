<title>GandalfTheWise-ctflearn</title>

<!DOCTYPE html>
<html>

<body>
    <h1>GandalfTheWise-ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> Extract the flag from the Gandalf.jpg file. You may need to write a quick script to solve this.
<a href="https://ctflearn.com/challenge/download/936">Gandalg.jpg</a>

 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
we download image<img src=" https://cybersecctf.github.io/blog/2024/practice/ctflearn/GandalfTheWise/gandalf.jpg" alt="ctf quetion image" class="inline"/> nothing in image for flag so use exiftool 
see <code>Q1RGbGVhcm57eG9yX2lzX3lvdXJfZnJpZW5kfQo= decoded to CTFlearn{xor_is_your_friend} </code>      
    that was fake flag so search harder in strings find
<code>
JFIF
+Q1RGbGVhcm57eG9yX2lzX3lvdXJfZnJpZW5kfQo=
+xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p
+h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU
</code>
first flag mention xor so if xor two of   them in  script can get use this script
<pre>
import base64,sys
a = "xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p"
if len(sys.argv)>1:
 a=sys.argv[1]
else:
 print("usage -v string1(xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p) string2(h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU)")
A = base64.b64decode(a)
b = "h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU"
if len(sys.argv)>2:
 b=sys.argv[2]
B = base64.b64decode(b)
c = []
l = len(A)
i = 0
while i < l:
  c.append(chr(A[i] ^ B[i]))
  i += 1
print("".join(c))
</pre>
and get our flag
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlearn{Gandalf.BilboBaggins}
</p>

    <h2>Conclusion</h2>
    <p>this is a    easy chanllenge for xor of two string</p>
</body>
</html>



 