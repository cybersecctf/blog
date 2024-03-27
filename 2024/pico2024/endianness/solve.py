from pwn import *

def find_little_endian(word):
    little_endian = word[::-1].hex()
    return little_endian

def find_big_endian(word):
    big_endian = ''.join(format(ord(char), '02X') for char in word)
    return big_endian

host = 'titan.picoctf.net'
port = 63093

conn = remote(host, port)
# Receive the initial prompt
conn.recvuntil("Word: ")
challenge_word = conn.recvline().strip().decode()  # Decode the received bytes to string
# Calculate little endian and big endian representations
little_endian = find_little_endian(challenge_word)
big_endian = find_big_endian(challenge_word)

# Send little endian representation
conn.sendline(little_endian)
print(conn.recvline().strip())  # Receive response

# Send big endian representation
conn.sendline(big_endian)
print(conn.recvline().strip())  # Receive response

# Receive and print the flag
flag = conn.recvall().strip()
print("Flag:", flag)
conn.close()
