 

<!DOCTYPE html>
<html>
 
<body>
    <h1>5x5 Crypto--ctflearn  Writeup </h1>

    <h2>Challenge Description</h2>
    <p> 
Ever heard of the 5x5 secret message system? If not,
 basically it's a 5x5 grid with all letters of the alphabet in order,
 without k because c is represented to make the k sound only. Google it if you need to. 
A letter is identified by Row-Column. All values are in caps. Try: 1-3,4-4,2-1,{,4-4,2-3,
4-5,3-2,1-2,4-3,_,4-5,3-5,}
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>this is sample  5x5 Polybius square cipher that can decode it with this 


<pre>
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
print(decode_message(cells, exclude='O'))  # Exclude 'W'   sometimes not working code is sample and work for none and k



</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{more_than_m33ts_the_3y3657BaB2C}
</p>

    <h2>Conclusion</h2>
    <p>this is a medium chanllenge for  Polybius square cipher</p>

</body>
</html>
