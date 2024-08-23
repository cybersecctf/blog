<title>char50- learningctf2024</title>

<!DOCTYPE html>
<html>

<body>
    <h1>char50- learningctf2024</h1>

    <h2>Challenge Description</h2>
    <p> create 50 random char and wraped it with flag{}
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
 run this code and get flag
<pre>
#python
import random,string
print(''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=50)))
</pre>
       and get flag
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">flag{bxlc6zhjaihmvsblfcqtbct5ui191m7jv4q1ip2mecfk73b30w}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for  create random 50 character</p>
</body>
</html>

