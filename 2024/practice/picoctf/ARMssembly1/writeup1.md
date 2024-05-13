
<!DOCTYPE html>
<html>

<body>
    <h1>ARMssembly 1- picoctf2021</h1>

    <h2>Challenge Description</h2>
    <p>AUTHOR: PRANAY GARG

Description
For what argument does this program print `win` with variables 79, 7 and 3? File: <a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/ARMssembly1/chall_1.S">chall_1.S</a> Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
 we open code and analysis it in this way 
<pre>
  .arch armv8-a
    .file    "chall_1.c"
    .text
    .align    2
    .global    func
    .type    func, %function
func:
    sub    sp, sp, #32
    str    w0, [sp, 12]    [sp,12] =w0 input
    mov    w0, 79          w0=79  
    str    w0, [sp, 16]      [sp.16]=79
    mov    w0, 7               w0=7
    str    w0, [sp, 20]      [sp.20]=7
    mov    w0, 3                w0=3
    str    w0, [sp, 24]       [sp.24]=3 
    ldr    w0, [sp, 20]       w0=7
    ldr    w1, [sp, 16]         w1=79
    lsl    w0, w1, w0          w0=10112
    str    w0, [sp, 28]        [sp.28]=10112
    ldr    w1, [sp, 28]         w1=10112
    ldr    w0, [sp, 24]         w0=3
    sdiv    w0, w1, w0         w0=w1/w0=10112/3=3370   
    str    w0, [sp, 28]           [sp.28]=3370
    ldr    w1, [sp, 28]            w1=3370  
    ldr    w0, [sp, 12]            w0=x
    sub    w0, w1, w0           w0=3370-x
    str    w0, [sp, 28]            [sp.28]=w0 
    ldr    w0, [sp, 28]               
    add    sp, sp, 32
    ret
    .size    func, .-func
    .section    .rodata
    .align    3
.LC0:
    .string    "You win!"
    .align    3
.LC1:
    .string    "You Lose :("
    .text
    .align    2
    .global    main
    .type    main, %function
main:
    stp    x29, x30, [sp, -48]!
    add    x29, sp, 0
    str    w0, [x29, 28]
    str    x1, [x29, 16]
    ldr    x0, [x29, 16]
    add    x0, x0, 8
    ldr    x0, [x0]
    bl    atoi
    str    w0, [x29, 44]
    ldr    w0, [x29, 44]        
    bl    func               #get values and  calcualte them with function
    cmp    w0, 0          
    bne    .L4                 #if w0!=0 go to l4  and print loose else print ewin          w0 is 3370 
    adrp    x0, .LC0                   
    add    x0, x0, :lo12:.LC0
    bl    puts
    b    .L6
.L4:                  
    adrp    x0, .LC1         
    add    x0, x0, :lo12:.LC1
    bl    puts
.L6:
    nop
    ldp    x29, x30, [sp], 48
    ret
    .size    main, .-main
    .ident    "GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
    .section    .note.GNU-stack,"",@progbits

</pre>       
 linear   converting of it to python is:
<pre>
#python
>>s=(79<<7)/3

print(s,hex(int(s)))
</pre>
and convert result to 32 bit hex is our flag
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{00000d2a}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for  calculate and reverse enginering with asm</p>
</body>
</html>


