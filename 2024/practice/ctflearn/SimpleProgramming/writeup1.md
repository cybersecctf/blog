
<!DOCTYPE html>
<html>

<body>
    <h1>Simple Programming
- ctflearn</h1>

    <h2>Challenge Description</h2>
    <p>Can you help me? I need to know how many lines there are where the number of 0's is a multiple of 3 or the numbers of 1s is a multiple of 2. Please! Here is the file: https://mega.nz/#!7aoVEKhK!BAohJ0tfnP7bISIkbADK3qe1yNEkzjHXLKoJoKmqLy
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
this is programing language can do solve in any language on base of your desire but
here use python and get flag
<pre>
#python
import sys
file="data.dat"
if len(sys.argv)>1:
    file=sys.argv[1]
count=0
with open("data.dat","r") as f:
     lines=f.readlines()
for line in lines:
 if line.count('0')%3==0 or line.count('1')%2==0:
   count+=1
print(count)
</pre>
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">flag{6662}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for learn  programming and read lines from file and count 1 0s</p>
</body>
</html>

