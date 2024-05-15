import base64, sys
from Crypto.Util.number import long_to_bytes, bytes_to_long

def int_to_bytes(val):
    return val.to_bytes((val.bit_length() + 7) // 8, 'big')

print("-v value base64/ascii/long")
operation = "decode"  # default operation
type = "long"  # default type
input_value = "11515195063862318899931685488813747395775516287289682636499965282714637259206269"  # default input

if len(sys.argv) > 1:
    input_value = sys.argv[1]
if len(sys.argv) > 2:
    type = sys.argv[2]  # ascii/base64/long
if len(sys.argv) > 3:
    operation = sys.argv[3]  # encode/decode

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
