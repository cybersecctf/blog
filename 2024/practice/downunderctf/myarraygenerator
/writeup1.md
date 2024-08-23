<title>my array generator---down under ctf 2024 </title>
 

<!DOCTYPE html>
<html>
 
<body>
    <h1>my array generator---down under ctf 2024 </h1>

    <h2>Challenge Description</h2>
    <p> The MAG cipher was a fast stream cipher algorithm submitted to the eSTREAM project of the eCRYPT network.
It was not selected for consideration in the second phase,
 as further cryptanalysis revealed a number of vulnerabilities including a distinguisher, 
partial-key recovery and in some variants a full key recovery.
 This challenge implements a weaker version of the MAG cipher with some security features removed.

Funnily enough, the wikipedia article got deleted just as 
I was writing this challenge due to a lack of notability.

Author: wednesday

<a href="https://github.com/cybersecctf/blog/blob/main/2024/practice/downunderctf/myarraygenerator
/challenge.py">challenge.py</a>
<a href="https://github.com/cybersecctf/blog/blob/main/2024/practice/downunderctf/myarraygenerator
/output.txt">output.txt</a>
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>after using binawalk and exiftool not working using 

<pre>
import blog

import os,subprocess
def solve(file, search=""):
    result=""
    if search!="":       
        result = subprocess.run(f"strings {file} | grep {search}", shell=True, text=True, capture_output=True)
    else:
           result = subprocess.run(f"strings {file}", shell=True, text=True, capture_output=True)          
    return result.stdout

if __name__ == "__main__" :
  print(solve("garden.jpg"))
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{more_than_m33ts_the_3y3657BaB2C}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on develper tools in in chrome and web exploitations</p>

</body>
</html>
