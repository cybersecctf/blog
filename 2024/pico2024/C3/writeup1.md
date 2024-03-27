
<!DOCTYPE html>
<html>

<body>
    <h1>C3- picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: MATT SUPERDOCK

Description
This is the Custom Cyclical Cipher!
Download the  ciphertext  <a href="https://artifacts.picoctf.net/c_titan/47/ciphertext">here</a>.
Download the encoder  <a href="https://artifacts.picoctf.net/c_titan/47/convert.py">here</a>..
Enclose the flag in our wrapper for submission. If the flag was "example" you would submit "picoCTF{example}".
</p>
merge
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
download files and see code of it
<p id="code1">
$wget https://artifacts.picoctf.net/c_titan/47/ciphertext 
$wget https://artifacts.picoctf.net/c_titan/47/convert.py
</p>
open convert.py
<p id="code1">
import sys
chars = ""
from fileinput import input
for line in input():
  chars += line

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

out = ""

prev = 0
for char in chars:
  cur = lookup1.index(char)
  out += lookup2[(cur - prev) % 40]
  prev = cur

sys.stdout.write(out)
</p>
It imports the sys module for handling standard input and output, and the fileinput module to process input from files.
It defines two strings lookup1 and lookup2. These are essentially lookup tables used for encoding and decoding characters.
lookup1 contains a set of characters, including some special characters, digits, and lowercase letters.
lookup2 contains uppercase letters, both uppercase and lowercase letters are used to generate the encoded output.
It iterates over each line of input using the input() function from fileinput.
For each character in the input, it finds the index of the character in lookup1.
It calculates the new character by subtracting the previous index from the current index modulo 40, and then uses this value as an index to find the corresponding character in lookup2.
It appends the new character to the output string.
Finally, it writes the encoded output to standard output.
 It's a simple substitution cipher where each character is replaced by another character based on its position in the lookup tables.
so on base of upper info can decrypt via thisc ode
  <pre>
enc = ''
with open('ciphertext', 'r') as f:
    enc = f.read()

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

dec = "" 

prev = 0
for char in enc:
    cur = lookup2.index(char)
    print(prev, cur)
    dec += lookup1[(cur + prev) % 40]
    prev = (cur + prev) % 40

    print(dec)

print('---')
print(dec)


#asciiorder
#fortychars
#selfinput
#pythontwo

chars = ""
from fileinput import input
for line in dec:
    chars += line
b = 1 / 1

print(len(chars))

for i in range(len(chars)):
    if i == b * b * b:
        print(chars[i]) #prints
        b += 1 / 1
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


