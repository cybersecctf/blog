
<!DOCTYPE html>
<html>

<body>
    <h1>Deep stego in the office- spcsctf</h1>

    <h2>Challenge Description</h2>
    <p> 
We hide the flag in the standard way. Almost the same as in any type of file


</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
understand this code and enter flag 0
<pre>
from hashlib import md5

cipher = "/:7,67Ct01;'1;'8:7*)*4A'.->-:'.:75'<0-'=88-:'n14-E"
hash_val = "14927c0edb1bfaf21c81d6b88ca9472a"

def caesar_decrypt(input_string, shift):
    output_string = ""
    for char in input_string:
        ascii_val = ord(char)
        new_ascii_val = ((ascii_val - 32 - shift) % 94) + 32
        output_string += chr(new_ascii_val)
    return output_string

for shift in range(94):
    potential_plaintext = caesar_decrypt(cipher, shift)
    if md5(potential_plaintext.encode()).hexdigest() == hash_val:
        print(f"Found potential flag: {potential_plaintext} with shift {shift}")
        break

</pre>        
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">0
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work onsocket code and competetion style </p>
</body>
</html>


