<title>Bit-O-Asm-4- picogym Exclusive</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Bit-O-Asm-4- picogym Exclusive</h1>

    <h2>Challenge Description</h2>
    <p> 
AUTHOR: LT 'SYREAL' JONES

Description
Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Download the assembly dump  <a href="https://artifacts.picoctf.net/c/511/disassembler-dump0_d.txt">here</a>
  
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
we open assembly dump and watch it
<code>
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    cmp    DWORD PTR [rbp-0x4],0x2710
<+29>:    jle    0x55555555514e <main+37>
                        
<+31>:    sub    DWORD PTR [rbp-0x4],0x65
<+35>:    jmp    0x555555555152 <main+41>
<+37>:    add    DWORD PTR [rbp-0x4],0x65
<+41>:    mov    eax,DWORD PTR [rbp-0x4]
<+44>:    pop    rbp
<+45>:    ret
</code>

This code appears to be assembly code, likely part of a larger program or function. Let's break it down step by step:
<code>
endbr64: This instruction is used for control flow integrity. It's typically seen at the beginning of a function.

push rbp: This instruction pushes the value of the base pointer register rbp onto the stack.

mov rbp, rsp: This instruction moves the value of the stack pointer rsp into the base pointer rbp. This effectively sets up a stack frame for the current function.

mov DWORD PTR [rbp-0x14], edi: This moves the value of the edi register (which typically holds the first argument to a function in x86-64 calling conventions) into a memory location at rbp-0x14.

mov QWORD PTR [rbp-0x20], rsi: This moves the value of the rsi register (typically holds the second argument) into a memory location at rbp-0x20.

mov DWORD PTR [rbp-0x4], 0x9fe1a: This moves the immediate value 0x9fe1a into a memory location at rbp-0x4.

cmp DWORD PTR [rbp-0x4], 0x2710: This compares the value at memory location rbp-0x4 with 0x2710 (10000 in decimal).

jle 0x55555555514e <main+37>: If the comparison result indicates that the value at memory location rbp-0x4 is less than or equal to 0x2710, jump to the address 0x55555555514e (the label main+37).

sub DWORD PTR [rbp-0x4], 0x65: Subtract 0x65 (101 in decimal) from the value at memory location rbp-0x4.

jmp 0x555555555152 <main+41>: Unconditional jump to the address 0x555555555152 (the label main+41).

<+37>: add DWORD PTR [rbp-0x4], 0x65: If the comparison result in step 7 indicates that the value at memory location rbp-0x4 is greater than 0x2710, add 0x65 (101 in decimal) to the value at memory location rbp-0x4.

mov eax, DWORD PTR [rbp-0x4]: Move the value at memory location rbp-0x4 into the eax register.

pop rbp: Pop the value of the base pointer rbp from the stack, restoring the previous stack frame.

ret: This instruction returns control flow from the function, typically returning the value in the eax register.
</code>
so python code for it is like this
<pre>
rbp_minus_0x4 = 0x9fe1a
if rbp_minus_0x4 > 10000:
        rbp_minus_0x4 -= 0x65
else:
        rbp_minus_0x4 += 0x65#jle main jump if less equal and go here if less equal and previous if bigger


print(rbp_minus_0x4)
</pre>
run it and get flag or can calculate value without code manually in this problem
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{654773}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on reverse engineering on asm and eax and python </p>
</body>
</html>


