
<!DOCTYPE html>
<html>

<body>
    <h1>basic-mod1- picoctf2022</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: WILL HONG

Description
We found this weird message being passed around on the servers, we think we have a working decryption scheme.
Download the message <a href="https://artifacts.picoctf.net/c/127/message.txt">here</a>.
Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
       we see info ,
The provided info appears to be performing a basic form of cryptography known as a simple substitution cipher.

In a substitution cipher, each character in the plaintext is replaced by another character according to a fixed system. In this case, the numbers in the string s are being used to index into the alphabet string, effectively mapping each number to a corresponding character.

Here's how it works:

Each number in the string s represents an index position within the alphabet string.
The numbers are converted into characters by looking up their corresponding positions in the alphabet string.
The resulting characters are concatenated together to form the final ciphertext.
this is full code of sample   substitution cipher with number and decimal
<pre>
import sys

s="128 322 353 235 336 73 198 332 202 285 57 87 262 221 218 405 335 101 256 227 112 140"
if len(sys.argv)>1:
   s=sys.argv[1]

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
if len(sys.argv)>2:
  alphabet=sys.argv[2]
f=""
for x in s.split():
    f+=alphabet[int(x)%37]
print(f)
</pre>     
    and run and wrap result with picoCTF
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{R0UND_N_R0UND_79C18FB3}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for     substitution cipher  and cryptography with python</p>
</body>
</html>


