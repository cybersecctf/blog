<!DOCTYPE html>
<html>
<head>
    <title>
picopractice(2021)- Nice netcat...Challenge Writeup
</title>
</head>
<body>
    <h1>picopractice(2021)- Nice netcat...Challenge Writeup</h1>

    <h2>Challenge Description</h2>
    <p>AUTHOR: SYREAL

Description
There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 22902, but it doesn't speak English...
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        <li>use command $nc mercury.picoctf.net 22902>flag for run netcat and save content in flag file</li>
        <li>this is decimal number in every line can be asci code of characters so use this code for get char from decimal
  </li>
<li> <pre>
import blog
import os
def solve(x):
 if os.path.exists(x):
  x=open(x).read().strip()
 s=''.join(chr(int(s)) for s in x.split())
 return s
if __name__ == "__main__" :
 print(solve("flag"))
 print(solve("65 78"))#test execute
</pre> and yes get flag start with pico
</li>
      
    </ol>

    <h2>Flag</h2>
    <p class="flag">picoCTF{g00d_k1tty!_n1c3_k1tty!_d3dfd6df}</p>

    <h2>Conclusion</h2>
    <p>easy ctf for cryptography and decimal to ascii convertor  with  python code</p>
</body>
</html>
