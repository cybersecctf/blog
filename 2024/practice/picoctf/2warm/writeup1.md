
<!DOCTYPE html>
<html>

   <title>picoctf 2019-  2Warm</title>   

<body>
    <h1>picoctf 2019-  2Warm</h1>

    <h2>Challenge Description</h2>
    <p>AUTHOR: SANJAY C/DANNY TUNITIS

Description
Can you convert the number 42 (base 10) to binary (base 2)?
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        <li> you can get it manual but for all numbers use online or python code
<pre>
def solve(ch):
  return bin(ch)
if __name__ == "__main__" :
 print(solve(42).replace("0b",""))
</pre>
 </li>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{101010}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for convert base 10(decimal) to base 2</p>
</body>
</html>
