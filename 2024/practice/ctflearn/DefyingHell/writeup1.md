<!DOCTYPE html>
<html>
 
<body>
    <h1>ctflearn---Defying Hell
  Writeup </h1>

    <h2>Challenge Description</h2>
    <p> Alice has been sharing secret encrypted messages with Bob. I would really like to know what those are...

I contacted my good friend Eve, a well-known eavesdropper. She sent me the numbers she found at the beginning of their conversation. By the look of things, this looks like a key exchange. If we would find the key, we would be able to decode every message they encrypted with it!

Help me find both private keys. To submit the flag, decode them correctly and wrap them into CTFlearn{<Alice>_<Bob>} format.

Hint: the title of this challenge is a pun... I can't tell you more ;)
<a href="https://cybersecctf.github.io/blog/2024/practice/ctflearn/DefyingHell/data.txt">data.txt</a>
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>we open data.txt and and see pg a ,b and on base of quetion can guess that 
is a  <a href="https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange">Diffie–Hellman key exchange</a> quetion with two key a b and
with run code can getg flag 

<pre>
import blog

import math;
from sympy.ntheory.residue_ntheory import discrete_log

def solve(p,g,A,B):
 
 x = discrete_log(p, A, 2)
 y = discrete_log(p, B, 2)

 if (pow(2,x,p) == A):
    a = x

 if (pow(2,y,p) == B):
    
    b = y
 k_a = pow(B,a,p)
 k_b = pow(A,b,p)
 k = k_a # Note that k = k_a = k_b

 a=bytes.fromhex(hex(a)[2:])
 b=bytes.fromhex(hex(b)[2:])
 return a,b
if __name__ == "__main__" :
 p =blog.set( 2468642135797531,1)
 g = blog.set(2,2)
 A =blog.set( 679217732839784,3)# A = g^{a} mod p where a is the secret integer of Alice
 B =blog.set( 1255037608816496,4) # B = g^{b} mod p where b is the secret integer of Bob
 print(solve(p,g,A,B))
</pre>
flag is combination of two key a,b with _
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlearn{H3ll0_Fr13nd}
</p>

    <h2>Conclusion</h2>
    <p>this is a medium  for Diffie–Hellman key exchange</p>

</body>
</html>
