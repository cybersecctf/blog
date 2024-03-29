
<!DOCTYPE html>
<html>
<head>
  <title>
</title> 
</head>
<body>
    <h1>picoctf2021- tunn3l v1s10n Challenge Writeup(first save it)</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: DANNY

Description
We found this file. Recover the flag.
https://mercury.picoctf.net/static/d0129ad98ba9258ab59e7700a1b18c14/tunn3l_v1s10n
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        <li>  in hints say Weird that it won't display right... it means something wrong in showing file</li>
        <li>exiftool say file is bmp but not showing so should modify with hex editor becaosue change extension not working</li>
            <img src=" https://phantom1ss.github.io/blog/2024/practice/picoctf/tunn3lv1s10n/pngbadhex.png" alt="png bad hex" class="inline"/>

    remove bad text in hex editor and convert them to 0 like this image and open <a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/tunn3lv1s10n/TUNELL2.bmp"> image</a> and get flag
 <img src=" https://phantom1ss.github.io/blog/2024/practice/picoctf/tunn3lv1s10n/pnghex.png" alt="png good hex" class="inline"/>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{QU1t3_a_V13w_2020}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on  hex editor and png files and forensics</p>
</body>
</html>




