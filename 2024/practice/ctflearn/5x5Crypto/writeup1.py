
import numpy as np

def create_cipher(exclude=None):
    if exclude:
        alphabet = [chr(i) for i in range(65, 91) if chr(i) != exclude.upper()]
    else:
        alphabet = [chr(i) for i in range(65, 91)]
    
    # Ensure the array is 5x5 by taking the first 25 characters
    alphabet = alphabet[:25]

    arr = np.array(alphabet).reshape(5, 5)
    return arr

def decode_message(cells, exclude=None):
    arr = create_cipher(exclude)
    decoded_message = []
    for i in cells:
        if i[0].isdigit() and i[2].isdigit():
            x = int(i[0]) - 1
            y = int(i[2]) - 1
            decoded_message.append(arr[x][y])
        else:
            decoded_message.append(i[0])
    return ''.join(decoded_message)

# Example usage
cells = ["1-3", "4-4", "2-1", "{", "4-4", "2-3", "4-5", "3-2", "1-2", "4-3", "_", "4-5", "3-5", "}"]
print(decode_message(cells))  # No exclusion
print(decode_message(cells, exclude='K'))  # Exclude 'K'
print(decode_message(cells, exclude='O'))  # Exclude 'W'



