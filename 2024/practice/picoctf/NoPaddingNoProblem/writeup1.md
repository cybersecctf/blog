<title>No Padding, No Problem- picoctf 2021</title>

<!DOCTYPE html>
<html>

<body>
    <h1>No Padding, No Problem- picoctf 2021</h1>

    <h2>Challenge Description</h2>
    <p>AUTHOR: SARA

Description
Oracles can be your best friend, they will decrypt anything, except the flag's ciphertext. How will you break it? Connect with nc mercury.picoctf.net 30048.
</p>
 
    <h2>Solution Approach</h2>
    <p>on base of https://ctftime.org/writeup/27357  </p>
    <ol>
        The provided netcat connection gives the public modulus n and public exponent e as well as the ciphertext. This is also a Oracle because we can provide come ciphertext and the program will decrypt it for us.
Reading Bitsdeep's article on RSA Oracle, we could multiply the ciphertext my another cipher text c2 which me know the plain text of and recover the decrypted c1 ciphertext. Heres how the math works: C = c*c_2 = M^e*2^e = 2M^e. So we just need to divide the returned plaintext by 2 to get the deciphered flag.
a offline code for get argument of n e c and get plain text by oracle is 
    <pre>
#python
from pwn import *


def integer_to_bytes(integer, _bytes):
    output = bytearray()
    for byte in range(_bytes):
        output.append((integer >> (8 * (_bytes - 1 - byte))) & 255)
    return output

address='mercury.picoctf.net'
if len(sys.argv)>1:
 address=sys.argv[1]
port=30048
if len(sys.argv)>2:
 port=sys.argv[2]


conn = remote(address, port)
conn.recvuntil("n: ")
n = int(conn.recvline().decode('utf-8'))
conn.recvuntil("e: ")
e = int(conn.recvline().decode('utf-8'))
conn.recvuntil("ciphertext: ")
c = int(conn.recvline().decode('utf-8'))
#plaintext = "helloworld"
#plaintext = "".join([str(ord(c)) for c in plaintext])
#encrypted = str(pow(int(plaintext), e, n)).encode('utf-8')
# print(plaintext)
evil = pow(2, e, n)
encrypted = str(evil * c)
conn.sendline(encrypted.encode('utf-8'))
conn.recvuntil("go: ")
p = int(conn.recvline().decode('utf-8')) // 2
print(bytes.fromhex(hex(p)[2:]).decode('utf-8'))
</pre>

    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{m4yb3_Th0se_m3s54g3s_4r3_difurrent_5052620}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on oracle rsa attack on python</p>
</body>
</html>

