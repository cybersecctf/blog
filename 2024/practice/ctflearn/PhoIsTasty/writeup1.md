<title>Pho Is Tasty!- ctflearn</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Pho Is Tasty!- ctflearn</h1>

    <h2>Challenge Description</h2>
    <p>The flag is hidden in the jpeg file. Good Luck! Have some Pho! Solve this challenge before solving my Scope challenge for 100 points.
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
i download file 
 <img src=" https://cybersecctf.github.io/blog/2024/practice/ctflearn/PhoIsTasty/971" alt="ctf quetion image" class="inline"/>
       using exiftool and strings not work but after search see that hexdump is working so
use this python code for search with or without pattern in hexdump and find flag
<pre>
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

</pre>
and find flag in text
<pre>
ctf' found in line 5!
Matched content: C..T..F
Next 5 lines:
00000040  1d 09 43 04 15 54 02 06  46 14 0d 6c 16 0e 65 06  |..C..T..F..l..e.|
00000050  19 61 17 1f 72 1b 18 6e  01 0c 7b 04 07 49 0f 03  |.a..r..n..{..I..|
00000060  5f 02 0e 4c 16 18 6f 1f  04 76 19 0c 65 1f 06 5f  |_..L..o..v..e.._|
00000070  18 01 50 11 10 68 13 14  6f 1a 02 21 04 02 21 13  |..P..h..o..!..!.|
00000080  14 21 0b 14 7d ff db 00  84 00 08 08 08 08 08 08  |.!..}...........|
00000090  09 0a 0a 09 0c 0d 0c 0d  0c 12 10 0f 0f 10 12 1b  |................|
</pre>
remove dots and will get flag
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlearn{I_Love_Pho!!!}
</p>

    <h2>Conclusion</h2>
    <p>this is a     easy chanllenge for search on hexdump of files</p>
</body>
</html>


