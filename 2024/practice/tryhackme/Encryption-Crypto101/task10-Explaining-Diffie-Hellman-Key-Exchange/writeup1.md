 

<!DOCTYPE html>
<html>
 
<body>
    <h1>tryhackme--task10-Explaining Diffie Hellman Key Exchange  Writeup </h1>

    <h2>Challenge Description</h2>
    <p>  What is Key Exchange?
Key exchange allows 2 people/parties to establish a set of common cryptographic keys without an observer being able to get these keys. Generally, to establish common symmetric keys.

How does Diffie Hellman Key Exchange work?
Alice and Bob want to talk securely. They want to establish a common key, so they can use symmetric cryptography, but they don’t want to use key exchange with asymmetric cryptography. This is where DH Key Exchange comes in.

Alice and Bob both have secrets that they generate, let’s call these A and B. They also have some common material that’s public, let’s call this C.

We need to make some assumptions. Firstly, whenever we combine secrets/material it’s impossible or very very difficult to separate. Secondly, the order that they're combined in doesn’t matter.

Alice and Bob will combine their secrets with the common material, and form AC and BC. They will then send these to each other, and combine that with their secrets to form two identical keys, both ABC. Now they can use this key to communicate.

Extra Resources
An excellent video if you want a visual explanation is available here. https://www.youtube.com/watch?v=NmM9HA2MQGI

DH Key Exchange is often used alongside RSA public key cryptography, to prove the identity of the person you’re talking to with digital signing. This prevents someone from attacking the connection with a man-in-the-middle attack by pretending to be Bob.

Answer the questions below
I understand how Diffie Hellman Key Exchange works at a basic level
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>
for complete task just read info carefolly and then click correct answer for understand
this task i ad this code extra like previous tasks
<pre>
import blog
import random

import os,subprocess
def solve(p, g):
 # Prime number and primitive root
 P = 23
 G = 5
 # Alice's private key
 a = random.randint(1, P-1)
 # Bob's private key
 b = random.randint(1, P-1)
 # Alice's public key
 A = pow(G, a, P)
 # Bob's public key
 B = pow(G, b, P)
 # Shared secret key
 shared_key_Alice = pow(B, a, P)
 shared_key_Bob = pow(A, b, P)
 return a,b,A,B,shared_key_Alice,shared_key_Bob



if __name__ == "__main__" :
  p=blog.set(23,1)
  g=blog.set(5,2)
  print(solve(p,g))
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">
</p>

    <h2>Conclusion</h2>
    <p>this is a easy chanllenge for unserstand How does Diffie Hellman Key Exchange work</p>

</body>
</html>
