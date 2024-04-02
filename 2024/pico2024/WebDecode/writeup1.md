
<!DOCTYPE html>
<html>

<body>
    <h1>WebDecode- picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: NANA AMA ATOMBO-SACKEY

Description
Do you know how to use the web inspector?
Start searching <a href="http://titan.picoctf.net:54494/">here</a> to find the flag
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
 open website and search for flag with inspector        
    in about page .i get    base64 text inside it with this command convert it to text and get flag
<pre>
#python
import base64,sys
try:
 a="cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMWY4MzI2MTV9"
 if len(sys.argv)>1:
  a = sys.argv[1]
 print(base64.b64decode(a))
except:
 print("not a base 64 nymber")
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{web_succ3ssfully_d3c0ded_1f832615}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for  search in site pages with inspect and convert base64 to text</p>
</body>
</html>


