<title>WebDecode-picoctf2024</title>

<!DOCTYPE html>
<html>

<body>
    <h1>WebDecode-picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p> Do you know how to use the web inspector?
Additional details will be available after launching your challenge instance.
Start searching here to find the flag <a href="http://titan.picoctf.net:55220/">here</a>
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
we going to about page 
<pre>
import base64
import blog
def solve(operation,a): 
 try:
  if operation=="decode":
    return base64.b64decode(a)
  else:
    return base64.b64encode(a)
 except Exception as e:
  return f"not a base64 nymber {str(e)}"
if __name__ == "__main__" :
  a=blog.set("cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMWY4MzI2MTV9",1)
  print(solve("decode",a)) 
</pre>
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">flag{}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on develper tools in in chrome and web exploitations</p>
</body>
</html>


