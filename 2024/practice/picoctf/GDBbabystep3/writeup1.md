
<!DOCTYPE html>
<html>

<body>
    <h1>GDB baby step 3- picogym Exclusive</h1>

    <h2>Challenge Description</h2>
    <p> 
AUTHOR: LT 'SYREAL' JONES

Description
Now for something a little different. 0x2262c96b is loaded into memory in the main function. Examine byte-wise the memory that the constant is loaded in by using the GDB command x/4xb addr. The flag is the four bytes as they are stored in memory. If you find the bytes 0x11 0x22 0x33 0x44 in the memory location, your flag would be: picoCTF{0x11223344}.
Debug <a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/GDBbabystep3/debugger0_c">this</a>.
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
 we open debugger0_c in gdb and add this commands in step by step to find flag in that address 

<pre>
$wget https://phantom1ss.github.io/blog/2024/practice/picoctf/GDBbabystep3/debugger0_c(or from your picoctf problem)
$sudo chmod +x debugger0_c
gdb (--args) ./debugger0_c
gdb layout asm(for see asm codes)
gdb $b *(main+25)(becaouse is last location that address of 0x2262c96b and $rbp is stored  for watch later.
gdb x/4xb $rbp-4(in my computer for get flag)


</pre>
via this command<pre> gdb x/4xb $rbp-4 </pre>i get flag stored in $rbp-4 from memory  0x2262c96b 
 <img src=" https://phantom1ss.github.io/blog/2024/practice/picoctf/GDBbabystep3/blog.png" alt="location for break and value of address" class="inline"/>
</ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{0x6bc96222}
</p>

    <h2>Conclusion</h2>
    <p>this is a    easy chanllenge for work on reverse engineering on asm and $rbp and python and get dump file and watch rbp and memories value with gdb </p>
</body>
</html>









