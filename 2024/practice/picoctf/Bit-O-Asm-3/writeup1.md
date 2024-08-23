<title>Bit-O-Asm-3- picogym Exclusive</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Bit-O-Asm-3- picogym Exclusive</h1>

    <h2>Challenge Description</h2>
    <p> 
AUTHOR: LT 'SYREAL' JONES

Description
Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Download the assembly dump  <a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/Bit-O-Asm-3/disassembler-dump0_c.txt">here</a>
  
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        we open dump file from <a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/Bit-O-Asm-2/disassembler-dump0_b.txt">link</a>.it was like this<a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/Bit-O-Asm-2/writeup1.md">writeup</a> from this blog except that in this code<code>
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0xc],0x9fe1a
<+22>:    mov    DWORD PTR [rbp-0x8],0x4
<+29>:    mov    eax,DWORD PTR [rbp-0xc]
<+32>:    imul   eax,DWORD PTR [rbp-0x8]
<+36>:    add    eax,0x1f5
<+41>:    mov    DWORD PTR [rbp-0x4],eax
<+44>:    mov    eax,DWORD PTR [rbp-0x4]
<+47>:    pop    rbp
<+48>:    ret

</code>
this code have functio name endbr64 and get 0x9fe1a and multiply in 0x4 and add 0x1f5 to eax and get flag
 full code in python for do calculation in hex in this
<pre>
a=int("0x9fe1a",16)                       <+15>:    mov    DWORD PTR [rbp-0xc],0x9fe1a                       
b=int("0x4",16)                           DWORD PTR [rbp-0x8],0x4                                                                                        
a*=b                                      <+29>:    mov    eax,DWORD PTR [rbp-0xc]
<+32>:    imul   eax,DWORD PTR [rbp-0x8]
<+36>:    add    eax,0x1f5
                        
c=int("0x1f5",16)                <+36>:    add    eax,0x1f5                                
a+=c                                                               
print(a)                                                                 
                                                     
</pre>   
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{2619997}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on reverse engineering on asm and eax and python </p>
</body>
</html>


