
<!DOCTYPE html>
<html>
 
<body>
    <h1>Blame Game-picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p>AUTHOR: JEFFERY JOHN

Description
Someone's commits seems to be preventing the program from working. Who is it?
You can download the challenge files here:
challenge.zip:https://artifacts.picoctf.net/c_titan/72/challenge.zip
</p>
ssh
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
 this is like <a href="https://phantom1ss.github.io/blog/2024/pico2024/TimeMachine/writeup1.md">this</a> but you need search on logsw and find someone havn't 'important' work because this
<p id="code1">
┌──(kali㉿kali)-[~/…/2024/pico2024/BlameGame/drop-in]
└─$ git log                                 
commit 8cc3930896bb01ae046bc08c382bd30772918ff5 (HEAD -> master)
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:09:06 2024 +0000

    important business work

commit 6dbd8d326a2f0c9fe7f0011c8e60448b9accc6ff
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:09:06 2024 +0000

    important business work

commit 2e8970529c41058a68aae8bc04ef7a2d53ce0d8a
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:09:06 2024 +0000

    important business work

commit 135020e8b96565248b604cb42ae54e256e8fc48a
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:09:06 2024 +0000

    important business work

commit a95fbac033f190b3fb1066727ea01d7d4be362b5
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:09:06 2024 +0000

    important business work

commit e6b8b174bf1ce6361ff29096579d2752616cb6f2
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:09:06 2024 +0000

    important business work
..........
</p>
do search with this command and get flag
<pre>
$wget https://artifacts.picoctf.net/c_titan/66/challenge.zip
$unzip challenge.zip
$git log (see commits)
$ git log --invert-grep --grep='important'

in this competetion can see flag without git show
</pre>
and get flag
<pre>
                                                                 
┌──(kali㉿kali)-[~/…/2024/pico2024/BlameGame/drop-in]
└─$ git log --invert-grep --grep='important'

commit 0351e0474493168ca76441c24630c17554fd09ca
Author: picoCTF{@sk_th3_1nt3rn_d2d29f22}  <ops@picoctf.com>
Date:   Sat Mar 9 21:09:01 2024 +0000

    optimize file size of prod code

commit f3cec26cf7f80f91b5c3d1972f14dd4e9f97ec83
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:09:01 2024 +0000

    create top secret project

 </pre>
     </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">   picoCTF{@sk_th3_1nt3rn_d2d29f22}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work in github and commit history and search on it
</body>
</html>


