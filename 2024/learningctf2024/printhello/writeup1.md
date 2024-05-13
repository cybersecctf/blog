
<!DOCTYPE html>
<html>

<body>
    <h1>printhello- learningctf2024</h1>

    <h2>Challenge Description</h2>
    <p> print hello!world and wraped it with flag{}
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
 run this code and get flag
<pre>
#python
import sys,string
value="hello!world"
if len(sys.argv)>1:
       value=sys.argv[1]
print(value)
</pre>
       and get flag
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">flag{value}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for  print hello!world or any input</p>
</body>
</html>

