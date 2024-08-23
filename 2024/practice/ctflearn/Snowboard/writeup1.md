<title>Snowboard- ctflearn</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Snowboard- ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> Find the flag in the jpeg file. Good Luck!


 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
         this time we can't use exiftool or strings in file for get flag if use will get CTFlearn{CTFIsEasy!!!}
as flag that is fake but when use this command
<pre>$file $1</pre> with this image 
 <img src=" https://cybersecctf.github.io/blog/2024/practice/ctflearn/Snowboard/Snowboard.jpg" alt="ctf quetion image" class="inline"/>
    that describe info file can see this text<pre>Snowboard.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 300x300, segment length 16, comment: "CTFlearn{CTFIsEasy!!!}", comment: "Q1RGbGVhcm57U2tpQmFuZmZ9Cg==", Exif Standard: [TIFF image data, little-endian, direntries=8, manufacturer=Canon, model=Canon EOS 6D Mark II, xresolution=138, yresolution=146, resolutionunit=2, software=GIMP 2.10.6, datetime=2019:05:07 14:37:21], progressive, precision 8, 1200x800, components 3
</pre>
that is info of file and also base64 text that can be decode with code inside this <a href="https://cybersecctf.github.io/blog/2024/practice/ctflearn/QRCode/writeup1.md">writeup and get flag that is real</a>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlearn{SkiBanff}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for use file command</p>
</body>
</html>



