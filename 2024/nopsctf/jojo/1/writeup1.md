<title>Jojo is missing!- N0PSctf2024</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Jojo is missing!- N0PSctf2024</h1>

    <h2>Challenge Description</h2>
    <p> We have received a message from Jojo, join our Discord server to read it: https://discord.com/invite/xqvnaGzG6x
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        <li> steps1 </li>
 we search on discord for flag in pinned message in annoncement  and see hex number 
and converted it to text via code below and get flag
<pre>
import blog
def solve(hex):
 print(blog.solveup("cryptohack hex","decode",hex))
if __name__ == "__main__" :
  hex=blog.set("49 66 20 61 6E 79 6F 6E 65 20 72 65 61 64 73 20 69 74 2C 20 49 20 61 6D 20 4A 6F 6A 6F 2E 20 49 20 68 61 76 65 20 62 65 65 6E 20 63 61 70 74 75 72 65 64 20 62 79 20 61 20 67 72 6F 75 70 20 63 61 6C 6C 65 64 20 4A 33 4A 75 4A 34 2E 20 50 6C 65 61 73 65 20 63 6F 6D 65 20 61 6E 64 20 73 61 76 65 20 6D 65 21 0A 4E 30 50 53 7B 4A 30 4A 30 5F 31 73 5F 6D 31 53 35 31 6E 47 21 7D",1)
 
  solve(hex)
</pre>
  
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">N0PS{J0J0_1s_m1S51nG!}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for convert hex to text</p>
</body>
</html>

