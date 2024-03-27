<!DOCTYPE html>
<html>

<body>
    <h1>ctf event- challengename Challenge Writeup(first save it)</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: SYREAL

Description
The Network Operations Center (NOC) of your local institution picked up a suspicious file, they're getting conflicting information on what type of file it is. They've brought you in as an external expert to examine the file. Can you extract all the information from this strange file?
Download the suspicious file <a href="https://artifacts.picoctf.net/c_titan/7/flag2of2-final.pdf">here</a>.
</p>
merge
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
this challenge is about find file correct type can use with file
and see is png file abd rename to png file with this commands.
we unzip file and see pdf file and open it and see second part of flag .
after use $file command see is png file.
then rename file to png and open it and see first part of flag.
        <pre>
$wget https://artifacts.picoctf.net/c_titan/7/flag2of2-final.pdf
$file flag2of2-final.pdf
$ mv  flag2of2-final.pdf flag2of2-finalpng.png
</pre>
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{f1u3n7_1n_pn9_&_pdf_53b741d6}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on image and exiftool and base64 and forensics</p>
</body>

 
