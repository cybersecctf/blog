 

<!DOCTYPE html>
<html>
 
<body>
    <h1>We want Nudes instead of Nukes--ctflearn  </h1>

    <h2>Challenge Description</h2>
    <p> https://ctflearn.com/challenge/289
 
 
Donald has gone completely crazy. To prevent world chaos, you kidnapped him. Right before the kidnapping he tried to send one encrypted message to his wife Melania. Luckily you intercepted the message. Donald admits that he used AES-CBC encryption - a block cipher operating with a block length of 16 bytes. (here represented by 32 characters)<br /> The message was: {391e95a15847cfd95ecee8f7fe7efd66,8473dcb86bc12c6b6087619c00b6657e}

The format contains first the Initialization vector(IV) and then the cipher text(c) separated by a colon all wrapped in curly braces. {IV,c} After torturing him by stealing his hairpiece, he tells you the plain text of the message is:

FIRE_NUKES_MELA!

As a passionate hacker you of course try to take advantage of this message. To get the flag alter the message that Melania will read: SEND_NUDES_MELA!

Submit the flag in the format: flag{IV,c}

The characters are hexlified, and one byte is represented by two characters; e.g. the string "84" represents the character "F" of the message and so on.
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>after using binawalk and exiftool not working using 

<pre>
import blog

def solve(x1,iv,c):
 # c = Ek(iv xor x1)    ci = Ek(c(i-1) xor xi)
 y1 = "SEND_NUDES_MELA!"
 iv2 = []
 # c will be the same if   iv xor x1 = iv2 xor y1
 #                         iv2 = (iv xor x1) xor y1
 #                         flag{iv2,c}
 for i in range(len(iv)):
    #print("",ord(x1[i]),end="")
    #iv1.append(iv[i])
    d=blog.solveup("venona","encode",iv[i]^ord(x1[i])^ord(y1[i]),"int hex").replace("0x","")  
    iv2.append(d)
 return "".join(iv2)
if __name__ == "__main__" :
 x1 =blog.set( "FIRE_NUKES_MELA!",1)
 iv =blog.set( b'\x39\x1e\x95\xa1\x58\x47\xcf\xd9\x5e\xce\xe8\xf7\xfe\x7e\xfd\x66',2)
 c =blog.set( b'\x84\x73\xdc\xb8\x6b\xc1\x2c\x6b\x60\x87\x61\x9c\x00\xb6\x65\x7e',3) 
 iv2=solve(x1,iv,c)
 print(iv2)
</pre>
flag is flag{iv2,c} that c is 8473dcb86bc12c6b6087619c00b6657e
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">flag{2c1289a05847cfd65ecee8f7fe7efd66,8473dcb86bc12c6b6087619c00b6657e}
</p>

    <h2>Conclusion</h2>
    <p>this is a hard chanllenge for work on   aes cbc</p>

</body>
</html>
