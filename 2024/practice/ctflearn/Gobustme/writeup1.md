<title>Gobustme ?- ctflearn</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Gobustme ?- ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> Some ghosts made this site ?, it's a little spooky but theres a bunch of stuff hidden around.

gobustme.ctflearn.com
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
   i can't open this site like sites in web challenge probebly ctflearn hosting is down so
get writeups from here
<pre> $gobuster dir -u $1 -w $2</pre>
use site in $1 and wordlist in  $2 and find flag directory and flag or go to folder .
this is sample result of this command
<pre>
 gobuster dir -u https://gobustme.ctflearn.com -w /seclists/Discovery/Web-Content/common.txt
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     https://gobustme.ctflearn.com
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Timeout:                 10s
===============================================================
2023/07/15 13:08:26 Starting gobuster in directory enumeration mode
===============================================================
/.well-known/http-opportunistic (Status: 200) [Size: 32]
/call                 (Status: 301) [Size: 169] [--> http://gobustme.ctflearn.com/call/]
/carpet               (Status: 301) [Size: 169] [--> http://gobustme.ctflearn.com/carpet/]
/flag                 (Status: 301) [Size: 169] [--> http://gobustme.ctflearn.com/flag/]
/hide                 (Status: 301) [Size: 169] [--> http://gobustme.ctflearn.com/hide/]
/index.html           (Status: 200) [Size: 2713]
/sex                  (Status: 301) [Size: 169] [--> http://gobustme.ctflearn.com/sex/]
/shadow               (Status: 301) [Size: 169] [--> http://gobustme.ctflearn.com/shadow/]
/skin                 (Status: 301) [Size: 169] [--> http://gobustme.ctflearn.com/skin/]
Progress: 4712 / 4716 (99.92%)
===============================================================
2023/07/15 13:10:31 Finished
===============================================================                          
```

/flag directory looked more like it could be but /hide gave the flag
 
flag ```CTFlearn{gh0sbu5t3rs_4ever}```
</pre>
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlearn{gh0sbu5t3rs_4ever}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on brutforce directory with gobuster</p>
</body>
</html>

