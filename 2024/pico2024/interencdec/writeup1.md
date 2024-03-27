<!DOCTYPE html>
<html>

<body>
    <h1>interencdec- picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: JEFFERY JOHN
AUTHOR: NGIRIMANA SCHADRACK

Description
Can you get the real meaning from this file.
Download the file  <a href="https://artifacts.picoctf.net/c_titan/1/enc_flag">here</a> .
</p>
merge
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
  <pre>
$wget https://artifacts.picoctf.net/c_titan/1/enc_flag
$cat enc_flag
$echo "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgyeG9OakJzTURCcGZRPT0nCg=="|base64 -d
$echo "d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2g0N2o2azY5fQ=="|base64 -d
result is wpjvJAM{jhlzhy_k3jy9wa3k_h47j6k69}y

 
</pre>
use caesar ciipher in this <a href="https://www.dcode.fr/caesar-cipher">site</a> and get flag
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{caesar_d3cr9pt3d_a47c6d69}

</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for  cryptographpy and multiply convertion of base64 and caesar</p>
</body>

 


