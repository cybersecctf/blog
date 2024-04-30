
<!DOCTYPE html>
<html>

<body>
    <h1>recursive-cracke- bsides-delhi-ctf2018</h1>

    <h2>Challenge Description</h2>
    <p> 
 Dig deeper and deeper. Don’t give up hope.
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
    we convert this file 
<a href="https://cybersecctf.github.io/blog/2024/bsidesdl/RecursiveCracker/challenge.txt">challenge.txt </a> to hex via this tool
<a href="https://zb3.me/malbolge-tools/#interpreter">malbolge-tools</a> that this file writed by irs language
then convert hex to file with this <a href="https://cybersecctf.github.io/blog/2024/bsidesdl/RecursiveCracker/writeup2.md">code</a>
and see is zip file with password crackthem and cat flag.txt and get flag
<pre>
#python
import os,sys
zipfile="flag.zip"
dictionary="/home/rockyou.txt "
if len(sys.argv)>1:
    zipfile=sys.argv[1]
if len(sys.argv)>2:
    dictionary=sys.argv[2]
os.system("fcrackzip -v -D -u -p "+dictionary+" "+zipfile)
</pre>
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">flag{Y0u_d1d_1t_br0_k33p_g0inG}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   meidum chanllenge for crack passwords in nested zip</p>
</body>
</html>
