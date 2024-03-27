<!DOCTYPE html>
<html>

<body>
    <h1>WebDecode- picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: NANA AMA ATOMBO-SACKEY

Description
Do you know how to use the web inspector?
Start searching <a href="http://titan.picoctf.net:54494/">here</a> . to find the flag .
</p>
merge
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
 this is challenge for search in site and inspect pages for find flag .search it on find in <a href="http://titan.picoctf.net:54494/about.html">here</a> . to find the flag in base64.


 <img src=" https://phantom1ss.github.io/blog/2024/pico2024/WebDecode/chromeinspector.png" alt="chrome inspector" class="inline"/>
and use this  for convert base64 to text
<pre>
 $echo "cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMjgzZTYyZmV9"|base64 -d

</pre>
</p> 
 
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{web_succ3ssfully_d3c0ded_283e62fe}

</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for inspect web and convert base64 to text</p>
</body>

 

