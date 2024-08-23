<title>Easy Peasy - picoctf2021</title>
<!DOCTYPE html>
<html>

<body>
    <h1>Easy Peasy - picoctf2021</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: MADSTACKS

Description
A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{}) nc mercury.picoctf.net 20266 <a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/EasyPeasy/otp.py">otp.py</a>
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        we download file and open it
       <p id="code1">
$wget https://mercury.picoctf.net/static/84c434ada6e2f770b5000292cadae7eb/otp.py
 </p> 
and open code see this is xor encrypting of flag whithis code
<p id="code1">
ui = input("What data would you like to encrypt? ").rstrip()
        if len(ui) == 0 or len(ui) > KEY_LEN:
                return -1

        start = key_location
        stop = key_location + len(ui)

        kf = open(KEY_FILE, "rb").read()

        if stop >= KEY_LEN:
                stop = stop % KEY_LEN
                key = kf[start:] + kf[:stop]
        else:
                key = kf[start:stop]
        key_location = stop

        result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), ui, key))

        print("Here ya go!\n{}\n".format("".join(result)))

        return key_location


print("******************Welcome to our OTP implementation!******************")
c = startup(0)
while c >= 0:
        c = encrypt(c)

</p>
 and reverse it and opwn it and convert flag from hex to text and get flag
<pre>
from pwn import *

KEY_LEN = 50000
MAX_CHUNK = 1000

r = remote("mercury.picoctf.net", 20266)
r.recvuntil("This is the encrypted flag!\n")
flag = r.recvlineS(keepends = False)
log.info(f"Flag: {flag}")
bin_flag = unhex(flag)

counter = KEY_LEN - len(bin_flag)

with log.progress('waiting...') as p:
    while counter > 0:
        p.status(f"{counter} bytes left")
        chunk_size = min(MAX_CHUNK, counter)
        r.sendlineafter("What data would you like to encrypt? ", "a" * chunk_size)
        
        counter -= chunk_size
 
r.sendlineafter("What data would you like to encrypt? ", bin_flag)
r.recvlineS()
flag=r.recvlineS()
print("The flag: {}".format(flag))
s=bytearray.fromhex(flag).decode()
print(s)
</pre>      
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{99072996e6f7d397f6ea0128b4517c23}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for reversing enginering   python and    xor and pwn easy</p>
</body>
</html>


