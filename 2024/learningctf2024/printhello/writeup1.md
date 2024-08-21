
<!DOCTYPE html>
<html>
<body>
<title>Picker III- picoGym Exclusive</title>

<h2>Challenge Description</h2>
<p> AUTHOR: LT 'SYREAL' JONES

AUTHOR: LT 'SYREAL' JONES

Description
Can you figure out how this program works to get the flag?
Additional details will be available after launching your challenge instance.
------------------------------------------------------------------------------
 Connect to the program with netcat:
$ nc saturn.picoctf.net 50824
The program's source code can be downloaded <a href="https://artifacts.picoctf.net/c/525/picker-III.py">here</a>.
</p>

<h2>Solution Approach</h2>
<p>Here are the steps we took to solve the challenge:</p>
<ol>
we open source code and see that like <a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/PickerI/writeup1.md">picker-I</a>win function
print flag but unlike it win isn't accessible and have new accessible functions so have to write win inside func_table that is accessible via choice
and modify this part
<pre>
# This table is formatted for easier viewing, but it is really one line
  func_table = \
'''\
print_table                     \
read_variable                   \
write_variable                  \
getRandomNumber                 \
'''
.....
</pre>
via write function and exec that can modify it
<pre>
def write_variable():
  var_name = input('Please enter variable name to write: ')
  if( filter_var_name(var_name) ):
    value = input('Please enter new value of variable: ')
    if( filter_value(value) ):
      exec('global '+var_name+'; '+var_name+' = '+value)
    else:
      print('Illegal value')
  else:
    print('Illegal variable name')
</pre>
but this code say that it has some condition
<pre>
FUNC_TABLE_SIZE = 4
FUNC_TABLE_ENTRY_SIZE = 32
CORRUPT_MESSAGE = 'Table corrupted. Try entering \'reset\' to fix it'
def check_table():
  global func_table

  if( len(func_table) != FUNC_TABLE_ENTRY_SIZE * FUNC_TABLE_SIZE):
    return False
  return True
def get_func(n):
  global func_table
  # Check table for viability
  if( not check_table() ):
    print(CORRUPT_MESSAGE)
    return
  # Get function name from table
  func_name = ''
  func_name_offset = n * FUNC_TABLE_ENTRY_SIZE
  for i in range(func_name_offset, func_name_offset+FUNC_TABLE_ENTRY_SIZE):
    if( func_table[i] == ' '):
      func_name = func_table[func_name_offset:i]
      break

  if( func_name == '' ):
    func_name = func_table[func_name_offset:func_name_offset+FUNC_TABLE_ENTRY_SIZE]
  
  return func_name
</pre>
after some try and get error find this input  "win and add it in length of func_table like image below can get flag.
<img src=" https://phantom1ss.github.io/blog/2024/practice/picoctf/PickerIII/plickeriii.png" alt="plickeriii" class="inline"/>
but flag is in hex. convert it to text with   code in this <a href="https://phantom1ss.github.io/blog/?q=hex">writeup</a> and get real flag
</pre>
</ol>
<br>
<h2>Flag</h2>
<p class="flag">picoCTF{7h15_15_wh47_w3_g37_w17h_u53r5_1n_ch4rg3_a186f9ac}

<h2>Conclusion</h2>
<p>this is a very easy challenge for work on reverse engineering with python and bypass filter input and modify then</p>
</body>
</html>


 
<a href="https://phantom1ss.github.io/blog/?q=hex">writeup</a>