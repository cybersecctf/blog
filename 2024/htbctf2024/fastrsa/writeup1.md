
<!DOCTYPE html>
<html>
     <title>htbctf2024---fastrsa
 </title>
<body>

    <h1>htbctf2024---fastrsa</h1>

    <h2>Challenge Description</h2>
    <p>Are you fast enough to solve?
 <a href="https://cybersecctf.github.io/blog/2024/htbctf2024/fastrsa/fastrsa.zip">link text</a>Are you fast enough to solve?

</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>this is reverse rsa and python code thta should get p,q ,n m,e 
via reverse in this code
<code>
#!/usr/local/bin/python
import os
import random
import gmpy2
from inputimeout import inputimeout 

FLAG = "FlagY{dummy_flag!}"

def encrypt(b, m):
    p = gmpy2.next_prime(2 ** b + random.randint(0, 2 ** b))
    q = gmpy2.next_prime(2 ** b + random.randint(0, 2 ** b))
    n = p * q
    print(n)
    print(m ** 3 % n)
    print((m + 1) ** 3 % n)

for i in range(1, 15):
    b = 30 * i
    m = random.randint(0, 4 ** b)
    encrypt(b, m)
    try:
        x = int(inputimeout("Enter Number : ",5))
        if x == m:
            print("============================\nKeep Going!\n============================")
            continue
        else:
            print("============================\nWrong Answer!\n============================")
            exit()
    except ValueError:
        print("============================\nNot allowed Answer!\n============================")
        exit()
    except Exception:
        exit()

print(FLAG)

</code>
they get values hould find this values and get rsa viasolving(solution will be improved after ginish
<pre>
import blog

import os,subprocess
def solve(n,e,c, p,q):
       
    return blog.solveup("rsa",n,e,c,p,q)

if __name__ == "__main__" :
 #find your values and nec pq
 n = blog.set(831416828080417866340504968188990032810316193533653516022175784399720141076262857,1)
 e = blog.set(65537,2)
 c =blog.set( 240986837130071017759137533082982207147971245672412893755780400885108149004760496,3)
 p = blog.set(1593021310640923782355996681284584012117,4)
 q = blog.set(521911930824021492581321351826927897005221,5)
 print(solve(n,e,c,p,q))
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{more_than_m33ts_the_3y3657BaB2C}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on develper tools in in chrome and web exploitations</p>

</body>
</html>
