
<!DOCTYPE html>
<html>

<body>
    <h1>Factoring - cryptohack</h1>

    <h2>Challenge Description</h2>
    <p> Why is everyone so obsessed with multiplying two primes for RSA. Why not just use one?

Challenge files:
  - <a href="https://cryptohack.org/static/challenges/output_086036e35349a406b94bfac9a7af6cca.txt">output.txt</a>

Resources:
  - <a href="https://crypto.stackexchange.com/questions/5170/why-do-we-need-in-rsa-the-modulus-to-be-product-of-2-primes">Why do we need in RSA the modulus to be product of 2 primes?</a>
 </p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
<pre>
import blog
 
from Crypto.Util.number import bytes_to_long, long_to_bytes


def solve(n,e,ct):
 phi = blog.solveup("phi",n)
 d = blog.solveup("private key d",e,phi)
 pt = pow(ct, d, n)
 return long_to_bytes(pt)
if __name__ == "__main__" :
 n = blog.set(171731371218065444125482536302245915415603318380280392385291836472299752747934607246477508507827284075763910264995326010251268493630501989810855418416643352631102434317900028697993224868629935657273062472544675693365930943308086634291936846505861203914449338007760990051788980485462592823446469606824421932591,1)  
 e = 65537
 ct = 161367550346730604451454756189028938964941280347662098798775466019463375610700074840105776873791605070092554650190486030367121011578171525759600774739890458414593857709994072516290998135846956596662071379067305011746842247628316996977338024343628757374524136260758515864509435302781735938531030576289086798942
 print(solve(n,e,ct)) 
</pre>
 
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">crypto{0n3_pr1m3_41n7_pr1m3_l0l}
</p>

    <h2>Conclusion</h2>
    <p>this is a    medium chanllenge for decrypt message with n is prime and not factoring  pq</p>
</body>
</html>


