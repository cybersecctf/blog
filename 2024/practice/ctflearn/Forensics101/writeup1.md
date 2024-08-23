<title>Forensics 101-ctflearn</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Forensics 101-ctflearn</h1>

    <h2>Challenge Description</h2>
    <p>Think the flag is somewhere in there. Would you help me find it? https://mega.nz/#!OHohCbTa!wbg60PARf4u6E6juuvK9-aDRe_bgEL937VO01EImM7c
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        we downloadifle and use this command and python code for find flag insided image 
<pre>
#python
import blog
#python
import subprocess,os

def solve(file, search=""):
    result=""
    if search!="":       
        result = subprocess.run(f"strings {file} | grep {search}", shell=True, text=True, capture_output=True)
    else:
           result = subprocess.run(f"strings {file}", shell=True, text=True, capture_output=True)          
    return result.stdout

if __name__ == "__main__":
    file=blog.set("file.jpg",1)
    search=blog.set("{",2)  #flag have '{' normally    
    print("d",solve("file.jpg", search))
</pre>
after run code above see text that have flag

</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">flag{wow!_data_is_cool}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge forforensics and get flag from file</p>
</body>
</html>

