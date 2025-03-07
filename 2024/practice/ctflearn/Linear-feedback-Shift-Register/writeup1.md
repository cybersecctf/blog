<title>ctflearn--Linear-feedback. Shift. Register.Writeup </title>
 

<!DOCTYPE html>
<html>
 
<body>
    <h1>ctflearn--Linear-feedback. Shift. Register.Writeup </h1>
    <h2>Challenge Description</h2>
    <p> Hello!

I have just implemented a super-cool PRNG!

I've used every next generated by it number to XOR every next character in my super-secret message with.

Are you able to retrieve it?

Btw. Biggest possibly generated number by my PRNG is 255.

Psst. The retrieved message would be your flag!

As always, starting with: CTFlearn{...

I'm giving you the PRNG scheme with a brief description (description.png) and a "secretMessage.hex" file with every byte being the corresponding message char inside PRNG.zip file.
<a href="https://cybersecctf.github.io/blog/2024/practice/ctflearn/Linear-feedback-Shift-Register/PRNG.zip">PRNG.zip</a>

</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li> we extract zip and see a hex and image
<img src=" https://cybersecctf.github.io/blog/2024/practice/ctflearn/Linear-feedback-Shift-Register/PRNG/description.png" alt="PRNG scheme" width="500" height="600" class="inline"/>

<pre>
import blog

import os,subprocess
def msb(num, pos):
    ret = (num & (1 << pos[0])) >> pos[0]
    for p in pos[1:]:
        ret ^= (num & (1 << p)) >> p
    return ret

def get_next(last, pos):
    m = msb(last, pos)
    return (m << 7)|(last >> 1)

def solve(cipher,prefix,msb_pos):
   
    last = 0
    last = prefix[-1] ^ cipher[len(prefix)-1]

    output=''
    
    for i in range(len(prefix), len(cipher)):
        last = get_next(last, msb_pos)
        output += chr(cipher[i] ^ last)
        
    return prefix + output.encode()
if __name__ == "__main__" :
 cipher = blog.set("./PRNG/secretMessage.hex",1)
 prefix =blog.set( b"CTFlearn{",2)
 msb_pos = blog.set([6,5,3,2,0],3)
 print(solve(cipher,prefix,msb_pos))
 
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlearn{Lin34r_F33db4ck_Sh1fT_R3g1st3r}
</p>

    <h2>Conclusion</h2>
    <p>this is a hard challenge for work on  Linear Feedback Shift Register (LFSR)</p>

</body>
</html>
