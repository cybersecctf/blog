 

<!DOCTYPE html>
<html>
 <title>try hack me---Crucial Crypto Maths  Writeup </title>
<body>
    <h1>try hack me---Crucial Crypto Maths  Writeup </h1>

    <h2>Challenge Description</h2>
    <p> There's a little bit of math(s) that comes up relatively often in cryptography. The Modulo operator. Pretty much every programming language implements this operator, or has it available through a library. When you need to work with large numbers, use a programming language. Python is good for this as integers are unlimited in size, and you can easily get an interpreter.

When learning division for the first time, you were probably taught to use remainders in your answer. X % Y is the remainder when X is divided by Y.

Examples
25 % 5 = 0 (5*5 = 25 so it divides exactly with no remainder)

23 % 6 = 5 (23 does not divide evenly by 6, there would be a remainder of 5)

An important thing to remember about modulo is that it’s not reversible. If I gave you an equation: x % 5 = 4,
 there are infinite values of x that will be valid.
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>this is a find mod problem

<pre>
import blog

import os,subprocess
def solve(a, b):
   return a%b

if __name__ == "__main__" :
 print(solve(30,5))
 print(solve(25,7))
 print(solve(118613842,9091))
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">0 4 3565
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on mod</p>

</body>
</html>
