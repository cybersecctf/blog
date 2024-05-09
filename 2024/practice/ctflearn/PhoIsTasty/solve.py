import subprocess
import re
import sys

# Get the file name, search string, and pattern from command line arguments
file = "971"
search = "ctf"
pattern = ".."
if len(sys.argv) > 1:
    file = sys.argv[1]
if len(sys.argv) > 2:
    search = sys.argv[2]
if len(sys.argv) > 3:
    pattern = sys.argv[3]

# Define the command as a list
command = ["hexdump", "-C", file]

# Run the command
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Get the output and error (if any)
stdout, stderr = process.communicate()

# Convert the output to a string
hexdump = stdout.decode()

# Split the hexdump into lines
lines = hexdump.split("\n")

# If a pattern is provided, search for the pattern
if pattern:
    pattern = pattern.join(list(search))  # Creates a pattern like "C..T..F"
    for i, line in enumerate(lines, start=1):
        # Search for the pattern in the line using regular expressions
        match = re.search(pattern, line, re.IGNORECASE)
        if match:
            print(f"'{search}' found in line {i}!")
            print("Matched content:", match.group())
            print("Next 5 lines:")
            print(line)
            for next_line in lines[i:i+5]:
                print(next_line)
            break
    else:
        print(f"'{search}' not found in hexdump.")
# If no pattern is provided, search for the exact string
else:
    for i, line in enumerate(lines, start=1):
        # Check if the target is in the line
        if search.lower() in line.lower():
            print(f"'{search}' found in line {i}!")
            print("Matched content:", line)
            print("Next 5 lines:")
            for next_line in lines[i:i+5]:
                print(next_line)
            break
    else:
        print(f"'{search}' not found in hexdump.")

# Print the error (if any)
if stderr:
    print("Error:", stderr.decode())

