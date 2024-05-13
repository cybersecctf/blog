 
<pre>
#python 
#convert hex of file to file
import sys
hex="challengehex.txt"
zipfile="challenge.zip"
if len(sys.rgv)>2:
 hex=sys.argv[1]
 zipfile=sys.argv[2]
else:
 print("usag -v hexfile destination")     
with open(hex, 'r') as infile:
    # Open the output file in write binary mode
    with open(zipfile, 'wb') as outfile:
        # Iterate over each line in the input file
        for line in infile:
            # Remove any leading/trailing whitespace from the line
            line = line.strip()
            # Convert the hex string to bytes and write to the output file
            outfile.write(bytes.fromhex(line))

print("File converted  successfully.")
</pre>

