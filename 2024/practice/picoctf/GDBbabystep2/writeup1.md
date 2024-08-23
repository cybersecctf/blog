<title>GDB baby step 2- picogym Exclusive</title>

<!DOCTYPE html>
<html>

<body>
    <h1>GDB baby step 2- picogym Exclusive</h1>

    <h2>Challenge Description</h2>
    <p> 
AUTHOR: LT 'SYREAL' JONES

Description
Can you figure out what is in the eax register at the end of the main function? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Debug <a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/GDBbabystep2/debugger0_b">this</a>.
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
 we download file and run it with gdb and watch value of eax with or calculate it manually like <a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/GDBbabystep1/writeup1.md">this writeup</a>
this is our steps in gdb
<pre>
┌──(kali㉿kali)-[~/…/2024/practice/picoctf/GDBbabystep2]
└─$ gdb ./debugger0_b
GNU gdb (Debian 13.2-1) 13.2
Copyright (C) 2023 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./debugger0_b...
(No debugging symbols found in ./debugger0_b)
(gdb) start
Temporary breakpoint 1 at 0x40110e
Starting program: /home/kali/Desktop/blog/2024/practice/picoctf/GDBbabystep2/debugger0_b 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Temporary breakpoint 1, 0x000000000040110e in main ()
(gdb) print $eax
$1 = 4198662
(gdb) n
Single stepping until exit from function main,
which has no line number information.
__libc_start_call_main (main=main@entry=0x401106 <main>, argc=argc@entry=1, argv=argv@entry=0x7fffffffde78) at ../sysdeps/nptl/libc_start_call_main.h:74
74      ../sysdeps/nptl/libc_start_call_main.h: No such file or directory.
(gdb) print $eax
$2 = 307019
(gdb) n
[Inferior 1 (process 35100) exited with code 0113]
(gdb) 
</pre>
and last value of eax before exiting is our flag <pre>$2 = 307019
</pre>
</ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{307019}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on reverse engineering on asm and eax and python and get dump file and watch eax with gdb </p>
</body>
</html>







