<title>Simple Steganography-ctflearn</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Simple Steganography-ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> Think the flag is somewhere in there. Would you help me find it? hint-" Steghide Might be Helpfull"

<a href=" https://ctflearn.com/challenge/download/894">minions.jpg</a>
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        we open minion image 
        <img src=" https://cybersecctf.github.io/blog/2024/practice/ctflearn/SimpleSteganography/894" alt="ctf quetion image" class="inline"/>
and use exiftool no  flag but say <code>Keywords                        : myadmi</code> that mean should use it on steghide
<pre>
$steghide extract -sf $1 -p $2
</pre>
    and open raw.txt that is in <a href="https://cybersecctf.github.io/blog/2024/practice/ctflearn/base22the6/writeup1.md">base64</a> and convert it and remove /X00 and get flag
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlearn{this_is_fun}
</p>

    <h2>Conclusion</h2>
    <p>this is a    easy chanllenge for work on steghide and Simple Steganography </p>
</body>
</html>


 
