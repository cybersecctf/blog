
<!DOCTYPE html>
<html>

<body>
    <h1>speeds and feeds- picoctf2021</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: RYAN RAMSEYER

Description
There is something on my shop network running at nc mercury.picoctf.net 59953, but I can't tell what it is. Can you?
</p>
merge
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
we run netcat and see <a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/speedsandfeeds/file">content</a> of it that is gcode becaouse have many parts start with G and use for cnc and 3d printers. in gocode
<pre>
G17 is XY plane, G18 is XZ plane and G19 is YZ and GCODE start with one of them
</pre>
can search full defination in google or ai or <a href="https://www.cnczone.com/forums/g-code-programing/82663-g17-g18-g19-explanation-please.html">here</a>
but for find flag don't need to define every part of code just add to gcode simulator like <a href="https://ncviewer.com/">this</a> and watch flag

 <img src=" https://phantom1ss.github.io/blog/2024/practice/picoctf/speedsandfeeds/ncviewer.png" alt="ncviewer.com" class="inline"/>       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{num3r1cal_c0ntr0l_f3fea95b}

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on  reverse engineering in gcode</p>
</body>
</html>





