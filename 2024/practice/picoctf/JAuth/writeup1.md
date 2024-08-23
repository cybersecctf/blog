<title>JAuth- picoGym Exclusive</title>

<!DOCTYPE html>
<html>
 
<body>
    <h1>JAuth- picoGym Exclusive</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: LT 'SYREAL' JONES

AUTHOR: GEOFFREY NJOGU

Description
Most web application developers use third party components without testing their security. Some of the past affected companies are:
Equifax (a US credit bureau organization) - breach due to unpatched Apache Struts web framework CVE-2017-5638
Mossack Fonesca (Panama Papers law firm) breach - unpatched version of Drupal CMS used
VerticalScope (internet media company) - outdated version of vBulletin forum software used
Can you identify the components and exploit the vulnerable one?
The website is running <a href="http://saturn.picoctf.net:55824/">here</a> Can you become an admin?
You can login as test with the password Test123! to get started.
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
      we have two hints in thiws problem:1-Use the web browser tools to check out the JWT cookie.2-The JWT should always have two (2) . separators.

so To start we go  to the developer tools, then application, the cookies to see the cookies for the site. After logging in with the test credentials a new JWT (JSON Web Token) cookie.

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRoIjoxNzEwMjY1OTYwNzgwLCJhZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjIuMC4wLjAgU2FmYXJpLzUzNy4zNiIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNzEwMjY1OTYxfQ.6cHAYnlRorNDexJLh7ACtaMg49rI7qdX0ZS7A6uB7Cw


The . is the seperator so it can be seen that there are three parts. First being the header, then the payload, then lastly the signature. Since they are in base64 it could be decoded with CyberChef.

Part 1:

Base64: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9

Decoded: {"typ":"JWT","alg":"HS256"}

Part 2:

Base64: eyJhdXRoIjoxNzA5NjE3NTUzMDg4LCJhZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjIuMC4wLjAgU2FmYXJpLzUzNy4zNiIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNzA5NjE3NTUzfQ

Decoded: {"auth":1709617553088,"agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36","role":"user","iat":1709617553}

Part 3:

Base64:6cHAYnlRorNDexJLh7ACtaMg49rI7qdX0ZS7A6uB7Cw

Decoded:byQC{K Wє,

The last part is hashed (HS256) which is why it outputs a weird value.

By taking the second part's decoded version and putting it into cyberchef to encode while changing the role from user to admin you can get a changed cookie value. For the first part you have the alg set to HS256 which is what creates the third part. By setting that to none we then don't have to worry about the third part and could leave it blank. So just take the first part's decoded output and change HS256 to none then re-encode with base64.

By then reconstructing and putting the parts back together you can get the full JWT cookie back with admin role. Be careful to remove any "=" padding with base64 because it is ignored with JWT tokens.

 

When you change the cookie value to the modified cookie and refresh the page you get the flag.
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{4_d14m0nd_1n_7h3_r0ugh_6e04440d}

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for web exploitation and third party components </p>
</body>
</html>




