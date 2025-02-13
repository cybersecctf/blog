<title>lactf2025---misc/extended  Writeup </title>
 

<!DOCTYPE html>
<html>
 
<body>
    <h1>lactf2025---misc/extended  Writeup </h1>

    <h2>Challenge Description</h2>
    <p>  What if I took my characters and... extended them?
Downloads
<a href="https://chall-files.lac.tf/uploads/b6609714c9d51ed45fca31cbce5768b4a0e262c75aa9fc2802cb161cb4976634/gen.py">gen.py</a>
<a href="https://chall-files.lac.tf/uploads/a841ea3a1960f62ee643d8224f0ae20e0816cd64b0b58abb32b62080b194f58b/chall.txt">chall.txt</a>
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>we download files are this in chall.txt
<code>
ìáãôæûÆõîîéìùßÅîïõçèßÔèéóßÌïïëóßÄéææåòåîôßÏîßÍáãßÁîäß×éîäï÷óý
</code>
and this in gen.py
<code>
flag = "lactf{REDACTED}"
extended_flag = ""

for c in flag:
    o = bin(ord(c))[2:].zfill(8)

    # Replace the first 0 with a 1
    for i in range(8):
        if o[i] == "0":
            o = o[:i] + "1" + o[i + 1 :]
            break

    extended_flag += chr(int(o, 2))

print(extended_flag)

with open("chall.txt", "wb") as f:
    f.write(extended_flag.encode("iso8859-1"))

</code>
in this code 
Read the contents of chall.txt.

For each character, convert it to its binary representation.

Replace the first 1 with a 0 (reversing the modification).

Convert the binary string back to a character.

Reconstruct the original flag.
now return back to flag from chall.txt that is on upper code using this code and get flag
<pre>
with open("chall.txt", "rb") as f:
    extended_flag = f.read().decode("iso8859-1")

# Step 2: Reverse the modification
original_flag = ""

for c in extended_flag:
    # Convert the character to its 8-bit binary representation
    o = bin(ord(c))[2:].zfill(8)
    print(o)
    # Replace the first '1' with '0' to undo the modification
    for i in range(8):
        if o[i] == "1":
            o = o[:i] + "0" + o[i + 1:]
            break
    print(o)
    # Convert the binary string back to a character
    original_flag += chr(int(o, 2))

# Step 3: Print the original flag
print(original_flag)
</pre>
</li>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">lactf{Funnily_Enough_This_Looks_Different_On_Mac_And_Windows}
</p>

    <h2>Conclusion</h2>
    <p>this is a easy chanllenge for reverse binary and cgaracter encoding  in python </p>

</body>
</html>
