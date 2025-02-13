with open("chall.txt", "rb") as f:
    extended_flag = f.read().decode("iso8859-1")

# Step 2: Reverse the modification
original_flag = ""

for c in extended_flag:
    # Convert the character to its 8-bit binary representation
    o = bin(ord(c))[2:].zfill(8)
    print(o)
    # Replace the first '1' with '0' to undo the modification
    for i in range(8):
        if o[i] == "1":
            o = o[:i] + "0" + o[i + 1:]
            break
    print(o)
    # Convert the binary string back to a character
    original_flag += chr(int(o, 2))

# Step 3: Print the original flag
print(original_flag)