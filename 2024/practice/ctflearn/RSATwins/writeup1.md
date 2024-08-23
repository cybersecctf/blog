<title>RSA Twins!--glory of garden  Writeup </title>
 

<!DOCTYPE html>
<html>
 
<body>
    <h1>RSA Twins!--glory of garden  Writeup </h1>

    <h2>Challenge Description</h2>
    <p> https://mega.nz/#!2aBwFCKa!NWQKRIbYzSAU2iwCPNppO7SE92W6sne4FKD3sKE2A-k 
Aww, twins :). Theyâre so cute! They must be (almost) identical because theyâre the same except for the slightest difference. Anyway, see if you can find my flag. Hint: This is just math. You're probably not going to find any sort of specialized attack.
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>
we open link and see this text and solve with our blog rsa solveup and get flag
this rsa is factorization attack becaouse can solve by this method and not working by large n
and p and q are correct and p*q=n p,q is factors of n
<code>
n = 14783703403657671882600600446061886156235531325852194800287001788765221084107631153330658325830443132164971084137462046607458019775851952933254941568056899

e = 65537

c = 684151956678815994103733261966890872908254340972007896833477109225858676207046453897176861126186570268646592844185948487733725335274498844684380516667587
</code>

<pre>
import blog
def solve(n,e,c):
 try: 
  s=blog.solveup("rsa",n,e,c)
 except:
  return "invalid parameters for factorization attack  do another rsa atttack"
 return s
if __name__ == "__main__" :
 n =blog.set( 14783703403657671882600600446061886156235531325852194800287001788765221084107631153330658325830443132164971084137462046607458019775851952933254941568056899,1)
 
 e =blog.set( 65537,2)

 c =blog.set( 684151956678815994103733261966890872908254340972007896833477109225858676207046453897176861126186570268646592844185948487733725335274498844684380516667587,3)
 print(solve(n,e,c))
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">flag{i_l0v3_tw1N_pr1m3s}
</p>

    <h2>Conclusion</h2>
    <p>this is a  easy chanllenge for </p>

</body>
</html>
