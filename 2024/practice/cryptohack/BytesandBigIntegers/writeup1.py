#python
import base64, sys
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
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
                return f"The decoded string in {encoding} is: {ascii_value}" 
                return   ascii_value         
            except UnicodeDecodeError:
                return f"Unable to decode the string using {encoding}" 
    elif type == "hex":
         return bs.unhexlify(input_value) 
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
            return str(bs.hexlify(bytes(text))) 
             
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
 print(solve("encode","HELLO","hex"))
 print(solve("encode","HELLO","ascii"))