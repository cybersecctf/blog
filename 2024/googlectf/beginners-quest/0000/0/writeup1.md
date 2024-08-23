<title>google ctf begginer quest-  0000 0</title>
<!DOCTYPE html>
<html>

<body>
    <h1>google ctf begginer quest-  0000 0</h1>

    <h2>Challenge Description</h2>
    <p>  Let's test your knowledge on Caesar's methods     


<a href="https://cybersecctf.github.io/blog/2024/googlectf/beginners-quest/0000/0/message.txt">message.txt</a>

</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
       this is begginer quest for use caesar 
       for find flag use this code
<pre>
#python
import sys
values=sys.argv
 
def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            if char.isupper():
                plaintext += chr((ord(char) - int(shift) - 65) % 26 + 65)
            else:
                plaintext += chr((ord(char) - int(shift) - 97) % 26 + 97)
        else:
            plaintext += char
    return plaintext
ciphertext="wpjvJAM{jhlzhy_k3jy9wa3k_lh60l00i}"
searchtext=""
shift=-1
print(sys.argv)
if len (sys.argv)>1:
 ciphertext =sys.argv[1]#for decrypt another caesar text
 if len (sys.argv)>2:
       if sys.argv[2].isnumeric():
            shift=sys.argv[2]
       else:
             searchtext=sys.argv[2] 
# Try all shifts from 1 to 32
if shift ==-1:
 for shift in range(1, 33):
    plaintext = caesar_decrypt(ciphertext, shift)
    if searchtext in plaintext :
        print("Shift:", shift)
        print("Decrypted plaintext:", plaintext)
     
else:
    plaintext = caesar_decrypt(ciphertext, shift)
    print("Decrypted [plaintext] in [shift]: ", plaintext,shift)</pre>
with argument message(,essage.txt content) "FLAG" and get flag
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">FLAG{rotate_that_alphabet}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on caesar and crypto </p>
</body>
</html>

