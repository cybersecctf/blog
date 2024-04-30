 
# Open the input file in read mode
with open('challengehex.txt', 'r') as infile:
    # Open the output file in write binary mode
    with open('challenge.zip', 'wb') as outfile:
        # Iterate over each line in the input file
        for line in infile:
            # Remove any leading/trailing whitespace from the line
            line = line.strip()
            # Convert the hex string to bytes and write to the output file
            outfile.write(bytes.fromhex(line))

print("File written successfully.")

