<title>tryhackme---digital signature  Writeup </title>
 

<!DOCTYPE html>
<html>
 
<body>
    <h1>tryhackme---digital signature  Writeup </h1>

    <h2>Challenge Description</h2>
    <p> What's a Digital Signature?
Digital signatures are a way to prove the authenticity of files, to prove who created or modified them. Using asymmetric cryptography, you produce a signature with your private key and it can be verified using your public key. As only you should have access to your private key, this proves you signed the file. Digital signatures and physical signatures have the same value in the UK, legally.

The simplest form of digital signature would be encrypting the document with your private key, and then if someone wanted to verify this signature they would decrypt it with your public key and check if the files match.

Certificates - Prove who you are!
Certificates are also a key use of public key cryptography, linked to digital signatures. A common place where they’re used is for HTTPS. How does your web browser know that the server you’re talking to is the real tryhackme.com?

The answer is certificates. The web server has a certificate that says it is the real tryhackme.com. The certificates have a chain of trust, starting with a root CA (certificate authority). Root CAs are automatically trusted by your device, OS, or browser from install. Certs below that are trusted because the Root CAs say they trust that organisation. Certificates below that are trusted because the organisation is trusted by the Root CA and so on. There are long chains of trust. Again, this blog post explains this much better than I can. https://robertheaton.com/2014/03/27/how-does-https-actually-work/

You can get your own HTTPS certificates for domains you own using Let’s Encrypt for free. If you run a website, it’s worth setting it up.
try hack me verified by Cloudflare
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>this competetion need no code but if you want sign and verify files withpython use this code 
moidfied version  use in products

<pre>

import blog

import socket
import ssl
import pprint
 

def solve(hostname):
  try:
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
    conn.connect((hostname, 443))
    cert = conn.getpeercert()
    return cert
  except Exception as e:
     return str(e)


if __name__ == "__main__" :
  web=blog.set("tryhackme.com",1)
  pprint.pprint(solve(web))#better print with pprint and pretty print

</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">complete
</p>

    <h2>Conclusion</h2>
    <p>this is a medium chanllenge for sign files</p>

</body>
</html>
