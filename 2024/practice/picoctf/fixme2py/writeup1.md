
<!DOCTYPE html>
<html>

<body>
    <h1>beginner picomini 2022- fixme2.py)</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: LT 'SYREAL' JONES

Description
Fix the syntax error in the Python script to print the flag.

<a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/fixme2py/fixme2.py">Download Python script</a>
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
i open script below  of page  and see only this code should change for get flag <pre>if flag = "":</pre> to<pre>
if flag == "":</pre> and then  run code and get flag
     <pre>
import random
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x58) + chr(0x18) + chr(0x11) + chr(0x41) + chr(0x09) + chr(0x5f) + chr(0x1f) + chr(0x10) + chr(0x3b) + chr(0x1b) + chr(0x55) + chr(0x1a) + chr(0x34) + chr(0x5d) + chr(0x51) + chr(0x40) + chr(0x54) + chr(0x09) + chr(0x05) + chr(0x04) + chr(0x57) + chr(0x1b) + chr(0x11) + chr(0x31) + chr(0x0d) + chr(0x5f) + chr(0x05) + chr(0x40) + chr(0x04) + chr(0x0b) + chr(0x0d) + chr(0x0a) + chr(0x19)

  
flag = str_xor(flag_enc, 'enkidu')

# Check that flag is not empty
if flag = "":#convert = to ==
  print('String XOR encountered a problem, quitting.')
else:
  print('That is correct! Here\'s your flag: ' + flag)
</pre>
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{3qu4l1ty_n0t_4551gnm3nt_f6a5aefc}
</p>
    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for  work on python script and differents between = and ==</p>
</body>
</html>

