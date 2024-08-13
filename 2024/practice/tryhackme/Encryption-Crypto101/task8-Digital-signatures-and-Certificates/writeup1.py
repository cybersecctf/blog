

import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
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

