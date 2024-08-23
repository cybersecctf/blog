<title>interencdec- picoctf2024</title>

<!DOCTYPE html>
<html>

<body>
    <h1>interencdec- picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p>AUTHOR: NGIRIMANA SCHADRACK

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
import blog
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
def solve(ciphertext,searchtext,shift=-1):
 if searchtext.isnumeric():
            shift=int(searchtext)
 # Try all shifts from 1 to 32
 if shift ==-1:
  for shift in range(1, 33):
    plaintext = caesar_decrypt(ciphertext, shift)
    if searchtext in plaintext :
        print("Shift:", shift)
        print("Decrypted result plaintext:", plaintext)
     
 else:
    plaintext = caesar_decrypt(ciphertext, shift)
    print("Decrypted [plaintext] in [shift]: ", plaintext,shift)
if __name__ == "__main__" :
    ciphertext=blog.set("wpjvJAM{jhlzhy_k3jy9wa3k_lh60l00i}",1)
    searchtext=blog.set("",2)
    shift=blog.set(-1,3)
    solve(ciphertext,searchtext,shift)
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

