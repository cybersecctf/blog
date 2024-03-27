
<!DOCTYPE html>
<html>

<body>
    <h1>Custom encryption- picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: NGIRIMANA SCHADRACK

Description
Can you get sense of this code file and write the function that will decode the given encrypted file content.
Find the encrypted file here <a href="https://artifacts.picoctf.net/c_titan/16/enc_flag">flag_info</a> and <a href="https://artifacts.picoctf.net/c_titan/16/custom_encryption.py">code file</a> might be good to analyze and get the flag.
</p>
merge
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        we open and see this code
<p id="code1">
def generator(g, x, p):
    return pow(g, x) % p
p = 97
g = 31
a = 97
b = 22
enc =  [151146, 1158786, 1276344, 1360314, 1427490, 1377108, 1074816, 1074816, 386262, 705348, 0, 1393902, 352674, 83970, 1141992, 0, 369468, 1444284, 16794, 1041228, 403056, 453438, 100764, 100764, 285498, 100764, 436644, 856494, 537408, 822906, 436644, 117558, 201528, 285498]


text_key = "trudeau"

u = generator(g, a, p)
v = generator(g, b, p)
key = generator(v, a, p)
b_key = generator(u, b, p)

assert key == b_key

# rev encrypt()

enc1 = ''
for n in enc:
    enc1 += chr(n // (key*311))

print(f'{enc1 = }')


# rev dynamic_xor_encrypt()

dec = ''
for i, char in enumerate(enc1[::-1]):
    key_char = text_key[(len(enc1) - i - 1) % len(text_key)]
    decrypted_char = chr(ord(char) ^ ord(key_char))
    dec += decrypted_char
    
print(dec)
</p>
       
we should reverse it and get message from cipher so use this code and run it
<pre>
def generator(g, x, p):
    return pow(g, x) % p
p = 97
g = 31
a = 97
b = 22
enc =  [151146, 1158786, 1276344, 1360314, 1427490, 1377108, 1074816, 1074816, 386262, 705348, 0, 1393902, 352674, 83970, 1141992, 0, 369468, 1444284, 16794, 1041228, 403056, 453438, 100764, 100764, 285498, 100764, 436644, 856494, 537408, 822906, 436644, 117558, 201528, 285498]


text_key = "trudeau"

u = generator(g, a, p)
v = generator(g, b, p)
key = generator(v, a, p)
b_key = generator(u, b, p)

assert key == b_key

# rev encrypt()

enc1 = ''
for n in enc:
    enc1 += chr(n // (key*311))

print(f'{enc1 = }')


# rev dynamic_xor_encrypt()

dec = ''
for i, char in enumerate(enc1[::-1]):
    key_char = text_key[(len(enc1) - i - 1) % len(text_key)]
    decrypted_char = chr(ord(char) ^ ord(key_char))
    dec += decrypted_char
    
print(dec)
</pre>
    and get flag
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{custom_d2cr0pt6d_e4530597}
</p>

    <h2>Conclusion</h2>
    <p>this is a    easy chanllenge for custom encryption on diffie hellman encryption and reverse it</p>
</body>
</html>


