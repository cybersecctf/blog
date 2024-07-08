 
<!DOCTYPE html>
<html>

<body>
    <h1>Attack on AES- spcsctf</h1>

    <h2>Challenge Description</h2>
    <p> 
In this task, you need to decrypt ciphertext and find a flag encrypted using an Advanced Encryption Standard (AES) block cipher in Electronic Code Book (ECB) mode.

You have access to the encryption device and can encrypt arbitrary data to which the flag is added, reusing the same key each time.

nc ctf.mf.grsu.by 9016

</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
<pre>
import blog
blog.islog=True
blog.solveup("google venona one time pad xor")
</pre>
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">0
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work onsocket code and competetion style </p>
</body>
</html>


