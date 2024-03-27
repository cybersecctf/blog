<!DOCTYPE html>
<html>

<body>
    <h1>CanYouSee-picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: MUBARAK MIKAIL

Description
How about some hide and seek?
Download this file  <a href="https://artifacts.picoctf.net/c_titan/4/unknown.zip">here</a>.
 
</p>
merge
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
we unzip file and see image inside it and use exiftool and see a abse64 text inside Attribution URL parameter.decode it and get flag 
        <pre>
$wget https://artifacts.picoctf.net/c_titan/4/unknown.zip
$unzip unknown.zip
$exiftool ukn_reality.jpg
$echo 'cGljb0NURntNRTc0RDQ3QV9ISUREM05fZGVjYTA2ZmJ9Cg==' |base64 -d  
</pre>
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{ME74D47A_HIDD3N_deca06fb}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on image and exiftool and base64 and forensics</p>
</body>

 