
<!DOCTYPE html>
<html>

<body>
    <h1>Basic Injection- ctflearn</h1>

    <h2>Challenge Description</h2>
    <p>See if you can leak the whole database using what you know about SQL Injections. <a href="https://web.ctflearn.com/web4/">link</a>

Don't know where to begin? Check out CTFlearn's <a href="https://ctflearn.com/lab/sql-injection-part-1"> SQL Injection Lab</a>
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
     we open site
 <img src=" https://cybersecctf.github.io/blog/2024/ctflearn/BasicInjection/web.png" alt="image" class="inline"/>
see is input box vulunerable for sql injection as describe in challenge and site.
easy sql injection describe it here <a href="https://ctflearn.com/lab/sql-injection-part-1"> SQL Injection Lab-1</a>
       get from list in this site see that  <pre>'hello' or '1' = '1'  </pre> work as input and find all users and flag
     <img src=" https://cybersecctf.github.io/blog/2024/ctflearn/BasicInjection/alluser.png" alt="image" class="inline"/>
this challenge is about what happen if not use sanitiz3_inputs}    and sample in
Yes, you should always sanitize input data. Sanitation isn't just about protecting you from injection, but also to validate types, restricted value (enums), ranges, etc.. While an attacker might not be able to manipulate your sql, they can still cause undesired behavior in the rest of your application.and means check values have good and acceptable range like this ip check.if dont check ip can have values like null for easy sql injection
<pre>
<?php 
$ipaddr = "126.0.0.5"; 
  
if (!filter_var($ipaddr, FILTER_VALIDATE_IP) === false) { 
    echo("Valid IP-address"); 
} else { 
    echo("Invalid IP-address"); 
} 
?> 
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">: CTFlearn{th4t_is_why_you_n33d_to_sanitiz3_inputs}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on sql injection and web exploitation sanitiz inputs</p>
</body>
</html>




 
