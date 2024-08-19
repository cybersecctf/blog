 

<!DOCTYPE html>
<html>
<title>tryhackme---Task 3 why is Encryption important?Writeup </title> 
<body>
    <h1>tryhackme---Task 3 why is Encryption important?Writeup </h1>

    <h2>Challenge Description</h2>
    <p> Cryptography is used to protect confidentiality, ensure integrity, ensure authenticity. You use cryptography every day most likely, and you’re almost certainly reading this now over an encrypted connection.

When logging into TryHackMe, your credentials were sent to the server. These were encrypted, otherwise someone would be able to capture them by snooping on your connection.

When you connect to SSH, your client and the server establish an encrypted tunnel so that no one can snoop on your session.

When you connect to your bank, there’s a certificate that uses cryptography to prove that it is actually your bank rather than a hacker.

When you download a file, how do you check if it downloaded right? You can use cryptography here to verify a checksum of the data.

You rarely have to interact directly with cryptography, but it silently protects almost everything you do digitally.

Whenever sensitive user data needs to be stored, it should be encrypted. Standards like PCI-DSS state that the data should be encrypted both at rest (in storage) AND while being transmitted. If you’re handling payment card details, you need to comply with these PCI regulations. Medical data has similar standards. With legislation like GDPR and California’s data protection, data breaches are extremely costly and dangerous to you as either a consumer or a business.

DO NOT encrypt passwords unless you’re doing something like a password manager. Passwords should not be stored in plaintext, and you should use hashing to manage them safely.
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>after using binawalk and exiftool not working using 

<pre>
import blog

import os,subprocess
def solve( search,file):

   return blog.solveup("search json",search,file)

if __name__ == "__main__" :
  print(solve("What does SSH stand for?","sol.json"))
  print(solve("How do webservers prove their identity?","sol.json"))
  print(solve("What is the main set of standards you need to comply with if you store or process payment card details?","sol.json"))
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">PCI-DSS
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for intro encryption</p>

</body>
</html>
