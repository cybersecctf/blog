
<!DOCTYPE html>
<html>

<body>
    <h1>GDB baby step 4- picogym Exclusive</h1>

    <h2>Challenge Description</h2>
    <p> 
main calls a function that multiplies eax by a constant. The flag for this challenge is that constant in decimal base. If the constant you find is 0x1000, the flag will be picoCTF{4096}.
Debug  

Debug <a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/GDBbabystep4/debugger0_d">this.</a>
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
we download file from  picocft or my site 
 and  use this command to open gdb and see  assembly dump files
<p id="code1">
$wget https://phantom1ss.github.io/blog/2024/practice/picoctf/GDBbabystep3/debugger0_c(or from your picoctf problem)
$sudo chmod +x debugger0_c
gdb (--args) ./debugger0_c
gdb layout asm(for see asm codes)
</p>

 <img src=" https://phantom1ss.github.io/blog/2024/practice/picoctf/GDBbabystep4/gdb.png" alt="ctf quetion image" class="inline"/>
in asm in the line  <pre> imul $0x3269,$eax,$eax</pre> from code
 0x3269 is  flag and after convert  it to decimal .
</ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{12905}
</p>

 
    <h2>Conclusion</h2>
    <p>this is a    easy chanllenge for work on reverse engineering on asm and $rbp and python and get dump file and watch rbp and memories value with gdb </p>
</body>
</html>










