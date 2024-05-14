import base64,sys
type="base64"
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
if len(sys.argv)>1:
  hex_string=sys.argv[1]
if len(sys.argv)>2:
  type=sys.argv[2]#ascii/base64
bytes_value = bytes.fromhex(hex_string)
encodings = ['utf-8', 'latin1', 'ascii', 'cp1252']
if type!="base64":
 for encoding in encodings:
    try:
        ascii_value = bytes_value.decode(encoding)
        print(f"The decoded string in {encoding} is: {ascii_value}")
    except UnicodeDecodeError:
        print(f"Unable to decode the string using {encoding}")
else:
 print(base64.b64encode(bytes_value))