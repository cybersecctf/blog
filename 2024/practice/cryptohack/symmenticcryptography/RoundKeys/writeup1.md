
<!DOCTYPE html>
<html>
 
<body>
    <h1>Round Keys- cryptohack</h1>

    <h2>Challenge Description</h2>
    <p> We're going to skip over the finer details of the KeyExpansion phase for now. The main point is that it takes in our 16 byte key and produces 11 4x4 matrices called "round keys" derived from our initial key. These round keys allow AES to get extra mileage out of the single key that we provided.
The initial key addition phase, which is next, has a single AddRoundKey step. The AddRoundKey step is straightforward: it XORs the current state with the current round key.
diagram showing AddRoundKey
 <img src=" https://cybersecctf.github.io/blog/2024/practice/cryptohack/symmenticcryptography/RoundKeys/AddRoundKey.png" alt="ctf quetion image" class="inline"/>
 AddRoundKey also occurs as the final step of each round. AddRoundKey is what makes AES a "keyed permutation" rather than just a permutation. It's the only part of AES where the key is mixed into the state, but is crucial for determining the permutation that occurs.
As you've seen in previous challenges, XOR is an easily invertible operation if you know the key, but tough to undo if you don't. Now imagine trying to recover plaintext which has been XOR'd with 11 different keys, and heavily jumbled between each XOR operation with a series of substitution and transposition ciphers. That's kinda what AES does! And we'll see just how effective the jumbling is in the next few challenges.
Complete the add_round_key function, then use the matrix2bytes function to get your next flag.
Challenge files:
<a href="https://cybersecctf.github.io/blog/2024/practice/cryptohack/symmenticcryptography/RoundKeys/add_round_key.py">add_round.py</a>
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
we use this code for xor of two matrix pair to pair on base of row and col and concert it  to byte 

<pre>

def add_round_key(s, k):
  s = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]
  x= [ [-1]*len(s) for i in range(len(s))]
  i=0
  c=len(s)
  for i in range(c):
   for j in range(c):
     if x[i][j]==-1 :
       x[i][j]=s[i][j]^k[i][j]
  return x      
import blog
if __name__ == "__main__" :
 state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]
 round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]
 state=blog.set(state,1)
 round_key=blog.set(round_key,2) 
 operation=blog.set("text",3)
 x=add_round_key(state, round_key)
 if operation=="text":
  print(blog.solveup("matrix","matrixtobyte",x))
</pre>
       
     
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">flag{}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on develper tools in in chrome and web exploitations</p>
</body>
</html>

 

