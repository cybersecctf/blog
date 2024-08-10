 

<!DOCTYPE html>
<html>
 
<body>
    <h1>tryhackme---encryption 101 task7 Establishing Keys Using Asymmetric Cryptography
 Writeup </h1>

    <h2>Challenge Description</h2>
    <p> A very common use of asymmetric cryptography is exchanging keys for symmetric encryption.

Asymmetric encryption tends to be slower, so for things like HTTPS symmetric encryption is better.

But the question is, how do you agree a key with the server without transmitting the key for people snooping to see?

Metaphor time
Imagine you have a secret code, and instructions for how to use the secret code. If you want to send your friend the instructions without anyone else being able to read it, what you could do is ask your friend for a lock.

Only they have the key for this lock, and we’ll assume you have an indestructible box that you can lock with it.

If you send the instructions in a locked box to your friend, they can unlock it once it reaches them and read the instructions.

After that, you can communicate in the secret code without risk of people snooping.

In this metaphor, the secret code represents a symmetric encryption key, the lock represents the server’s public key, and the key represents the server’s private key.

You’ve only used asymmetric cryptography once, so it’s fast, and you can now communicate privately with symmetric encryption.

The Real World
In reality, you need a little more cryptography to verify the person you’re talking to is who they say they are, which is done using digital signatures and certificates. You can find a lot more detail on how HTTPS (one example where you need to exchange keys) really works from this excellent blog post. https://robertheaton.com/2014/03/27/how-does-https-actually-work/


</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>no need qution just click compleye

<pre>
import blog

import os,subprocess
def solve():
   blog.solveup("inspect","https://robertheaton.com/2014/03/27/how-does-https-actually-work/","")
   return "complete"

if __name__ == "__main__" :
  print(solve())
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">complete
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on develper tools in in chrome and web exploitations</p>

</body>
</html>
