from pwn import *

def binary_search(conn):
    low = 1
    high = 1000

    while low <= high:
        mid = (low + high) // 2
        conn.recvuntil("Enter your guess: ")
        conn.sendline(str(mid))
        response = conn.recvline().strip().decode()
        print(response)

        if "Correct" in response:
            break
        elif "Higher" in response:
            high = mid - 1
        elif "Lower" in response:
            low = mid + 1

# SSH connection details
host = 'atlas.picoctf.net'
port = 59358
username = 'ctf-player'
password = '83dcefb7'

# Connect to the remote server via SSH
conn = ssh(host=host, port=port, user=username, password=password)

# Start the binary search
binary_search(conn)

# Close the SSH connection
conn.close()
