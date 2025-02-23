import paramiko
import time

# SSH Connection Details
host = "rhea.picoctf.net"
port = 63869   
username = "ctf-player"
password = "6abf4a82"

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
    cmd = input("ssh> ")
    if cmd.strip() == "$$exit":
        print("[+] Exiting SSH session.")
        break
    send_command(cmd)

# Close the connection
client.close()
