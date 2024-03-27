binary_num1 = '10000010'
binary_num2 = '10000011'
# Convert binary numbers to integers
num1 = int(binary_num1, 2)
num2 = int(binary_num2, 2)

# Perform the operation
result = num1<<1

# Convert the result back to binary
binary_result = bin(result)[2:]  # [2:] to remove the '0b' prefix

# Display the result
print("Binary result:", binary_result)
print(hex(int(binary_result, 2)))