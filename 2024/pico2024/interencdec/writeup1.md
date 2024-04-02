
<!DOCTYPE html>
<html>

<body>
    <h1>interencdec- picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p>AUTHOR: NGIRIMANA SCHADRACK

Description
Can you get the real meaning from this file.
Download the file 
<a href="https://artifacts.picoctf.net/c_titan/1/enc_flag">here</a>.
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
   we download files and see them
    YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgyeG9OakJzTURCcGZRPT0nCg== is seems like base64 encoded text decode it with this command twice becaouse result was also base64
<p id="code1">
$echo "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgyeG9OakJzTURCcGZRPT0nCg==" |base64 -d
$echo "d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2xoNjBsMDBpfQ==" |base64 -d
</p>
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
                plaintext += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                plaintext += chr((ord(char) - shift - 97) % 26 + 97)
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
       if sys.argv.isnumeric():
            shift=sys.argv[2]
        else:
             searchtext=sys.argv[2] 
# Try all shifts from 1 to 32
if shift ==-1:
for shift in range(1, 33):
    plaintext = caesar_decrypt(ciphertext, shift)
    if plaintext.startswith("pico"):
        print("Shift:", shift)
        print("Decrypted plaintext:", plaintext)
        break
else:
    plaintext = caesar_decrypt(ciphertext, shift)
    print("Decrypted [plaintext] in [shift]: ", plaintext,shift)
    break
</pre>
                   
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag"> picoCTF{caesar_d3cr9pt3d_ea60e00b}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work oncryptograpy and convert between base64 and caesarcipher and text</p>
</body>
</html>

