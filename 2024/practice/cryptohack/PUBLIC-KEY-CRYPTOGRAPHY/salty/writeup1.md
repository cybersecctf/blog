<title>salty - cryptohack</title>

<!DOCTYPE html>
<html>

<body>
    <h1>salty - cryptohack</h1>

    <h2>Challenge Description</h2>
    <p>Smallest exponent should be fastest, right?

Challenge files:
  - <a href="https://cryptohack.org/static/challenges/salty_9854bdcadc3f8b8f58008a24d392c1bf.py">salty</a>
  -   - <a href="https://cryptohack.org/static/challenges/output_95f558e889cc66920c24a961f1fb8181.txt">output.txt</a>

 </p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
for get flag run this code if blog.solveup("isprine",n) not working use site and get primefactor list of n and calculate phi and then get flag with run this code
<pre>
import blog
 
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes

def solve(n,e,ct):
 n = 110581795715958566206600392161360212579669637391437097703685154237017351570464767725324182051199901920318211290404777259728923614917211291562555864753005179326101890427669819834642007924406862482343614488768256951616086287044725034412802176312273081322195866046098595306261781788276570920467840172004530873767
 e = 1
 ct = 44981230718212183604274785925793145442655465025264554046028251311164494127485
 return long_to_bytes(ct)
if __name__ == "__main__" :
 n = blog.set(110581795715958566206600392161360212579669637391437097703685154237017351570464767725324182051199901920318211290404777259728923614917211291562555864753005179326101890427669819834642007924406862482343614488768256951616086287044725034412802176312273081322195866046098595306261781788276570920467840172004530873767,1)                                                                
 e = blog.set(1,2)
 ct = blog.set(44981230718212183604274785925793145442655465025264554046028251311164494127485,3)

 print(solve(n,e,ct,) )
</pre>
 
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">crypto{saltstack_fell_for_this!}</p>

    <h2>Conclusion</h2>
    <p>this is a    medium chanllenge for decrypt message with n that e is small like 1</p>
</body>
</html>




