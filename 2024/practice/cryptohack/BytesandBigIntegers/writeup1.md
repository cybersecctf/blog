<!DOCTYPE html>
<html>

<body>
    <h1>Bytes and Big Integers- cryptohack</h1>

    <h2>Challenge Description</h2>
    <p> Cryptosystems like RSA works on numbers, but messages are made up of characters. How should we convert our messages into numbers so that mathematical operations can be applied?

The most common way is to take the ordinal bytes of the message, convert them into hexadecimal, and concatenate. This can be interpreted as a base-16/hexadecimal number, and also represented in base-10/decimal.

To illustrate:

message: HELLO
ascii bytes: [72, 69, 76, 76, 79]
hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
base-16: 0x48454c4c4f
base-10: 310400273487

 Python's PyCryptodome library implements this with the methods bytes_to_long() and long_to_bytes(). You will first have to install PyCryptodome and import it with from Crypto.Util.number import *. For more details check the FAQ.


Convert the following integer back into a message:

11515195063862318899931685488813747395775516287289682636499965282714637259206269
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        <li> steps1 </li>
       we can use this script to decode/encode on asci/long/nase64 and get message
<pre>
#python
import base64, sys
import blog
from Crypto.Util.number import long_to_bytes, bytes_to_long
import binascii as bs
def int_to_bytes(val):
    return val.to_bytes((val.bit_length() + 7) // 8, 'big')
def solve(operation,input_value,type):
  try:
   if operation == "decode":
    if type == "ascii":
        bytes_value = bytes.fromhex(input_value)
        encodings = ['utf-8', 'latin1', 'ascii', 'cp1252']
        for encoding in encodings:
            try:
                ascii_value = bytes_value.decode(encoding)
                return f"The decoded string in {encoding} is:  {ascii_value}" 
                return   ascii_value         
            except UnicodeDecodeError:
                return f"Unable to decode the string using {encoding}" 
    elif type == "hex":
         s= bs.unhexlify(input_value) 
         return s.decode('utf-8') 
    elif type == "long":
        try:
            num = int(input_value)
            message_bytes = long_to_bytes(num)
            message = message_bytes.decode('utf-8')
            return message 
        except UnicodeDecodeError:
            return f"Unable to decode the long integer to a message using utf-8" 
        return base64.b64decode(input_value).decode('utf-8') 
   else:  # encode
    if type == "ascii":
        return [ord(c) for c in input_value] 
    elif type=="hex":
            text=input_value.encode()
            return bs.hexlify(bytes(text)).decode('utf-8')
             
    elif type == "long":
        return bytes_to_long(input_value.encode('utf-8')) 
    else:  # base64
        return base64.b64encode(input_value.encode('utf-8')).decode('utf-8') 
  except Exception as e:
    return f"error in  {operation} of {type} of {input_value} :{str(e)}" 
if __name__ == "__main__" :
 input_value =blog.set("11515195063862318899931685488813747395775516287289682636499965282714637259206269",1)
 type = blog.set("long",2)
 operation =blog.set("decode",3)
 print(solve(operation,input_value,type))
 print(solve("encode","HELLO","base64"))
 print(solve("encode","HELLO","long"))
 print(solve("decode","48454c4c4f","hex"))
 print(solve("encode","HELLO","ascii"))
 
</pre>
    and print flag
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}
</p>
 
    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for decode encodeon base64 asci long</p>
</body>
</html>

