<title>Git Is Good- ctflearn</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Git Is Good- ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> The flag used to be there. But then I redacted it. Good Luck. 
<a href="https://cybersecctf.github.io/blog/2024/practice/ctflearn/GitIsGood/gitIsGood.zip">gitIsGood.zip</a>
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
         we download zip and extract git 
       use cat flag.txt see that flag is redacted so maybe in history of git can find it so use
<pre>
$git show
</pre>
    and see flag in result like below
<pre>
Good/gitIsGood$ cat flag.txt
flag{REDACTED}
....................:~/Desktop/blog/2024/practice/ctflearn/GitIsGood/gitIsGood$ git show
commit d10f77c4e766705ab36c7f31dc47b0c5056666bb (HEAD -> master)
Author: LaScalaLuke <lascala.luke@gmail.com>
Date:   Sun Oct 30 14:33:18 2016 -0400

    Edited files

diff --git a/flag.txt b/flag.txt
index 8684e68..c5250d0 100644
--- a/flag.txt
+++ b/flag.txt
@@ -1 +1 @@
-flag{protect_your_git}
+flag{REDACTED}
 ...............~/Desktop/blog/2024/practice/ctflearn/GitIsG
ood/gitIsGood$ 

</pre>

    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">flag{protect_your_git}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on git and show command</p>
</body>
</html>


