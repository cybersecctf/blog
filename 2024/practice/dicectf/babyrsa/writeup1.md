
<!DOCTYPE html>
<html>

<body>
    <h1>baby-rsa- dicectf2022</h1>

    <h2>Challenge Description</h2>
    <p> I messed up prime generation, and now my private key doesn't work!
<a href="https://phantom1ss.github.io/blog/2024/practice/dicectf/babyrsa/output.txt">output.txt</a>

 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
      we open output.txt file this is a rsa can be rooted on factorb and use this crypt in saga for get flag
<pre>
#sage
from sage.all_cmdline import *   # import sage library

from Crypto.Util.number import long_to_bytes
p, q = int(input("input p get p,q from factordb")), int(input("input q"))
N = int(input("input n"))
e = int(input("input e"))
cipher = int(input("input c"))
# factor with cado-nfs


assert p * q == N

p_roots = mod(cipher, p).nth_root(e, all=True)
q_roots = mod(cipher, q).nth_root(e, all=True)

for xp in p_roots:
    for xq in q_roots:
        x = crt([Integer(xp), Integer(xq)], [p,q])
        x = int(x)
        flag = long_to_bytes(x)
        if flag.startswith(b"dice"):
            print(flag.decode())

</pre>
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">dice{cado-and-sage-say-hello}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for rsa with rooted n </p>
</body>
</html>


 
