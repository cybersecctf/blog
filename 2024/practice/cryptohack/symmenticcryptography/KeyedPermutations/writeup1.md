
<!DOCTYPE html>
<html>

<body>
    <h1>Keyed Permutations- cryptohack</h1>

    <h2>Challenge Description</h2>
    <p> AES, like all good block ciphers, performs a "keyed permutation". This means that it maps every possible input block to a unique output block, with a key determining which permutation to perform.

A "block" just refers to a fixed number of bits or bytes, which may represent any kind of data. AES processes a block and outputs another block. We'll be specifically talking the variant of AES which works on 128 bit (16 byte) blocks and a 128 bit key, known as AES-128.


Using the same key, the permutation can be performed in reverse, mapping the output block back to the original input block. It is important that there is a one-to-one correspondence between input and output blocks, otherwise we wouldn't be able to rely on the ciphertext to decrypt back to the same plaintext we started with.

What is the mathematical term for a one-to-one correspondence?
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
The mathematical term for a one-to-one correspondence is a bijection. A bijection, also known as a bijective function, is a function that is both injective (one-to-one) and surjective (onto). This means that every element of the function’s domain maps to a unique element in the function’s codomain, and every element in the codomain is the image of exactly one element in the domain and can run with   codes like this or any mapping code
<pre>
#python
class Bijection:
    def __init__(self):
        self.int_to_str = {}
        self.str_to_int = {}

    def add(self, i, s):
        if i in self.int_to_str or s in self.str_to_int:
            return
        self.int_to_str[i] = s
        self.str_to_int[s] = i

    def get_str(self, i):
        return self.int_to_str.get(i)

    def get_int(self, s):
        return self.str_to_int.get(s)
#a first elements and b second elements and c elements that you want see
def solve(a,b,c):
  bi = Bijection()
  for x in a:
   for y in b:
    bi.add(x, y)
  for z in c:
    print(bi.get_str(z))   
if __name__ == "__main__" :
    solve([1,2,3],["bijection","two","four"],[1])        
 

</pre>
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">crypto{bijection}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work bijection and understand meaning</p>
</body>
</html>

