<title>google ctf begginer quest-  1943 -1</title>

<!DOCTYPE html>
<html>

<body>
    <h1>google ctf begginer quest-  1943 -1</h1>

    <h2>Challenge Description</h2>
    <p>  
Phew, that was close... but you decrypted that one and  escaped the ambush in time! Sidney Rilley, you've done it again. They almost got lucky this one time. The  nemy continues to use unbreakable encryption. Hopefully, they made at least one mistake and you'll be able t o find and exploit it. If they keep reusing the cipher , just like they repeatedly use your name, maybe we can eventually find a way to defeat it. Login to your terminal (your password is 'Sidney'). Maybe you can decr ypt at least one of the messages. Connect with the command: "socat file:`tty`,rawer tcp:otp1.2023-bq.ctfcompetition.com:1337".Ah, and by the way, our crypto experts said to try crib dragging but we couldn't find any infants around.HINT: "multi-time pad" is a decent crib. The enemy thinks that the multi-time pad can't be broken.
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
         we connect to socat and and inher see this time 4 base64 text
 <img src=" https://cybersecctf.github.io/blog/2024/googlectf/beginners-quest/1943/1/base64.png" alt="ctf quetion image" class="inline"/>
that seems To decrypt the given ciphertexts encrypted using the multi-time pad method, you would typically perform a known-plaintext attack or a crib dragging attack.first need find all known words of 4 base64 with this code
<pre>
#python
from pwn import *


import string
import base64
import itertools

ciphers = [
    "0529242a631234122d2b36697f13272c207f2021283a6b0c7908",
    "2f28202a302029142c653f3c7f2a2636273e3f2d653e25217908",
    "322921780c3a235b3c2c3f207f372e21733a3a2b37263b313012",
    "2f6c363b2b312b1e64651b6537222e37377f2020242b6b2c2d5d",
    "283f652c2b31661426292b653a292c372a2f20212a316b283c09",
    "29232178373c270f682c216532263b2d3632353c2c3c2a293504",
    "613c37373531285b3c2a72273a67212a277f373a243c20203d5d",
    "243a202a633d205b3c2d3765342236653a2c7423202f3f652a18",
    "2239373d6f740a1e3c651f207f2c212a247f3d2e65262430791c",
    "263e203d63232f0f20653f207f332065262c3168313722367918",
    "2f2f372133202f142665212637222220733e383f2426386b",
]

crib = b"multi-time pad"

for i, j in itertools.combinations(range(len(ciphers)), 2):
    log.info(f"XORing {i} and {j}")
    xored = xor(ciphers[i], ciphers[j])
    for offset in range(len(xored) - len(crib) + 1):
        output = xor(xored[offset:offset+len(crib)], crib)
        if all(chr(c) in string.printable for c in output):
          if "{" in output or "}" in output:
            log.info(f"Found readable string at offset {offset}: {output}")
</pre>

and then xor two pairs of 4 base64     and get two hex
<pre>
1b00544916450945111b00263635705a4828544812061c0c543b0c0d1c4517553105090d17595945271f1d1a064e1511060417434c0212155a496e202f1628551c150d74001e45241311250a751b0c1017040a0a030e0918

07001157534f1817451749313b24225d003a410e045745741c0d1c4911410052174c0e0f1d57571109111b4e04455410100d4e021903131003542a39235b3d14085a491d074d1531130d3d10200203004941380806020004
</pre>
and use this command
<pre>
python3 cribdrag.py <A_xored_HEX_FROM_ABOVE>
</pre>
and when request scribe and offset test result get from upper code and get final text
<pre>
let's meet ASAP. I have their nuclear weapons technology. CTF{MultiTimePadIsUnbreakable}
we need to get that spy, Sidney Rilley. Fortunately, multi-time pad is truly unbreakable
keep our ciphers safe! They can't know that we use multi-time pad. In paritcular, Sidney
</pre>
that is flag 
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTF{MultiTimePadIsUnbreakable}
</p>

    <h2>Conclusion</h2>
    <p>this is a     medium  chanllenge for  base64 decode and xor and mult time pad</p>
</body>
</html>




