
<!DOCTYPE html>
<html>

<body>
    <h1>ModulusInutilis - cryptohack</h1>

    <h2>Challenge Description</h2>
    <p>My primes should be more than large enough now!

 
 

Challenge files:
  - <a href=""https://cybersecctf.github.io/blog/2024/practice/cryptohack/PUBLIC-KEY-CRYPTOGRAPHY/ModulusInutilis/modulus_inutilis.py">modulus_inutilis.py</a>
  -   - <a href="https://cybersecctf.github.io/blog/2024/practice/cryptohack/PUBLIC-KEY-CRYPTOGRAPHY/ModulusInutilis/output.txtt">output.txt</a>

 </p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
for get flag run this code if blog.solveup("isprine",n) not working use site and get primefactor list of n and calculate phi and then get flag with run this code
<pre>
import blog
 
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
import sympy
def solve(n,e,ct):

 m = sympy.root(ct, e)
 return long_to_bytes(m)
   
if __name__ == "__main__" :

 n = 17258212916191948536348548470938004244269544560039009244721959293554822498047075403658429865201816363311805874117705688359853941515579440852166618074161313773416434156467811969628473425365608002907061241714688204565170146117869742910273064909154666642642308154422770994836108669814632309362483307560217924183202838588431342622551598499747369771295105890359290073146330677383341121242366368309126850094371525078749496850520075015636716490087482193603562501577348571256210991732071282478547626856068209192987351212490642903450263288650415552403935705444809043563866466823492258216747445926536608548665086042098252335883
 e = 3
 ct = 243251053617903760309941844835411292373350655973075480264001352919865180151222189820473358411037759381328642957324889519192337152355302808400638052620580409813222660643570085177957 
 print( solve(n,e,ct))
</pre>
 
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">crypto{N33d_m04R_p4dd1ng}</p>

    <h2>Conclusion</h2>
    <p>this is a    medium chanllenge for decrypt message with n that e is small like 3</p>
</body>
</html>






