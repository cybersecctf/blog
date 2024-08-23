<title>Mind your Ps and Qs- cpicoctf2024</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Mind your Ps and Qs- cpicoctf2024</h1>

    <h2>Challenge Description</h2>
    <p> 

</p>
</p>
merge
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
  mindyourpsqs is english <a href="https://en.wikipedia.org/wiki/Mind_your_Ps_and_Qs">term</a>  means watch your tals and manners .see wiki page for complete define here means separate p and q in n via <a href="http://factordb.com/index.php?showid=1100000002524321038">factordb</a>or any way and then use this code and run it and get flag.this ways is good for small n and notice that small n isn't good for encryption with rsa at all.
<pre>
#python
from Crypto.Util.number import inverse, long_to_bytes
import blog
def solve(n,e,c,p=0,q=0):
  if type(n)!="<class 'int'>":
    n=int(n)
  if type(e)!="<class 'int'>":
    e=int(e)
  if type(c)!="<class 'int'>":
    c=int(c)

  if p==0 and q==0: 
    p,q=blog.solveup("isprime",n)
  phi = (p-1)*(q-1)
  d = inverse(e, phi)
  m = pow(c,d,n)
  return long_to_bytes(m)
if __name__ == "__main__" :
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
    <p class="flag">picoCTF{sma11_N_n0_g0od_23540368}
</p>
/x
    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for  on rsa small n(81 and less 100 char)  and e=65537</p>
</body>
</html>




<a href="http://factordb.com/index.php?showid=1100000002524321038">factordb</a>