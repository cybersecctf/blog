
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
import sys,os
file="file.jpg"
search="{"#flag have '{' normally
if len(sys.argv)>1:
      file=sys.argv[1]
if len(sys.argv)>2:
      search=sys.argv[2]
os.system("strings "+file+"|grep "+search)
</pre>    
and find flag that is in uncommon format 
<pre>
L{2^
[P{!
{~T{@
we|C{
v{*{8
flag{wow!_data_is_cool}
AG{u
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

