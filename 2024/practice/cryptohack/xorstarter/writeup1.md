
<!DOCTYPE html>
<html>

<body>
    <h1>XOR Starter- INTRODUCTION TO CRYPTOHACK</h1>

    <h2>Challenge Description</h2>
    <p>XOR is a bitwise operator which returns 0 if the bits are the same, and 1 otherwise. In textbooks the XOR operator is denoted by ⊕, but in most challenges and programming languages you will see the caret ^ used instead.

A    B    Output
0    0    0
0    1    1
1    0    1
1    1    0
For longer binary numbers we XOR bit by bit: 0110 ^ 1010 = 1100. We can XOR integers by first converting the integer from decimal to binary. We can XOR strings by first converting each character to the integer representing the Unicode character.

Given the string label, XOR each character with the integer 13. Convert these integers back to a string and submit the flag as crypto{new_string}.

 The Python pwntools library has a convenient xor() function that can XOR together data of different types and lengths. But first, you may want to implement your own function to solve this.
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
you can use this script with argument <code>python file.py label 13</code>
and get flag 
<pre>
#python
import ast
import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

if len(sys.argv)>1:
  ords=sys.argv[1]
  if ords.startswith("[") and ords.endswith("]") and "," in ords:
   ords= ast.literal_eval(ords)
  else:
    d=[]
    for x in ords:
      d.append(ord(x))
    ords=d

else:
  ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]
import blog 
hexs="0x32" 
type="int"
hexs=blog.set(0x32,1)
type=blog.set("int",2)
print(ords)
for x in ords:
  print(x)
print("Here is your flag:")
if type=="int":
   hexs=hex(int(hexs))
hexs = int(hexs, 16)
print("".join(chr(o ^ hexs) for o in ords))

</pre>
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">crypto{z3n_0f_pyth0n}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for xor string or integer list with number and integer</p>
</body>
</html>

