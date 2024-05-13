import itertools
import math

def read_file(file_path: str) -> str:
    with open(file_path, 'r') as f:
        # read special characters
        text = f.read() 
   
    return text


def unscramble(text, comb):
    row_len = len(comb)

    columns = [""] * row_len
    long_column_len = math.ceil(len(text) / row_len)
    short_column_len = math.floor(len(text) / row_len)

    short_column_count = row_len - len(text) % row_len
    long_column_count = row_len - short_column_count

    inverted_key = invert_key(comb)

    i = 0
    c = 0
    for k in inverted_key:
        is_long_column = k < long_column_count

        if is_long_column:
            columns[c] = text[i:i+long_column_len]
            i += long_column_len
        else:
            columns[c] = text[i:i+short_column_len]
            i += short_column_len
        c += 1
    
    unscrambled = ""

    for i in range(len(text)):
        c_idx = comb[i % row_len]
        z_idx = i // row_len

        if z_idx < len(columns[c_idx]):
            unscrambled += columns[c_idx][z_idx]
    
    return unscrambled


def invert_key(key):
    inverted = [0] * len(key)

    for i in range(len(key)):
        inverted[key[i]] = i
    return inverted


def try_combination(comb, text1, text2):
    # text 1 and text 2 start and end similarly
    front_ident_len = 100
    trail_ident_len = 46

    reordered1 = unscramble(text1, comb)
    reordered2 = unscramble(text2, comb)
    
    if reordered1[:front_ident_len] == reordered2[:front_ident_len] and reordered1[len(reordered1)-trail_ident_len:] == reordered2[len(reordered2)-trail_ident_len:]:
        return comb
    return None


def str_to_key(string):
    key = []
    for c in string.upper():
        key.append( ord(c) - ord('A') )
    return key



# Bruteforce combinations
row_len = 7

text1 = read_file("ciphertext1.txt")
text2 = read_file("ciphertext2.txt")
interesting = read_file("2.txt") 

comb = None

for combination in list(itertools.permutations(range(row_len))):
    comb = try_combination(combination, text1, text2)
    if comb != None:
        break


# unscramble the interesting text
unscrambled = unscramble(interesting, comb)


# create a dictionary
cypherdict = {}

plain1 = read_file("plaintext1.txt")
plain2 = read_file("plaintext2.txt")

trans1 = unscramble(text1, comb)
trans2 = unscramble(text2, comb)


for i in range(len(plain1)):
    # 2 letters in trans1 correspond to 1 letter in plain1
    cypherdict[trans1[i*2:i*2+2]] = plain1[i]

for i in range(len(plain2)):
    # 2 letters in trans2 correspond to 1 letter in plain2
    cypherdict[trans2[i*2:i*2+2]] = plain2[i]


# decrypt final text
result = ''
for i in range(len(unscrambled)//2):
    result += cypherdict[unscrambled[i*2:i*2+2]]

print(result)