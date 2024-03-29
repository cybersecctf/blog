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
<pre>
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

</pre>
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">flag{}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on develper tools in in chrome and web exploitations</p>
</body>
</html>


