
<!DOCTYPE html>
<html>

<body>
    <h1>Taking LS -ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> yJust take the Ls. Check out this zip file and I be the flag will remain hidden. https://mega.nz/#!mCgBjZgB!_FtmAm8s_mpsHr7KWv8GYUzhbThNn0I8cHMBi4fJQp8
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
we download zip file and search inside it and find password inside
<code>
TheFlag/The Flag/.ThePassword/ThePassword.txt
and open password protected pdf  with it and see flag
</code>
<pre>
#python
import os
# Replace 'your_zip_file.zip' and 'your_text' with your specific zip file and text
file="TheFlag.zip"
search=""
if len(sys.argv)>1:
   file=sys.argv[1]
if len(sys.argv)>2:
   search=sys.argv[2]
os.system("python solve.py  "+file+" "+search)

</pre>
       
    also can do <code>$ls -lah</code>on all  folders for find password
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">ABCTF{T3Rm1n4l_is_C00l}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge forsearch on zip file </p>
</body>
</html>

