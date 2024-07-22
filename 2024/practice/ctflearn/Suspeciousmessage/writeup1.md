
<!DOCTYPE html>
<html>

<body>
    <h1>Suspecious message
- ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> Hello! My friend Fari send me this suspecious message: 'MQDzqdor{Ix4Oa41W_1F_B00h_m1YlqPpPP}' and photo.png. Help me decrypt this!
 https://ctflearn.com/challenge/download/887
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
this is playfair cipher open this <a href="http://rumkin.com/tools/cipher/playfair.php">site</a> with this options 
 <img src="https://cybersecctf.github.io/blog/2024/practice/ctflearn/Suspeciousmessage/site.png" alt="playfair site screenshot" width="500" height="600" class="inline"/>
and get flag
<pre>
import blog
def solve(inspecturl="http://rumkin.com/tools/cipher/playfair.php"):
  blog.solveup("inspect",inspecturl)
  blog.solveup("inspect","https://cybersecctf.github.io/blog/2024/practice/ctflearn/Suspeciousmessage/site.png")
if __name__ == "__main__" :
 solve()
</pre>
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlearn{Pl4Yf41R_1S_C00l_c1PheRrRR}


</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on playfair cipher and crypto</p>
</body>
</html>



