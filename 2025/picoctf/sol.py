import paramiko
import time

# SSH Connection Details
host = "rhea.picoctf.net"  # Replace with your remote server host
port = 50550   # Replace with the appropriate port
username = "ctf-player"  # SSH Username
password = "6abf4a82"  # SSH Password

# Connect to SSH
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=username, password=password)

# Open a new channel for interactive shell session
shell = client.invoke_shell()

# Function to send a command and receive output
def send_command(command):
    shell.send(command + "\n")
    time.sleep(2)  # Give it time to process the command
    output = shell.recv(65535).decode("utf-8")  # Receive output
    print(output)  # Print the output for debugging
    return output

# Send the for loop command to execute on the remote server
loop_command = 'for i in ./files/*; do ./decrypt.sh "$i"; done'

# Send the loop command and capture the output
print("[+] Running command: ", loop_command)
output = send_command(loop_command)

# Print output (could be results of decryption or any errors)
print(f"[+] Command output:\n{output}")

# Close the SSH connection
client.close()
print("[+] SSH session closed.")
