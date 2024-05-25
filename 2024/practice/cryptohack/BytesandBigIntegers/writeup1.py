#python
import base64, sys
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
from Crypto.Util.number import long_to_bytes, bytes_to_long
def int_to_bytes(val):
    return val.to_bytes((val.bit_length() + 7) // 8, 'big')
def solve(input_value,type,operation):
 if operation == "decode":
    if type == "ascii":
        bytes_value = bytes.fromhex(input_value)
        encodings = ['utf-8', 'latin1', 'ascii', 'cp1252']
        for encoding in encodings:
            try:
                ascii_value = bytes_value.decode(encoding)
                print(f"The decoded string in {encoding} is: {ascii_value}")
            except UnicodeDecodeError:
                print(f"Unable to decode the string using {encoding}")
    elif type == "long":
        try:
            num = int(input_value)
            message_bytes = long_to_bytes(num)
            message = message_bytes.decode('utf-8')
            print(message)
        except UnicodeDecodeError:
            print(f"Unable to decode the long integer to a message using utf-8")
    else:  # base64
        print(base64.b64decode(input_value).decode('utf-8'))
 else:  # encode
    if type == "ascii":
        print(input_value.encode('utf-8').hex())
    elif type == "long":
        print(bytes_to_long(input_value.encode('utf-8')))
    else:  # base64
        print(base64.b64encode(input_value.encode('utf-8')).decode('utf-8'))
if __name__ == "__main__" :
 input_value =blog.set("11515195063862318899931685488813747395775516287289682636499965282714637259206269",1)
 type = blog.set("long",2)
 operation =blog.set("decode",3)
 solve(input_value,type,operation)
 solve("dawood","ascii","encode")