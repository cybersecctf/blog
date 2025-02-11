<title>lactf2025---crypto/RSAaaS Writeup </title>
 

<!DOCTYPE html>
<html>
 
<body>
    <h1>lactf2025---crypto/RSAaaS Writeup </h1>

    <h2>Challenge Description</h2>
    <p> Tired of doing RSA on your own? Try out my new service!

nc chall.lac.tf 31176
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>we run nc service see say Welcome to my RSA as a Service! 
Pass me two primes and I'll do the rest for you. 
Let's keep the primes at a 64 bit size, please. 
with this code get two flag input them and get flag
<pre>
from Crypto.Util.number import getPrime

p = getPrime(64)
while p % 65537 != 1:
    p = getPrime(64)
q = getPrime(64)

print(p)
print(q)
</pre>
result is here
<code>
 nc chall.lac.tf 31176


Welcome to my RSA as a Service! 
Pass me two primes and I'll do the rest for you. 
Let's keep the primes at a 64 bit size, please. 
Input p: 9551753453307194851
Input q: 14606166476164860221
Oh no! My service! Please don't give us a bad review! 
Here, have a complementary flag for your troubles. 
lactf{actually_though_whens_the_last_time_someone_checked_for_that}

</code>
that ahve flug
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">lactf{actually_though_whens_the_last_time_someone_checked_for_that}
</p>

    <h2>Conclusion</h2>
    <p>this is a medium chanllenge for find two 64 bit prime number and how get p,q in rsa</p>

</body>
</html>
