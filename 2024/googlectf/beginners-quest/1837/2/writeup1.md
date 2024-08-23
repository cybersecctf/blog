<title>google ctf begginer quest-  1837 -2</title>
<!DOCTYPE html>
<html>

<body>
    <h1>google ctf begginer quest-  1837 -2</h1>

    <h2>Challenge Description</h2>
    <p>Operator, can you decode this radio telegram for us? our predecessor managed to figure out the last two telegrams we intercepted and recorded, but unfortunately  they didn't leave us an explanation of what these messages are encrypted with. We think these messages might all be using the same code and keys, though.HINT: We have evidence that suggests that these messages were all written down in 7 columns when they were being encrypted. Could this be useful somehow?         
FLAG FORMAT: FLAG{example} except in challenge 2

</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
    This time we start by downloading the audio <a href="https://cybersecctf.github.io/blog/2024/googlectf/beginners-quest/1837/2/1837challenge2.mp3">file</a>.
If we listen to the audio file we can hear a morse code signal. We will use this online tool to decode the morse code.
After decoding the morse code we get the following text:
<pre>
GXAGGADXGGFXXXFGDDGXAGFXFAVGFXDVAVAGFGXFXGFDFDFGVGFXGFXAVXVGXVADXGVGXXXVGAVDXVVXAADVDFXDDFVGXXDGXGGGFAXFXDDGDGDXGDAAXFVAFFXDFFGFAGXGXGGDFFXVAVXFGFXGXAVDGXDGDXAFFAFVVDDAXXVXVFVXDXDGXGVDXFFFGAVAFFAXXFAXAGDXFXDXVXFXGADXVVGVXXFXGDGAAFAVXVAAXFFFADDAAVDDAAXFFDDGDGVDDAGAFAFFDV
</pre>
We notice that this text only contains the letters A, D, F, G, V, X. This looks like a ADFGVX cipher.

We now download the decrypted telegraphs.

After looking at the decrypted telegraphs we notice that the first and last few words are identical. This can be used to bruteforce all transpositions keys. We need to define a length for the key. After trying a bit we find out that the key is 7 characters long.

This script bruteforces all possible transpositions keys until both encrypted messages start and end with similar characters after being transposed.

Then the script creates a translation dictionary using the already decrypted telegraphs and will apply the transformation and dictionary to the interesting text.
<pre>
import itertools
import math

def read_file(file_path: str) -> str:
    with open(file_path, 'rb') as f:
        # read special characters
        text = f.read().decode('utf-8')
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

text1 = read_file("ciphertext.2txt").replace("\n", "")
text2 = read_file("ciphertext2.txt").replace("\n", "")
interesting = read_file("2.txt").replace("\n", "")

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
</pre>
we run this script and get flag on text below after word FLAG
<pre>
FROMGENERALSTAFFOFFICE14MARCH1918TRENCHCODE456ISNOWCOMPROMISEDDONOTUSEINFURTHERCOMMUNICATIONSNEWTRENCHCODESHOULDBEFOUNDATFLAGXXXXXXXXXX

</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">FLAG{XXXXXXXXXX}
</p>

    <h2>Conclusion</h2>
    <p>this is a medium chanllenge for decode morse code and convert text with  ADFGVX chipher </p>
</body>
</html>




