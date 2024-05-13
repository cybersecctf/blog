
<!DOCTYPE html>
<html>

<body>
    <h1>ARMssembly 0-picoctf2021</h1>

    <h2>Challenge Description</h2>
    <p> What integer does this program print with arguments 182476535 and 3742084308? File:
<a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/ARMssembly0/chall.S">chall.S</a> Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        <li> steps1 </li> 
       we download file with this command or via link in blog<p ID="code1">
$wget  https://mercury.picoctf.net/static/39820b71cabc14033bca1f2db00a6801/chall.S
</p>
and open it.
<pre>
    .arch armv8-a
    .file    "chall.c"
    .text
    .align    2
    .global    func1
    .type    func1, %function
func1:
    sub    sp, sp, #16
    str    w0, [sp, 12]
    str    w1, [sp, 8]
    ldr    w1, [sp, 12]
    ldr    w0, [sp, 8]
    cmp    w1, w0
    bls    .L2
    ldr    w0, [sp, 12]
    b    .L3
.L2:
    ldr    w0, [sp, 8]
.L3:
    add    sp, sp, 16
    ret
    .size    func1, .-func1
    .section    .rodata
    .align    3
.LC0:
    .string    "Result: %ld\n"
    .text
    .align    2
    .global    main
    .type    main, %function
main:
    stp    x29, x30, [sp, -48]!
    add    x29, sp, 0
    str    x19, [sp, 16]
    str    w0, [x29, 44]
    str    x1, [x29, 32]
    ldr    x0, [x29, 32]
    add    x0, x0, 8
    ldr    x0, [x0]
    bl    atoi
    mov    w19, w0
    ldr    x0, [x29, 32]
    add    x0, x0, 16
    ldr    x0, [x0]
    bl    atoi
    mov    w1, w0
    mov    w0, w19
    bl    func1
    mov    w1, w0
    adrp    x0, .LC0
    add    x0, x0, :lo12:.LC0
    bl    printf
    mov    w0, 0
    ldr    x19, [sp, 16]
    ldp    x29, x30, [sp], 48
    ret
    .size    main, .-main
    .ident    "GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
    .section    .note.GNU-stack,"",@progbits

</pre>
    it print biggist number of of this two value in 32 bit hex that for this two number 
is 3742084308 and convert to 32bit hex via this python code
<pre>
decimal_number = 3742084308
hex_string = hex(decimal_number & 0xFFFFFFFF)  # Masking to ensure it's a 32-bit hex string
print(hex_string)#0xdf0bacd4
</pre> and remove 0x for get final flag
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">flag{df0bacd4}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for  reverse enginerring in asm and convert decimal to  32 bit  hex </p>
</body>
</html>

