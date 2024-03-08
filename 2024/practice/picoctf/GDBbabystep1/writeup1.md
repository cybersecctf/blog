
<!DOCTYPE html>
<html>

<body>
    <h1>GDB baby step 1- picogym Exclusive</h1>

    <h2>Challenge Description</h2>
    <p> 
AUTHOR: LT 'SYREAL' JONES

Description
Can you figure out what is in the eax register at the end of the main function? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Disassemble <a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/GDBbabystep1/debugger0_a">this</a>
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
 we download file this time we should take assembly dump from gdb or any debugger and not giving directly like <a href="https://phantom1ss.github.io/blog/?q=Bit-O-Asm-4">previous</a> competetion in picogym Exclusive.
for get assembly dump file of main with gdb use this commands:<pre>$gdb ./debugger0_a   then inside gdb type ) disassemble main</pre>     we get  this dump file  
<pre>
0x0000000000001129 <+0>:     endbr64
   0x000000000000112d <+4>:     push   %rbp
   0x000000000000112e <+5>:     mov    %rsp,%rbp
   0x0000000000001131 <+8>:     mov    %edi,-0x4(%rbp)
   0x0000000000001134 <+11>:    mov    %rsi,-0x10(%rbp)
   0x0000000000001138 <+15>:    mov    $0x86342,%eax
   0x000000000000113d <+20>:    pop    %rbp 
   0x000000000000113e <+21>:    ret
</pre>
as see in line<code>0x0000000000001138 <+15>:    mov    $0x86342,%eax</code>
value of eax is 0x86342 and after convert t o decimal  flag is found.
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{549698}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on reverse engineering on asm and eax and python and get dump file with gdb </p>
</body>
</html>





