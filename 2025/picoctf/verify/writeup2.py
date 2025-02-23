import paramiko
import os
import scp  # Install with: pip install scp

# SSH Connection Details
host = "atlas.picoctf.net"
port = 61691 
username = "ctf-player"
password = ""
remote_file_path = "drop-in/flag.png"
local_file_path = "./flag.png"  # Save locally

# Connect to SSH
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=username, password=password)

# Start SCP client for file transfer
scp_client = scp.SCPClient(client.get_transport())

def download_file():
    """Download flag.png from remote SSH server to local machine."""
    print("[+] Downloading flag.png to local machine...")
    scp_client.get(remote_file_path, local_file_path)
    print(f"[+] File saved as {local_file_path}")

def run_local_strings():
    """Run 'strings' command locally on the downloaded file."""
    print("[+] Running 'strings' on local flag.png:")
    os.system(f"strings {local_file_path} | grep -i pico")

# Interactive Loop
while True:
    cmd = input("ssh> ")

    if cmd.strip() == "$$exit":
        print("[+] Exiting SSH session.")
        break

    elif cmd.strip() == f"strings {remote_file_path}":
        # Automatically download and process file locally
        download_file()
        run_local_strings()

    else:
        # Run other commands remotely
        stdin, stdout, stderr = client.exec_command(cmd)
        print(stdout.read().decode())
        print(stderr.read().decode())

# Close connections
scp_client.close()
client.close()
print("[+] SSH session closed.")
