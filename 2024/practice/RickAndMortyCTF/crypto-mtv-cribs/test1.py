import sys
import re

def xor_strings(a, b):
    # Perform XOR operation byte by byte between strings a and b
    return bytes(x ^ y for x, y in zip(a, b))

def is_hex(s):
    # Regular expression to match hexadecimal characters
    hex_regex = re.compile(r'^[0-9a-fA-F]+$')
    return bool(hex_regex.match(s))

def main():
    encoded_A = "382d4332272d2d623d3c1a52632a28387f0921130b3d7d2b52632b2f785c"
    original_A = "4d59204641564f52495445205249434b2049532054494e59205249434b21"           
    if len(sys.argv) >= 3:
     encoded_A = sys.argv[1]
     original_A = sys.argv[2]

    # Convert hexadecimal strings to bytes objects if input arguments are hex
    if is_hex(encoded_A) and is_hex(original_A):
        encoded_A = bytes.fromhex(encoded_A)
        original_A = bytes.fromhex(original_A)
             
    # Convert ASCII strings to bytes objects
    else:
        
        print( "usaage:python ecoded_hex decoded_hex two pair xor see output.txt")
        return
       
    # Find key by XORing encoded and original strings
    key_A = xor_strings(encoded_A, original_A)

    # Decrypt encoded message using the found key
    decrypted_A = xor_strings(encoded_A, key_A)

    # XOR decrypted_A with encoded_A to get the flag
    flag = xor_strings(decrypted_A, encoded_A)
    
    # Debugging print statements
    print("Key (Hex):", key_A.hex())
    print("Key (String):", key_A.decode(errors='replace'))
    print("XOR Result (Hex):", flag.hex())
    print("XOR Result (String):", flag.decode(errors='replace'))

if __name__ == "__main__":
    main()

