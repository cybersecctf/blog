<title>ctf event- challengename Challenge Writeup(first save it)</title>

<!DOCTYPE html>
<html>

<body>
    <h1>ctf event- challengename Challenge Writeup(first save it)</h1>

    <h2>Challenge Description</h2>
    <p> your description
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
<pre>
#python
from Crypto.Util.number import inverse
from binascii import unhexlify

# Given values
n = 86088719452932625928188797700212036385645851492281481088289877829109110203124545852827976798704364393182426900932380436551569867036871171400190786913084554536903236375579771401257801115918586590639686117179685431627540567894983403579070366895343181435791515535593260495162656111028487919107927692512155290673
e = 65537
c = 64457111821105649174362298452450091137161142479679349324820456191542295609033025036769398863050668733308827861582321665479620448998471034645792165920115009947792955402994892700435507896792829140545387740663865218579313148804819896796193817727423074201660305082597780007494535370991899386707740199516316196758
phi = 86088719452932625928188797700212036385645851492281481088289877829109110203124545852827976798704364393182426900932380436551569867036871171400190786913084573410416063246853198167436938724585247461433706053188624379514833802770205501907568228388536548010385588837258085711058519777393945044905741975952241886308

# Compute the private key d
d = inverse(e, phi)

# Decrypt the message
m = pow(c, d, n)

# Convert the message from int to bytes
flag_bytes = m.to_bytes((m.bit_length() + 7) // 8, 'big')
flag_bytes=str(flag_bytes).replace("\\x"," ")
print(flag_bytes)
s=unhexlify("8c 98 c2 c1 c1")
# Convert the bytes to ASCII
# Convert the bytes to a string using UTF-8 encoding
# Convert the bytes to a hexadecimal string
 
# Convert the hexadecimal string to ASCII
#flag_ascii = bytes.fromhex(str(flag_bytes)).decode('ascii')

print(f"Decrypted flag: {s}")



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

