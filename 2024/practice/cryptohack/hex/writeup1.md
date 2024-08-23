<title>hex- cryptohack</title>
<!DOCTYPE html>
<html>

<body>
    <h1>hex- cryptohack</h1>

    <h2>Challenge Description</h2>
    <p>When we encrypt something the resulting ciphertext commonly has bytes which are not printable ASCII characters. If we want to share our encrypted data, it's common to encode it into something more user-friendly and portable across different systems.

Hexadecimal can be used in such a way to represent ASCII strings. First each letter is converted to an ordinal number according to the ASCII table (as in the previous challenge). Then the decimal numbers are converted to base-16 numbers, otherwise known as hexadecimal. The numbers can be combined together, into one long hex string.

Included below is a flag encoded as a hex string. Decode this back into bytes to get the flag.

63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
         we use this python code on abse of description for convert hex to ascii
<pre>
#python
import blog
import binascii 
def solve(operation, hexs): 
  if operation=="decode":
    return bytes.fromhex(hexs).decode('utf-8')
  if operation=="encode":
    return binascii.hexlify(hexs.encode('utf-8')).decode('utf-8')
    
if __name__ == "__main__" :
 hex=blog.set("63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d",1)
 print(solve("decode",hex))
</pre>
       and get flag that is ascii bytes only need text inside ''       b'crypto{You_will_be_working_with_hex_strings_a_lot}'

    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">crypto{You_will_be_working_with_hex_strings_a_lot}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for convert hex to ascii</p>
</body>
</html>

