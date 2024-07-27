
 
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog

file1=blog.set("CTFLearn.pdf",1)
file2=blog.set("CTFLearn.txt",2)
# Read two files as byte arrays
file1_b = bytearray(open(file1, 'rb').read())
file2_b = bytearray(open(file2, 'rb').read())

# Set the length to be the smaller one
size = min(len(file1_b), len(file2_b))
xord_byte_array = bytearray(size)

# XOR between the files
for i in range(size):
    xord_byte_array[i] = file1_b[i] ^ file2_b[i]

# Write the XORed bytes to the output file
with open('output', 'wb') as output_file:
    output_file.write(xord_byte_array)

print("XOR operation completed and saved to output")
