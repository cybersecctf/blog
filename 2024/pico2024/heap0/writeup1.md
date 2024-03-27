
<!DOCTYPE html>
<html>

<body>
    <h1>heap 0- picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p> 
AUTHOR: ABRXS, PR1OR1TYQ

Description
Are overflows just a stack concern?
Download the binary <a href="https://artifacts.picoctf.net/c_tethys/28/chall">here</a>.
Download the source <a href="https://artifacts.picoctf.net/c_tethys/28/chall">here</a>.
Additional details will be available after launching your challenge instance.


</p>
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
Heap0 is a vulnerable program that allows users to write data to their own personal block of data on the heap. It contains a buffer overflow vulnerability in the write_buffer() function, which can be exploited to overwrite critical variables stored on the heap.
The vulnerability arises from the lack of bounds checking in the write_buffer() function. This function allows users to input data without verifying if the input exceeds the allocated buffer size, leading to a buffer overflow condition.
Upon running the program, we are presented with a menu containing several options, including writing to the buffer, printing the heap, printing safe_var, and printing the flag.
We identified that our target variable is safe_var, which stores a critical value that determines whether the flag is printed.
Our plan is to overflow the buffer allocated for input_data in such a way that we overwrite safe_var with the address of the flag. This will trick the program into printing the flag when we choose the appropriate menu option.
 We crafted a payload consisting of padding bytes to reach the address of safe_var and then the address of the flag.
We chose the option to write to the buffer and inputted our crafted payload.
 We selected the option to print the flag, which triggered the check_win() function. Due to our successful exploitation, the program printed the flag.
Upon successfully triggering the exploitation, the program printed the flag, confirming our successful exploitation of the buffer overflow vulnerability.

this is what we do in terminal and get results after trigger inputs and get flag

   we download file
<p id="code1">
$wget https://artifacts.picoctf.net/c_tethys/13/chall
$wget https://artifacts.picoctf.net/c_tethys/13/chall.c
</p>
<pre>
┌──(kali㉿kali)-[~/…/blog/2024/pico2024/heap0]
└─nc tethys.picoctf.net 60127


Welcome to heap0!
I put my data on the heap so it should be safe from any tampering.
Since my data isn't on the stack I'll even let you write whatever info you want to the heap, I already took care of using malloc for you.

Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data   
+-------------+----------------+
[*]   0x55ffe36982b0  ->   pico
+-------------+----------------+
[*]   0x55ffe36982d0  ->   bico
+-------------+----------------+

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 2
Data for buffer: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAApico

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 4

YOU WIN
 

</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{my_first_heap_overflow_76775c7c}
</p>

    <h2>Conclusion</h2>
    <p>this is a    medium chanllenge for  binary exploitation and heap overflow vulnerability</p>
</body>
</html>


