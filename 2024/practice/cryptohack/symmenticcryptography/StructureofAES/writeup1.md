
<!DOCTYPE html>
<html>

<body>
    <h1>Structure of AES- cryptohack</h1>

    <h2>Challenge Description</h2>
    <p> To achieve a keyed permutation that is infeasible to invert without the key, AES applies a large number of ad-hoc mixing operations on the input. This is in stark contrast to public-key cryptosystems like RSA, which are based on elegant individual mathematical problems. AES is much less elegant, but it's very fast.

At a high level, AES-128 begins with a "key schedule" and then runs 10 rounds over a state. The starting state is just the plaintext block that we want to encrypt, represented as a 4x4 matrix of bytes. Over the course of the 10 rounds, the state is repeatedly modified by a number of invertible transformations.

Each transformation step has a defined purpose based on theoretical properties of secure ciphers established by Claude Shannon in the 1940s. We'll look closer at each of these in the following challenges.


Here's an overview of the phases of AES encryption:

diagram showing AES rounds

1. KeyExpansion or Key Schedule

 From the 128 bit key, 11 separate 128 bit "round keys" are derived: one to be used in each AddRoundKey step.

2. Initial key addition

 AddRoundKey - the bytes of the first round key are XOR'd with the bytes of the state.

3. Round - this phase is looped 10 times, for 9 main rounds plus one "final round"

 a) SubBytes - each byte of the state is substituted for a different byte according to a lookup table ("S-box").

 b) ShiftRows - the last three rows of the state matrix are transposed—shifted over a column or two or three.

 c) MixColumns - matrix multiplication is performed on the columns of the state, combining the four bytes in each column. This is skipped in the final round.

 d) AddRoundKey - the bytes of the current round key are XOR'd with the bytes of the state.

Included is a bytes2matrix function for converting our initial plaintext block into a state matrix. Write a matrix2bytes function to turn that matrix back into bytes, and submit the resulting plaintext as the flag.

Challenge files:
  - <a href="https://cybersecctf.github.io/blog/2024/practice/cryptohack/symmenticcryptography/StructureofAES/matrix.py">matrix.py</a>

Resources:<a href="https://www.youtube.com/watch?v=gP4PqVGudtg">YouTube: AES Rijndael Cipher explained as a Flash animation</a>
  - 
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
<pre>
import blog
def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return bytes(sum(matrix, []))
def solve(operation,matrix):
   if operation=="matrixtobyte":
                 return matrix2bytes(matrix)
   else:
          if operation=="bytetomatrix":
                 return bytes2matrix(matrix)
if __name__ == "__main__" :
 matrix=blog.set( [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
],1)
 operation="matrixtobyte"
 print(solve(operation,matrix))

</pre>
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">crypto{inmatrix}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for Structure of AES and convert bytes and matrix to eachother</p>
</body>
</html>



