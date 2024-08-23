<title>Bit-O-Asm-2- picogym Exclusive</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Bit-O-Asm-2- picogym Exclusive</h1>

    <h2>Challenge Description</h2>
    <p> 
AUTHOR: LT 'SYREAL' JONES

Description
Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Download the assembly dump  <a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/Bit-O-Asm-2/disassembler-dump0_b.txt">here</a>
  
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        we open dump file from <a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/Bit-O-Asm-2/disassembler-dump0_b.txt">link</a>.it was like this<a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/Bit-O-Asm-1/writeup1.md">writeup</a> from this blog except that in this code<pre>
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    mov    eax,DWORD PTR [rbp-0x4]
<+25>:    pop    rbp
<+26>:    ret
</pre>
first 0x9fe1a value stored in DWORD and then DWORD stored in eax.like previous competetion        converted

with code<pre>print(int('0x9fe1a',16))</pre> and get value and stored 654874(result) it on flag
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{654874}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on reverse engineering on asm and eax</p>
</body>
</html>


