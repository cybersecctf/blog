<!DOCTYPE html>
<html>

<body>
    <h1>XOR Properties- cryptohack</h1>

    <h2>Challenge Description</h2>
    <p> In the last challenge, you saw how XOR worked at the level of bits. In this one, we're going to cover the properties of the XOR operation and then use them to undo a chain of operations that have encrypted a flag. Gaining an intuition for how this works will help greatly when you come to attacking real cryptosystems later, especially in the block ciphers category.

There are four main properties we should consider when we solve challenges using the XOR operator

Commutative: A ⊕ B = B ⊕ A
Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
Identity: A ⊕ 0 = A
Self-Inverse: A ⊕ A = 0

Let's break this down. Commutative means that the order of the XOR operations is not important. Associative means that a chain of operations can be carried out without order (we do not need to worry about brackets). The identity is 0, so XOR with 0 "does nothing", and lastly something XOR'd with itself returns zero.

Let's put this into practice! Below is a series of outputs where three random keys have been XOR'd together and with the flag. Use the above properties to undo the encryption in the final line to obtain the flag.

KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
i use this code for pairing xor and have flag
<pre>
from pwn import *
import blog
# needed for the xor()
def solve(a,b,type="hex"):
 a = bytes.fromhex(a)
 b = bytes.fromhex(b)
 s=xor(a, b)
 if type=="hex":
  return s.hex()
 else:
   return s.decode()     
if __name__ == "__main__" :
 a=blog.set("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313",1)
 b=blog.set("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e",2)
 type=blog.set("hex",3)    
 print(solve(a,b,type) ) 
</pre>
this is commands and arguments i use in this python code
(last number is result)
<pre>
$python hackcmd.py a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
911404e13f94884eabbec925851240a52fa381ddb79700dd6d0d
$python hackcmd.py 911404e13f94884eabbec925851240a52fa381ddb79700dd6d0d c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
504053b757eafd3d709d6339b140e03d98b9fe62b84add0332cc
$python hackcmd.py a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313 504053b757eafd3d709d6339b140e03d98b9fe62b84add0332cc
f688e5c46b71dfe30b5d460bd7e366406de3338adb14c4c401df
$python hackcmd.py f688e5c46b71dfe30b5d460bd7e366406de3338adb14c4c401df 911404e13f94884eabbec925851240a52fa381ddb79700dd6d0d     
679ce12554e557ada0e38f2e52f126e54240b2576c83c4196cd2
python hackcmd.py 679ce12554e557ada0e38f2e52f126e54240b2576c83c4196cd2 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf text
crypto{x0r_i5_ass0c1at1v3}

</pre>       
    that last result is flag
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">crypto{x0r_i5_ass0c1at1v3}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for xor two hex</p>
</body>
</html>

