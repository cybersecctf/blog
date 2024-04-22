import os,sys
#FREQUENCY CAESAR CIPHER
def FCcipher(MESSAGE: str) -> str:
    
    if  os.path.isfile(message) :
     with open(message, 'r') as f:
        text = f.read()
    else:
            text=  message
    result = ''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    change =    'FCKHOSMYBVQUPLRTNIAJGEZWXD'
    for char in text:
        if char in alphabet:
            result += change[alphabet.index(char)]
        else:
            result += char
    return result

message = "ANSU{QEX_RJV_NVSOQVZ_GH_SIBF}"
if len(sys.argv)>1:
 message=sys.argv[1]

print(FCcipher(message))