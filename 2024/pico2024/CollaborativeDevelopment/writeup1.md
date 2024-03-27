
<!DOCTYPE html>
<html>
<head>

</head>
<body>
    <h1>Collaborative Development-picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p>AUTHOR: JEFFERY JOHN

AUTHOR: JEFFERY JOHN

Description
My team has been working very hard on new features for our flag printing program! I wonder how they'll work together?
You can download the challenge files here:<a href="$wget https://artifacts.picoctf.net/c_titan/176/challenge.zip">challenge.zip</a>
</p>
ssh
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
 we shoudl see diffs on all branches and then merge each part and see flag.py in eachone to see all flag that is in three part this step we do
<pre>
 git diff feature/part-1 feature/part-2 feature/part-3
</pre>
and get flag
<pre>
┌──(kali㉿kali)-[~/…/2024/pico2024/CollaborativeDevelopment/drop-in]
└─$ git diff feature/part-1 feature/part-2 feature/part-3
diff --cc flag.py
index 7ab4e25,4672a5c..6e17fb3
--- a/flag.py
+++ b/flag.py
@@@ -1,3 -1,3 +1,2 @@@
  print("Printing the flag...")
--
- print("m@k3s_th3_dr3@m_", end='')
 -print("w0rk_2c91ca76}")
++print("picoCTF{t3@mw0rk_", end='')
</pre>
     </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">   picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_2c91ca76}
</p>

    <h2>Conclusion</h2>
    <p>this is a    easy chanllenge for work in github  and diff
</body>
</html>


