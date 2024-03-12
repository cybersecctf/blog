
<!DOCTYPE html>
<html>
<body>
<h1>Picker IV- picoGym Exclusive</h1>

<h2>Challenge Description</h2>
<p> Description
Can you figure out how this program works to get the flag?
Additional details will be available after launching your challenge instance.
------------------------------------------------------------------------------
 Connect to the program with netcat:
$ nc saturn.picoctf.net 60667
The program's source code can be downloaded <a href="https://artifacts.picoctf.net/c/528/picker-IV.c">here</a>.
The Binary can be downloaded <a href="https://artifacts.picoctf.net/c/528/picker-IV">here</a>.
</p>
this challenge  
<h2>Solution Approach</h2>
<p>Here are the steps we took to solve the challenge:</p>
<ol>
 we have two file binary and source download them with this 
<p id="code1">
$wget https://artifacts.picoctf.net/c/528/picker-IV.c
$wget https://artifacts.picoctf.net/c/528/picker-IV
</p>
we run it just do it
<p id="code1">
/picker-IV
Enter the address in hex to jump to, excluding '0x': 65
You input 0x65
Segfault triggered! Exiting.

</p>
and not really convert hex. so open source
<p id="code1">
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>


void print_segf_message(){
  printf("Segfault triggered! Exiting.\n");
  sleep(15);
  exit(SIGSEGV);
}

int win() {
  FILE *fptr;
  char c;

  printf("You won!\n");
  // Open file
  fptr = fopen("flag.txt", "r");
  if (fptr == NULL)
  {
      printf("Cannot open file.\n");
      exit(0);
  }

  // Read contents from file
  c = fgetc(fptr);
  while (c != EOF)
  {
      printf ("%c", c);
      c = fgetc(fptr);
  }

  printf("\n");
  fclose(fptr);
}

int main() {
  signal(SIGSEGV, print_segf_message);
  setvbuf(stdout, NULL, _IONBF, 0); // _IONBF = Unbuffered

  unsigned int val;
  printf("Enter the address in hex to jump to, excluding '0x': ");
  scanf("%x", &val);
  printf("You input 0x%x\n", val);

  void (*foo)(void) = (void (*)())val;
  foo();
}

</p>
</ol>
<br>
<h2>Flag</h2>
<p class="flag">picoCTF{7h15_15_wh47_w3_g37_w17h_u53r5_1n_ch4rg3_a186f9ac}

<h2>Conclusion</h2>
<p>this is a very easy challenge for work on reverse engineering with python and bypass filter input and modify then</p>

</body>
</html>


 
<a href="https://phantom1ss.github.io/blog/?q=hex">writeup</a>