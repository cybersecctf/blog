<pre>
#python
import numpy as np
import sys 
# ADFGVX cipher key square
key_square = [
    ['A', 'D', 'F', 'G', 'V', 'X'],
    ['N', 'B', 'C', 'E', 'H', 'I'],
    ['K', 'L', 'M', 'O', 'P', 'Q'],
    ['R', 'S', 'T', 'U', 'W', 'Y'],
    ['Z', '0', '1', '2', '3', '4'],
    ['5', '6', '7', '8', '9', '_']
]

def adfgvx_decrypt(message, keyword):
    # Determine dimensions of the key square
    rows = len(key_square)
    cols = len(key_square[0])

    # Create a dictionary to map ADFGVX symbols to row and column indices
    symbol_map = {}
    for i in range(rows):
        for j in range(cols):
            symbol_map[key_square[i][j]] = (i, j)

    # Remove spaces and split the message into ADFGVX pairs
    pairs = [message[i:i+2] for i in range(0, len(message), 2)]

    # Construct the transposition key from the keyword
    transposition_key = sorted(keyword)

    # Determine the number of columns for the transposition matrix
    num_cols = len(transposition_key)

    # Calculate the number of rows required
    num_rows = (len(pairs) + num_cols - 1) // num_cols

    # Initialize the transposition matrix with spaces
    transposition_matrix = [[''] * num_cols for _ in range(num_rows)]

    # Populate the transposition matrix with the ADFGVX pairs
    for i, pair in enumerate(pairs):
        row, col = divmod(i, num_cols)
        transposition_matrix[row][col] = pair

    # Reorder the columns of the transposition matrix based on the keyword
    reordered_matrix = []
    for letter in transposition_key:
        col_index = transposition_key.index(letter)
        reordered_matrix.append([row[col_index] for row in transposition_matrix])

    # Concatenate the rows of the reordered matrix to form the intermediate message
    intermediate_message = ''.join(''.join(row) for row in reordered_matrix)

    # Split the intermediate message into rows based on the length of the keyword
    intermediate_rows = [intermediate_message[i:i+num_rows] for i in range(0, len(intermediate_message), num_rows)]

    # Reorder the rows of the intermediate message based on the sorted keyword
    reordered_rows = [''] * num_rows
    for letter in keyword:
        row_index = transposition_key.index(letter)
        reordered_rows[row_index] = intermediate_rows.pop(0)

    # Concatenate the reordered rows to obtain the transposed message
    transposed_message = ''.join(reordered_rows)

    # Initialize the plaintext
    plaintext = ''

    # Iterate over the transposed message and perform the ADFGVX decryption
    for i in range(0, len(transposed_message), 2):
        symbol = transposed_message[i:i+2]
        symbol_row, symbol_col = symbol_map[symbol[0]]
        plaintext += key_square[symbol_row][int(symbol_col)]  # Convert second character to integer for column index
    return plaintext

# Example usage
if __name__ == "__main__":
    # Encrypted message and keyword
     isadfgvx=False  
     encrypted_message = "GDGDDFXVVDAFAXFXFDGXFFAXFVDXFXGDFFGXFXVVFDVXXDGXGFGGDFGVXVDGDFXXDDVAFDXVXGVDGFDXGGDGDAGFGXAF"
     if "A" in encrypted_message:
           if "D" in encrypted_message: 
              if "F" in encrypted_message: 
                    if "G" in encrypted_message: 
                           if "V" in encrypted_message: 
                                 if "X" in encrypted_message: 
                                          isadfgvx=True
     if not isadfgvx:
            print("isn't adfgvx chipher")
                    
     if len(sys.argv)>1:
          encrypted_message=sys.argv[1]
  
     keyword = "KEYWORD"
     if len(sys.argv)>2:
          keyword=sys.argv[2]
     # Decrypt the message
     plaintext = adfgvx_decrypt(encrypted_message, keyword)
     print("Decrypted message:", plaintext)
</pre>