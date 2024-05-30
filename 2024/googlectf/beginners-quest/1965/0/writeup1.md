
<!DOCTYPE html>
<html>

<body>
    <h1>google ctf begginer quest-  1965 -0</h1>

    <h2>Challenge Description</h2>
    <p>  
An array and a loop helped to hide a flag, can 
you reverse this to get the flag?
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
    we open this <a href="https://cybersecctf.github.io/blog/2024/googlectf/beginners-quest/1965/1965-source/LEVEL1-ATARI.BAS">file </a> related to this challenge .you can run basic codes but but in this challenge only need anlysis them and see description  analysis them .after that we can see that should reverse
only need reverse string at end of code
with this code
<pre>
 import blog
#python
def solve(s):
  print(s[::-1])
if __name__ == "__main__" :
  s=blog.set("MELBORP_A_EVLOS_OT_SDRAWKCAB_GNIKROW",1) 
  solve(s)
</pre>
for flag as this line say should wrap with FLAG
<pre>
020 PRINT "FLAG FORMAT: FLAG{[A-Z0-9_!]*}"
</pre>
and get final flag
 
<br>
    <h2>Flag</h2>
    <p class="flag">FLAG{WORKING_BACKWARDS_TO_SOLVE_A_PROBLEM}
</p>

    <h2>Conclusion</h2>
    <p>this is a     easy  chanllenge for  analysis basic code and reverse string in python</p>
</body>
</html>






