
<!DOCTYPE html>
<html>

<body>
    <h1>Bit-O-Asm-1- picogym exclusive</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: LT 'SYREAL' JONES

Description
Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Download the assembly dump <a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/Bit-O-Asm-1/disassembler-dump0_a.txt">here</a>
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        open text file see this lines
<pre>
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x4],edi
<+11>:    mov    QWORD PTR [rbp-0x10],rsi
<+15>:    mov    eax,0x30
<+20>:    pop    rbp
<+21>:    ret
</pre>
in last line related to eax       see value is 0x30 that converted to   48 in decimal on base of

 descriptions of problem for generate flag.
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{48}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on  reverse engineering in x86-64 and asm</p>
</body>
</html>

