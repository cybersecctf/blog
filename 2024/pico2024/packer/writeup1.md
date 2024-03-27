
<!DOCTYPE html>
<html>

<body>
    <h1>packer-picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: MUBARAK MIKAIL

Description
Reverse this linux executable?
<a href="https://artifacts.picoctf.net/c_titan/20/out">binary</a>
</p>
hex
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li> download file  and open it with ghidra but can't find anything on exports
 <img src=" https://phantom1ss.github.io/blog/2024/pico2024/packer/out.png" alt="ghidra out" class="inline"/>
 but hint say:
What can we do to reduce the size of a binary after compiling it.
so uset this command for reduce size of elf  
<pre>
    $upx -d out
</pre>
and open new file out1 with ghidra and see more function on export and open main function on it and see flag in hex

 <img src=" https://phantom1ss.github.io/blog/2024/pico2024/packer/out1.png" alt="ctf quetion image" class="inline"/>
conver hex to text with this code
<pre>
s=bytearray.fromhex("7069636f4354467b5539585f556e5034636b314e365f42316e34526933535f62646438343839337d").decode()
print(s)

</pre> and get real flag
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{U9X_UnP4ck1N6_B1n4Ri3S_bdd84893}
</p>
 
    <h2>Conclusion</h2>
    <p>this is a easy  chanllenge for reduce size of elf file and use in ghidra for get flag
</body>
</html>
hex


 
