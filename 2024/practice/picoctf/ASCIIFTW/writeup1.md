
<!DOCTYPE html>
<html>
 <title>ASCII FTW- picogym exclusive</title>
<body>
    <h1>ASCII FTW- picogym exclusive</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: ABHISHEK AGARWAL

Description
This program has constructed the flag using hex ascii values. Identify the flag text by disassembling the program.
You can download the file from  <a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/ASCIIFTW/asciiftw">here</a>

</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
when run program say flag start with 0x70. s0
for disassembling the program we use ghidra and open it and search for 0x70 

because program say flag start with and ascii of it is 'p' ,first part of pico and flag
    <img src=" https://phantom1ss.github.io/blog/2024/practice/picoctf/ASCIIFTW/asciftwng.png" alt="ctf quetion image" class="inline"/>

       see a lot of hex like<code>0x700 x69 0x63 </code>that re our flag that 

started with hex 70 and 'p'(ascii of 0x70) and pico. Combine them manaually and 

get<code>7069636f4354467b41534349495f49535f454153595f5f37424344393731447d</code> and convert with any online tool like <a href="https://

www.rapidtables.com/convert/number/hex-to-ascii.html">this</a>

and get flag
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{ASCII_IS_EASY_7BCD971D}
</p>
    <h2>Conclusion</h2>
    <p>this is a    medium chanllenge for work on ghidra and convert hex to asci
</body>
</html>



