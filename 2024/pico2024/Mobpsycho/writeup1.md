
<!DOCTYPE html>
<html>

<body>
    <h1>Mob psycho- picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: NGIRIMANA SCHADRACK
hex
Description
Can you handle APKs?
Download the android apk <a href="https://artifacts.picoctf.net/c_titan/51/mobpsycho.apk">here</a>.
 
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
          we downlod apk and unzip it and search inside apk with find to find a file with contain flag in name or maybe pico(can't find good thingwith grip )<p id="code1">grep -r "pico" "/home/kali/Desktop/blog/2024/pico2024/Mobpsycho" or grep -r "flag" "/home/kali/Desktop/blog/2024/pico2024/Mobpsycho" 
</p>
but search file with name flag if find find anything and yes find with this command <pre> $find "/home/kali/Desktop/blog/2024/pico2024/Mobpsycho" -type f -name '*flag*'
find "/home/kali/Desktop/blog/2024/pico2024/Mobpsycho"-type f -name '*flag*' -printf "%f\n" | grep -i "pico"(not working)
</pre>
 and find this hex that should convert it with python or online tool and get flag
<pre>
 import base64
from binascii import unhexlify

hex = unhexlify('7069636f4354467b6178386d433052553676655f4e5838356c346178386d436c5f35326135653264657d')
 
print(hex) 
</pre>
 
 
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_52a5e2de}
</p>

    <h2>Conclusion</h2>
    <p>this is a    easy chanllenge for find file inside apk files</p>
</body>
</html>


