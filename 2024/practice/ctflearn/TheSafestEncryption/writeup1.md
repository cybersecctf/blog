<title>The Safest Encryption--ctflearn </title>

<!DOCTYPE html>
<html>
 
<body>
    <h1>The Safest Encryption--ctflearn </h1>

    <h2>Challenge Description</h2>
    <p> I intercepted this zip file, the contents seem to be encrypted, but it looks like the key is also in there. Could you try recovering the encrypted file?
<a href="https://cybersecctf.github.io/blog/2024/practice/ctflearn/TheSafestEncryption/CTFlearn.zip">CTFlearn.zip</a>
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>
this is encrypted two file in txt and pdf but can't open in any editor and mean nothing in hex editor
but two file maybe need xor so if use this python code can get file that can open with editor and
flag is inside it

<pre>
 
import blog


def solve(file1,file2):
 # Read two files as byte arrays
 file1_b = bytearray(open(file1, 'rb').read())
 file2_b = bytearray(open(file2, 'rb').read())
 # Set the length to be the smaller one
 size = min(len(file1_b), len(file2_b))
 xord_byte_array = bytearray(size)
 # XOR between the files
 for i in range(size):
    xord_byte_array[i] = file1_b[i] ^ file2_b[i]
 # Write the XORed bytes to the output file
 with open('output', 'wb') as output_file:
    output_file.write(xord_byte_array)
 print( "XOR operation completed and saved to output")
if __name__ == "__main__" :
 file1=blog.set("CTFLearn.pdf",1)
 file2=blog.set("CTFLearn.txt",2)
 print(solve(file1,file2))
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlearn{CTFlearn_is_fun_hope_you_enjoyed_it!}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for xor two file</p>

</body>
</html>

