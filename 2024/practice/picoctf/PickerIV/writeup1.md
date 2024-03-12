
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
in this code The user is prompted to enter a memory address in 

hexadecimal format.

The inputted value is read using scanf and stored in the variable 

val.

val is then interpreted as a function pointer and assigned to foo.

Finally, foo() is called, effectively causing the program to jump to 
the address provided by the user and execute whatever code is 

located there. 
so like <a href="https://phantom1ss.github.io/blog/?q=GDBbabystep4">this </a>we just   locate address of win with gdb with this command
<pre>
(gdb) --args picker-IV
(gdb) layout asm
</pre>
in asm code ,can  see win address
 <img src=" https://phantom1ss.github.io/blog/2024/practice/picoctf/PickerIV/gdbwinaddress.png" alt="gdb win address" class="inline"/>
and if enter it without hex , it jump to address of win and print flag
</ol>
<br>
<h2>Flag</h2>
<p class="flag">picoCTF{n3v3r_jump_t0_u53r_5uppl13d_4ddr35535_14bc5444}


<h2>Conclusion</h2>
<p>this is a very easy challenge for work on binary exploitation and ret2win</p>

</body>
</html>


 

