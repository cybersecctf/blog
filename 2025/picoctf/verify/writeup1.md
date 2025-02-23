<title>ctfzone2024---Shes the Real one  Writeup </title>
 

<!DOCTYPE html>
<html>
 
<body>
    <h1>Verify---picoctf2024 Writeup </h1>

    <h2>Challenge Description</h2>
    <p>  Description
People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.
ssh -p 50550 ctf-player@rhea.picoctf.net
Using the password 6abf4a82. Accept the fingerprint with yes, and ls once connected to begin. Remember, in a shell, passwords are hidden!
Checksum: b09c99c555e2b39a7e97849181e8996bc6a62501f0149c32447d8e65e205d6d2
To decrypt the file once you've verified the hash, run ./decrypt.sh files/<file>.
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>we can connect to ssh with this python code for connect ssh 
<pre>
 
import paramiko
import time
import os

# SSH Connection Details
host = "rhea.picoctf.net"
port = 65460     
username = "ctf-player"
password = "6abf4a82"

# Python script (to be executed remotely)
python_script = """
import os
os.system("ls")
os.system("whoami")
os.system("uname -a")
"""

# Connect to SSH
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=username, password=password)

# Open an interactive shell session
shell = client.invoke_shell()
print("[+] Connected to SSH. Type commands (or 'python sol.py' to run script). Type '$$exit' to quit.")

# Function to send a command to SSH
def send_command(command):
    shell.send(command + "\n")
    time.sleep(1)  # Wait for command execution
    output = shell.recv(65535).decode("utf-8")
    print(output)

# Interactive Loop
while True:
    cmd = input("ssh> ")  # Get user input
    
    if cmd.strip() == "$$exit":  # Exit condition
        print("[+] Exiting SSH session.")
        break
    elif cmd.strip() == "python sol.py":  # Run Python script remotely
        print("[+] Running sol.py remotely...")
        
        # Write the python script to a temporary file on the remote server
        remote_script_path = "/tmp/sol.py"
        sftp = client.open_sftp()
        with sftp.open(remote_script_path, 'w') as remote_file:
            remote_file.write(python_script)
        sftp.close()

        # Execute the Python script on the remote server
        stdin, stdout, stderr = client.exec_command(f"python3 {remote_script_path}")
        print(stdout.read().decode())  # Print script output
        print(stderr.read().decode())  # Print errors (if any)

        # Optionally, clean up the script file on the remote server
        client.exec_command(f"rm {remote_script_path}")

    else:  # Run normal commands
        # If we need to run `cd` and `ls` together:
        if "cd" in cmd:
            # Chain `cd` with `ls` in the same remote session
            send_command(f"{cmd} && ls")
        else:
            send_command(cmd)

# Close SSH connection
client.close()
print("[+] SSH session closed.")

</pre>
or simple send command with
<a href="https://cybersecctf.github.io/blog/2025/picoctf/writeup1.py">send command</a>
    </ol>
and get flag with run 
<code>
$for i in ./files/*; do ./decrypt.sh "$i"; done
</code>
or without using script connect ssh and run command above
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{trust_but_verify_451fd69b}
</p>

    <h2>Conclusion</h2>
    <p>this is a easy challemge for coonect ssh and run linux command on folder</p>

</body>
</html>
