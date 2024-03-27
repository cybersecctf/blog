
<!DOCTYPE html>
<html>

<body>
    <h1>Unminify- picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p>   AUTHOR: ABRXS, PR1OR1TYQ

AUTHOR: JEFFERY JOHN

Description
I don't like scrolling down to read the code of my website, so I've squished it. As a bonus, my pages load faster!
Browse <a href="http://titan.picoctf.net:55033/">here</a> , and find the flag!
 
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
      we get flag from content of wepage with this command or see source of web in browser
<pre>
curl http://titan.picoctf.net:55033/|grep 'picoCTF{'
</pre>
  and get flag.flag is colored.
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{pr3tty_c0d3_51d374f0}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for get flag from content of site</p>
</body>
</html>

 
