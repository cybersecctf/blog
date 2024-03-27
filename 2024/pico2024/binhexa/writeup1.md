
<!DOCTYPE html>
<html>
 
<body>
    <h1>binhexa-picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p>AUTHOR: NANA AMA ATOMBO-SACKEY

Description
How well can you perfom basic binary operations?
Start searching for the flag here nc titan.picoctf.net 49152
</p>
ssh
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
we run netcat want doing operations in binary and convert final result in quetion6 to hex
 <img src=" https://phantom1ss.github.io/blog/2024/pico2024/binhexa/netcat.png" alt="netcat" class="inline"/>
  this is  the python code for doing binary operations and convert final result to hex as quetions want in netcat 
<pre>
binary_num1 = '10000010'
binary_num2 = '10000011'
# Convert binary numbers to integers
num1 = int(binary_num1, 2)
num2 = int(binary_num2, 2)

# Perform the operation
result = num2 >> 1

# Convert the result back to binary
binary_result = bin(result)[2:]  # [2:] to remove the '0b' prefix

# Display the result
print("Binary result:", binary_result)
print(hex(int(binary_result, 2)))
</pre>
 and will get flag after quetion6
     </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">  picoCTF{b1tw^3se_0p3eR@tI0n_su33essFuL_675602ae}

</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for doing binary operation in python and convert binary to hex
</body>
</html>


