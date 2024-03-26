
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
from Crypto.Util.number import inverse, long_to_bytes

c = 240986837130071017759137533082982207147971245672412893755780400885108149004760496
n = 831416828080417866340504968188990032810316193533653516022175784399720141076262857
e = 65537
p = 1593021310640923782355996681284584012117
q = 521911930824021492581321351826927897005221

phi = (p-1)*(q-1)

d = inverse(e, phi)

m = pow(c,d,n)

print(long_to_bytes(m))
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