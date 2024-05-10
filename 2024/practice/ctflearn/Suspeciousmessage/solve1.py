def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def prepare_input(dirty, type="pad string"):
    dirty = "".join([c.upper() for c in dirty if c.isalpha()])
    clean = ""

    if len(dirty) < 2:
        return dirty

    for i in range(len(dirty) - 1):
        if type == "leave double letters unchanged":
            clean += dirty[i]
        else:
            if dirty[i] == dirty[i+1]:
                clean += dirty[i] + "X"
            else:
                clean += dirty[i]

    clean += dirty[-1]

    if len(clean) % 2:
        clean += "X"

    return clean

def generate_table(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    table = []

    for char in key.upper():
        if char not in table and char in alphabet:
            table.append(char)

    for char in alphabet:
        if char not in table:
            table.append(char)

    return table

def playfair_decrypt(message, table, key, type="pad string"):
    message = prepare_input(message, type)
    output = ""
    for pair in chunker(message, 2):
        row1, col1 = divmod(table.index(pair[0]), 5)
        row2, col2 = divmod(table.index(pair[1]), 5)

        if type == "encode by moving right one column and down one row":
            if row1 == row2:
                output += table[row1*5+(col1+1)%5] + table[row2*5+(col2+1)%5]
            elif col1 == col2:
                output += table[((row1+1)%5)*5+col1] + table[((row2+1)%5)*5+col2]
            else:
                output += table[row1*5+(col2+1)%5] + table[row2*5+(col1+1)%5]
        else:
            if row1 == row2:
                output += table[row1*5+(col1-1)%5] + table[row2*5+(col2-1)%5]
            elif col1 == col2:
                output += table[((row1-1)%5)*5+col1] + table[((row2-1)%5)*5+col2]
            else:
                output += table[row1*5+col2] + table[row2*5+col1]

    return output

key = "QWERTYUIOPASDFGHKLZXCVBNM"
table = generate_table(key)
message = "MQDzqdorIx4OaWFBhmYlqPpPP"
message = "".join([c for c in message if c.isalpha()])
decrypted_message = playfair_decrypt(message, table, key, type="leave double letters unchanged")

# Convert 'j' to 'p'
decrypted_message = decrypted_message.replace('J', 'P')

# Group into 5 characters
decrypted_message = ' '.join(chunker(decrypted_message, 5))

# Add a new line after every 10 groups
decrypted_message = '\n'.join(chunker(decrypted_message, 50))  # 10 groups * 5 characters

print(decrypted_message)
