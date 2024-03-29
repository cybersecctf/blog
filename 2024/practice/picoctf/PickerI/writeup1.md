 
<!DOCTYPE html>
<html>
 
<body>
    <h1>Picker I- picoGym Exclusive</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: LT 'SYREAL' JONES

Description
This service can provide you with a random number, but can it do anything else?
Additional details will be available after launching your challenge instance.
------------------------------------------------------------------------------
Connect to the program with netcat:
$ nc saturn.picoctf.net 57313
The program's source code can be downloaded <a href="https://artifacts.picoctf.net/c/514/picker-I.py">her</a>
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
         we open  source .this is what do
<p id="code1">
This Python script defines several functions and an infinite loop that continuously prompts the user for input and evaluates it. Let's break down the main components:

getRandomNumber(): This function simply prints the number 4. The comment accompanying it is a reference to an <a href="https://en.wikipedia.org/wiki/Xkcd">Xkcd</a> comic about randomness.

exit(): This function calls sys.exit(0) to exit the script with a status code of 0.

esoteric1(): This function contains a multi-line string that seems to be C code related to querying the APM (Advanced Power Management) BIOS. However, this function is never actually called in the script.

win(): This function attempts to open a file named 'flag.txt' in read mode ('r'), reads its contents, processes them, and prints them out. This seems to be the part of the script you're interested in. However, there is a comment indicating that this operation will only work if 'flag.txt' exists in the same directory as the script. Otherwise, it will raise an error.

esoteric2(): Similar to esoteric1(), this function contains a multi-line string that seems to be C code related to testing the A20 line and the keyboard controller (KBC). Again, this function is not called in the script.
</p>
       netcat address print flag in hex when type win so like this code from this<a href="https://phantom1ss.github.io/blog/?q=ASCIINumbers">writeup </a> 
    for print flag in text just run this code 
<pre>


s="0x70 0x69 0x63 0x6f  0x43  0x54 0x46 0x7b 0x34 0x5f 0x64 0x31  0x34  0x6d  0x30 0x6e  0x64  0x5f  0x31 0x6e 0x5f 0x37 0x68 0x33 0x5f 0x72  0x30 0x75 0x67 0x68 0x5f 0x36 0x65 0x30 0x34 0x34 0x34  0x30  0x64, 0x7d "
import base64
from binascii import unhexlify
hex=""
for x in s.split():
 hex+=x.replace("0x","")
hex = unhexlify(hex)
print(hex) 
</pre>
and get flag
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{4_d14m0nd_1n_7h3_r0ugh_6e04440d}

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on reverse engineering with python</p>
</body>
</html>



