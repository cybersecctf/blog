 

<!DOCTYPE html>
<html>
 
<body>
    <h1>Encryption Master--ctflearn  Writeup </h1>

    <h2>Challenge Description</h2>
    <p>  Alright. Serious talk. You need to work pretty hard for this one (unless you are an encryption god.) Well, good luck. https://mega.nz/#!iPgzXIiD!Pkza_S8YUxIXrZ7gdwMcIoufMzi_FjSio3Vx9GuL0ok
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>this is maybe easier than hard but help understand and run 
              base2 and base64 and hex hard problems easier 
            with run this code can get flag                               

<pre>
import blog
import binascii

import os,subprocess
def base2(s, chars=['20', '30', '31'], operation="decode"):
    if operation == "decode":
        # Decoding logic
        d = []
        for i in range(0, len(s) - 1, 2):
            x = s[i:i + 2]
            if x == chars[0]:
                d.append('|')
            elif x == chars[1]:
                d.append('0')
            elif x == chars[2]:
                d.append('1')

        text = "".join(d)
        binary_string = text.split("|")
        p = []
        for x in binary_string:
            if x != '':
                # Convert binary to integer
                decimal_value = int(x, 2)
                # Convert integer to ASCII character
                p.append(chr(decimal_value))
        return "".join(p)

    elif operation == "encode":
        # Encoding logic
        encoded_string = []
        for char in s:
            # Convert ASCII character to binary
            binary_string = format(ord(char), '08b')
            for bit in binary_string:
                if bit == '0':
                    encoded_string.append(chars[1])
                elif bit == '1':
                    encoded_string.append(chars[2])
            # Append separator after each character's binary representation
            encoded_string.append(chars[0])

        return "".join(encoded_string)
def solve(s,type="base64 decode",chars=['20', '30', '31']):
  if type=="base64 decode":
        return blog.solveup("base64 decode","decode",s)  
  elif type=="base64 encode":
        return blog.solveup("base64 decode","encode",s)  
  elif type=="base2 decode":
        return base2(s, chars, operation="decode")
  elif type=="hex decode":
        return blog.solveup("cryptohack hex", "decode",s )
  elif type=="hex encode":
        return  blog.solveup("cryptohack hex", "encode",s )
def main(file,type="base64 decode"):
    s=blog.solveup("read file",file,"")
    
    if type=="base64 decode":
        return blog.solveup("base64 decode","decode",s)      
    s=blog.solveup("base64 decode","decode",s)

               
    s=s.replace(b"Nice! Now keep going. 54776f206d6f72652e",b"").decode()
    print(solve("54776f206d6f72652e","hex decode"))
    s=base2(s)   
    s=s.replace("Final Decryption! ","")
    s=blog.solveup("base64 decode","decode",s)
    return s
def find_valid_hex_string(hex_string):
    while len(hex_string) > 0:
        try:
            decoded_bytes = binascii.unhexlify(hex_string)
            decoded_string = decoded_bytes.decode("utf-8")
            return decoded_string
        except UnicodeDecodeError:
            # Remove the last character and try again
            hex_string = hex_string[:-1]

    return "Unable to find a valid string."
 

    return hex_string      

if __name__ == "__main__" :
  print("d",main("flag.txt",""))
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTF{I_AM_PROUD_OF_YOU}
</p>

    <h2>Conclusion</h2>
    <p>this is a medium chanllenge for work on base 2 and base 64 and hex</p>

</body>
</html>
