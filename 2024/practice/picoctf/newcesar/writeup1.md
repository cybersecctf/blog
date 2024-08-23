<title>picoctf 2021- New Caesar</title>
<!DOCTYPE html>
<html>
 
<body>
    <h1>picoctf 2021- New Caesar</h1>

    <h2>Challenge Description</h2>
    <p>AUTHOR: MADSTACKS

Description
We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{}) kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm 

<a href="https://mercury.picoctf.net/static/d9c139d91d2dfec8fd197ca6d970381a/new_caesar.py">new_caesar.py</a>

</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
       Write up:
After looking through their code I found a few important facts:

the key was one letter in the first 16 lowercase characters of the alphabet
to decode I would need to unshift first and then decode
So I started dissecting the shift function:
<pre>
def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]
</pre>
To undo this I would simply need to subtract t2 from t1 rather than adding to it, I created the new function and moved to the encode function:
<pre>
def b16_encode(plain):
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))
        enc += ALPHABET[int(binary[:4], 2)]
        enc += ALPHABET[int(binary[4:], 2)]
    return enc
</pre>
This function takes the text and turns each character into binary, then turns the first 4 and last 4 bits into integers and then gets a letter for each of these from the alphabet list. To undo this we need to get the letter placement in ALPHABET and then convert them to binary, combine, and turn into a character.

With this information I created a python script:
<pre>
#python
# import string
import string,sys

# constants
LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

# decode function
def b16_decode(cipher):
    dec = ""
    # loop through the cipher 2 characters at a time
    for c in range(0, len(cipher), 2):
        # turn the two characters into one binary string
        b = ""
        b += "{0:b}".format(ALPHABET.index(cipher[c])).zfill(4)
        b += "{0:b}".format(ALPHABET.index(cipher[c+1])).zfill(4)
        # turn the binary string to a character and add
        dec += chr(int(b,2))
    
    # return
    return dec

# unshift the text
def unshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]

# encrypted flag
enc = "mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj"
if len(sys.argv)>1:
    enc=sys.argv[1]
# loop through all possible keys
for key in ALPHABET:
    # initialize string
    s = ""

    # loop through the encrypted text
    for i,c in enumerate(enc):
        # unshift it based on key
        s += unshift(c, key[i % len(key)])

    # decode
    s = b16_decode(s)

    # print key
    print(s)  
</pre>       
    the results of this <a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/newcesar/new_caesarsolve.py">code</a> is some lines like this
<pre>
©¸¸¹su¥§yªw¨{}vt¥|yzut¥ª©¦vy{v|wu¨¥¥|
§§¨bdhfjleckhidcehjekfdk
qQqSWUY[TRZWXSRTWYTZUSZ
v`@`BrtFwDuHJCArIFGBArwvsCFHCIDBurrI
et_tu?_1ac5f3d7920a85610afeb2572831daa8
TcNcd.N PR$U"S&(!/P'$% /PUTQ!$&!'" SPP'
CR=RS=OADBOODC@BOO
2A,AB,>03
</pre>
i tested lines wrapped in picoCTF{} and finnaly et_tu?_1ac5f3d7920a85610afeb2572831daa8 was correct answer.
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{et_tu?_1ac5f3d7920a85610afeb2572831daa8}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for reverse python and custom caesar decryption and cryptography</p>
</body>
</html>


