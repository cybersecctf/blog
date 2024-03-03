
<!DOCTYPE html>
<html>
 
 
<body>
    <h1>picoctf 2019- strings it</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: SANJAY C/DANNY TUNITIS

Description
Can you find the flag in file without running it?
<a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/stringsit/strings">strings</a>
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
     i download strings file.it was elf file.execute it on linux say<code>Maybe try the 'strings' function? Take a look at the man page</code>strings is command in linux that like cat show content of file but unlike it have many command for search in file and flag and use for find flag in text or elf file more specially for larger files.
so i use this command<pre>$strings ./strings |grep 'pico'</pre>grep command search(grep) text in  file and becaouse of flag start with pico grep 'pico' and work in this example becaouse this executable file is large and can't find flag manually.
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{5tRIng5_1T_827aee91}</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for using linux strings and grep  command</p>
</body>
</html>

