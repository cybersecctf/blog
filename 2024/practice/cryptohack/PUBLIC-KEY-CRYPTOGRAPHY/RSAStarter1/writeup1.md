<title>RSA Starter 1- cryptohack</title>

<!DOCTYPE html>
<html>

<body>
    <h1>RSA Starter 1- cryptohack</h1>

    <h2>Challenge Description</h2>
    <p> All operations in RSA involve modular exponentiation.

Modular exponentiation is an operation that is used extensively in cryptography and is normally written like: 210 mod 17

You can think of this as raising some number to a certain power (210 = 1024), and then taking the remainder of the division by some other number (1024 mod 17 = 4). In Python there's a built-in operator for performing this operation: pow(base, exponent, modulus)

In RSA, modular exponentiation, together with the problem of prime factorisation, helps us to build a "trapdoor function". This is a function that is easy to compute in one direction, but hard to do in reverse unless you have the right information. It allows us to encrypt a message, and only the person with the key can perform the inverse operation to decrypt it.

Find the solution to 10117 mod 22663

 </p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
<pre>
import blog
def solve(a,b):
 return blog.solveup("find  two integers mod",a,b)
if __name__ == "__main__" :
 a=pow(101,17)
 b=22663
 print(solve(a,b))
</pre>        
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">19906
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for introduce rsa and two integer mod</p>
</body>
</html>


