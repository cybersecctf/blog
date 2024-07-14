 

<!DOCTYPE html>
<html>
 
<body>
    <h1>shufflebox-down underctf 2024 Writeup </h1>

    <h2>Challenge Description</h2>
    <p> 
I've learned that if you shuffle your text, it's elrlay hrda to tlle htaw eht nioiglra nutpi aws.

Find the text censored with question marks in output_censored.txt and surround it with DUCTF{}.

Author: hashkitten
<a href="https://cybersecctf.github.io/blog/2024/downunderctf2024/shufflebox/shufflebox.py">shufflebox.py</a> <a href="https://cybersecctf.github.io/blog/2024/downunderctf2024/shufflebox/output_censored.txt">output_censored.txt</a>
     </p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>we open shufflebox.py andoutput_censored.txt
#output_censored.txt
<code>
aaaabbbbccccdddd -> ccaccdabdbdbbada
abcdabcdabcdabcd -> bcaadbdcdbcdacab
???????????????? -> owuwspdgrtejiiud
</code>
#shufflebox.py
<code>
import random
PERM = list(range(16))
random.shuffle(PERM)
def apply_perm(s):
	assert len(s) == 16
	return ''.join(s[PERM[p]] for p in range(16))
for line in open(0):
	line = line.strip()
</code>
it create random permutation apply first part of  three line to perm and create create result
we don't know third line our code should explores all possible permutations of indices for the characters ‘a’, ‘b’, ‘c’, and ‘d’ in t1. It then checks if rearranging t2 according to each permutation results in the desired string s2. If a valid permutation is found, it is stored in the ok list. The final output is obtained by reversing the valid permutation and applying it to t3 that s's are first part and t's are second  part out txt file
so final code is 
<pre>
#python
import itertools

def find_all(string, char):
    return [i for i, x in enumerate(string) if x == char]

def solve(s1, t1, s2, t2, t3=None, s3=None):
    # Collect positions for each character
    positions = {}
    for char in 'abcd':
        positions[char] = find_all(t1, char)

    # Generate all possible permutations of positions
    pos = [p1 + p2 + p3 + p4 for p1 in itertools.permutations(positions['a'])
                                for p2 in itertools.permutations(positions['b'])
                                for p3 in itertools.permutations(positions['c'])
                                for p4 in itertools.permutations(positions['d'])]

    # Check if permutation that works for s1 works for s2
    valid_perms = []
    for perm in pos:
        if ''.join(t2[perm[i]] for i in range(16)) == s2:
            valid_perms.append(perm)

    assert len(valid_perms) == 1

    # Reverse permutation for t3 or s3
    if t3 is not None:
        result = ''.join(t3[valid_perms[0][i]] for i in range(16))
    elif s3 is not None:
        result = ''.join(s3[valid_perms[0][i]] for i in range(16))
    else:
        raise ValueError("Either t3 or s3 must be provided.")

    return result

# Example usage: 
s1 = "aaaabbbbccccdddd"
t1 = "ccaccdabdbdbbada"
s2 = "abcdabcdabcdabcd"
t2 = "bcaadbdcdbcdacab"
t3 = "owuwspdgrtejiiud"
s3 = None

result_with_t3 = solve(s1, t1, s2, t2, t3=t3)
result_with_s3 = solve(s1, t1, s2, t2, s3=s3)#if s3 isn't none and t3 is none

print("Result with t3:", result_with_t3)
print("Result with s3:", result_with_s3)

</pre> 
and wrap final answer in ductf
   </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">DUCTF{udiditgjwowsuper}
</p>

    <h2>Conclusion</h2>
    <p>this is a very  medium  chanllenge for find permutation of two list relarated</p>

</body>
</html>
