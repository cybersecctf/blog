<title>tryhackme---task9-Encryption and SSH authentication  Writeup </title>
 

<!DOCTYPE html>
<html>
 
<body>
    <h1>tryhackme---task9-Encryption and SSH authentication  Writeup </h1>

    <h2>Challenge Description</h2>
    <p> Encryption and SSH authentication
By default, SSH is authenticated using usernames and passwords in the same way that you would log in to the physical machine.

At some point, you’re almost certain to hit a machine that has SSH configured with key authentication instead. This uses public and private keys to prove that the client is a valid and authorised user on the server. By default, SSH keys are RSA keys. You can choose which algorithm to generate, and/or add a passphrase to encrypt the SSH key. ssh-keygen is the program used to generate pairs of keys most of the time.

SSH Private Keys
You should treat your private SSH keys like passwords. Don’t share them, they’re called private keys for a reason. If someone has your private key, they can use it to log in to servers that will accept it unless the key is encrypted.

It’s very important to mention that the passphrase to decrypt the key isn’t used to identify you to the server at all, all it does is decrypt the SSH key. The passphrase is never transmitted, and never leaves your system.

Using tools like John the Ripper, you can attack an encrypted SSH key to attempt to find the passphrase, which highlights the importance of using a secure passphrase and keeping your private key private.

When generating an SSH key to log in to a remote machine, you should generate the keys on your machine and then copy the public key over as this means the private key never exists on the target machine. For temporary keys generated for access to CTF boxes, this doesn't matter as much.

How do I use these keys?
The ~/.ssh folder is the default place to store these keys for OpenSSH. The authorized_keys (note the US English spelling) file in this directory holds public keys that are allowed to access the server if key authentication is enabled. By default on many distros, key authentication is enabled as it is more secure than using a password to authenticate. Normally for the root user, only key authentication is enabled.

In order to use a private SSH key, the permissions must be set up correctly otherwise your SSH client will ignore the file with a warning. Only the owner should be able to read or write to the private key (600 or stricter). ssh -i keyNameGoesHere user@host is how you specify a key for the standard Linux OpenSSH client.

Using SSH keys to get a better shell
SSH keys are an excellent way to “upgrade” a reverse shell, assuming the user has login enabled (www-data normally does not, but regular users and root will). Leaving an SSH key in authorized_keys on a box can be a useful backdoor, and you don't need to deal with any of the issues of unstabilised reverse shells like Control-C or lack of tab completion.

Answer the questions below
I recommend giving this a go yourself. Deploy a VM, like Linux Fundamentals 2 and try to add an SSH key and log in with the private key.
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>this a quetion for create ssh key in server with private key and public key
can do with this code too
and also answer quetions after code
<pre>
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
  blog.solveup("garden",f"python {john} {file} >ssh.txt","")

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
</pre>

    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">complete
</p>

    <h2>Conclusion</h2>
    <p>this is a easy chanllenge for connect with ssh</p>

</body>
</html>