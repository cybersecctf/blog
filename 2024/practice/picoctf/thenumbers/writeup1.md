
<!DOCTYPE html>
<html>

<body>
    <h1>picoctf2019- The Numbers</h1>

    <h2>Challenge Description</h2>
    <p> The numbers... what do they mean?
numbers:https://jupiter.challenges.picoctf.org/static/f209a32253affb6f547a585649ba4fda/the_numbers.png
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        <li> open image see numbers in pictures start with 16 if add ascii of them with 96 get p so do others to see can get flag </li>
        <li>with this code and get flag</li>
<pre>
#python
import sys
numbers="16 9 3 15 3 20 6 20 8 5  14 21 13 2 5 18 19 13 1 19 15 14"
prefix=0 #change it to 96 for this problem
if len(sys.argv)>1:
 numbers=sys.argv[1]
if len(sys.argv)>2:
 prefix=sys.argv[2]
d=""
for x in numbers.split():
 d+=chr(int(x)+prefix)
print(d)
 </pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoctf{thenumbersmason}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for cryptography and convert decimal and asci to character with python</p>
</body>
</html>
