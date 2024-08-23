<title>WOW.... So Meta- ctflearn</title>
<!DOCTYPE html>
<html>

<body>
    <h1>WOW.... So Meta- ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> This photo was taken by our target. See what you can find out about him from it. https://mega.nz/#!ifA2QAwQ!WF-S-MtWHugj8lx1QanGG7V91R-S1ng7dDRSV25iFbk
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
     we open this image <img src=" https://cybersecctf.github.io/blog/2024/practice/ctflearn/WOWSoMeta/pic.jpg" alt="image" class="inline"/>
becaouse meta use exiftool
<pre>
#python
import blog
import os
def solve(file):
 os.system(f"exiftool "+file)
if __name__ == "__main__" :
 solve("Ai")
</pre>
      that is getting from https://cybersecctf.github.io/blog/2023/practice/picoctf/information/writeup1.md
with parmeters <pre>pic.jpg</pre> and picture of this problem and meta of photo that have flag

    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag"> flag{EEe_x_I_FFf}

</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for use exiftool and forensics</p>
</body>
</html>


