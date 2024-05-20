<!DOCTYPE html>
<html>

<body>
    <h1>Modular Arithmetic 2- cryptohack</h1>
 
    <h2>Challenge Description</h2>
    <p> We'll pick up from the last challenge and imagine we've picked a modulus p, and we will restrict ourselves to the case when p is prime.

The integers modulo p define a field, denoted Fp.

If the modulus is not prime, the set of integers modulo n define a ring.


A finite field Fp is the set of integers {0,1,...,p-1}, and under both addition and multiplication there is an inverse element b for every element a in the set, such that a + b = 0 and a * b = 1.

 Note that the identity element for addition and multiplication is different! This is because the identity when acted with the operator should do nothing: a + 0 = a and a * 1 = a.


Lets say we pick p = 17. Calculate 317 mod 17. Now do the same but with 517 mod 17.

What would you expect to get for 716 mod 17? Try calculating that.

This interesting fact is known as Fermat's little theorem. We'll be needing this (and its generalisations) when we look at RSA cryptography.

Now take the prime p = 65537. Calculate 27324678765465536 mod 65537.

Did you need a calculator?
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
this is quetion for see if two  number 
are set in Fermat's little theorem. or no and so a^b+1 %b-1 is 1 or no (need in rsa).
<pre>
#python   
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
def fermat_test(a, p):
    return pow(a, p - 1, p)  
import sys
# Test the function with your number and a prime

a=blog.setval(273246787654,1)

p=blog.setval(17,2) 
 
print(fermat_test(a, p))   
</pre>
        
    
    </ol>
<br> 
    <h2>Flag</h2>
    <p class="flag">1
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on  Fermat's little theorem</p>
</body>
</html>

