from pwn import *


# Calculate the input that will overwrite 'sus' with the desired value
input_value = p64(0x67616c66)
print(input_value)
