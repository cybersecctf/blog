<title>Chalkboard - ctflearn</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Chalkboard - ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> Solve the equations embedded in the jpeg to find the flag. Solve this problem before solving my Scope challenge which is worth 100 points.
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
we use 
<pre>$exiftool $1</pre>
on this image
 <img src=" https://cybersecctf.github.io/blog/2024/practice/ctflearn/Chalkboard/972.png" alt="ctf quetion image" class="inline"/>
and find this text
        <pre>
The flag for this challenge is of the form:..CTFlearn{I_Like_Math_x_y}..where x and y are the solution to these equations:..

3x + 5y = 31
7x + 9y = 59 
....
</pre>
and for solve this problem use this math
<pre>
21x+35y=217
-21x-27y=-177
8y=40
y=5
x=31-25/3=2
</pre>
and get flag with replace x y       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlearn{I_Like_Math_2_5}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on exiftool and math</p>
</body>
</html>


 