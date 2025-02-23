import paramiko
import time
from sol import *
# SSH Connection Details
host = "rhea.picoctf.net"
port = 58042
username = "ctf-player"
password = ""

# Connect to SSH
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=username, password=password)

# Open an interactive shell session
shell = client.invoke_shell()
print("[+] Connected to SSH. Type your commands (type '$$exit' to quit).")

# Function to send commands
def send_command(command):
     
    shell.send(command + "\n")
    time.sleep(1)  # Wait for output
    output = shell.recv(65535).decode("utf-8")
    print(output)

# Interactive Loop
while True:
    cmd = input("ssh> sol is"+sol())
    if cmd.strip() == "$$exit":
        print("[+] Exiting SSH session.")
        break
    cmd=sol()
    send_command(cmd)

# Close the connection
client.close()
