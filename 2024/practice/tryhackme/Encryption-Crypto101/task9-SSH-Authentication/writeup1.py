
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog

import paramiko
import os
import subprocess
# Generate SSH keys
def runsh(command):
  d=[]
  result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=15)
  s=result.stdout.splitlines()
  for x in s:
   if x!="":
        d.append(x)
  return d
def generate_ssh_keys(key_name, passphrase=None):
    key = paramiko.RSAKey.generate(2048)
    private_key_path = os.path.expanduser(f"~/.ssh/{key_name}")
    public_key_path = f"{private_key_path}.pub"

    # Save private key
    key.write_private_key_file(private_key_path, password=passphrase)
    os.chmod(private_key_path, 0o600)  # Set permissions to 600

    # Save public key
    with open(public_key_path, 'w') as pub_file:
        pub_file.write(f"{key.get_name()} {key.get_base64()}")

    print(f"Keys generated: {private_key_path} (private), {public_key_path} (public)")

# Connect to a local host using SSH key
def ssh_connect_with_key(hostname, username, key_path, passphrase=None):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname, username=username, key_filename=key_path, passphrase=passphrase)
        print(f"Connected to {hostname} as {username}")
    except Exception as e:
        print(f"Failed to connect: {e}")
    finally:
        client.close()

def crackpassword(file):
  rockyou=blog.solveup("garden","locate rockyou.txt","/usr/share")
  john=blog.solveup("garden","locate ssh2john","bin")
  d=blog.solveup("garden",f"python {john} {file} >ssh.txt","")
  print("d",d)
  d=blog.solveup("garden",f"john ssh.txt --wordlist={rockyou}","")   
  return  d

def solve(q,val):
 print(val)  
 if q=="connect ssh":
  # Generate SSH keys
  generate_ssh_keys(key_name, passphrase) 
  # Add the public key to the authorized_keys file
  authorized_keys_path = os.path.expanduser("~/.ssh/authorized_keys")
  with open(f"{os.path.expanduser(f'~/.ssh/{key_name}.pub')}", 'r') as pub_key_file:
    pub_key = pub_key_file.read()
  with open(authorized_keys_path, 'a') as auth_keys_file:
    auth_keys_file.write(pub_key + "\n")
  # Connect to the local host using the generated key
  ssh_connect_with_key(hostname, username, os.path.expanduser(f"~/.ssh/{key_name}"), passphrase)
  return
 if q=="crack password":
     return crackpassword(val)
if __name__ == "__main__" :
 val=[""]*5
 q=blog.set("crack password",1)#or connect ssh
 val[0] = blog.set("id_rsa",2,"str") #or  server to connect
 val[1] = blog.set(os.getlogin(),3)  # Get the current logged-in user
 val[2] =blog.set( "your_passphrase",4)  # Optional
 val[3] = blog.set("my_ssh_key",5)
 print(solve(q,val[0]))
