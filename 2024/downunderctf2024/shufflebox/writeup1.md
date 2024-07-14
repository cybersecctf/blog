 

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
s1 = "aaaabbbbccccdddd"
t1 = "ccaccdabdbdbbada"

s2 = "abcdabcdabcdabcd"
t2 = "bcaadbdcdbcdacab"

t3 = "owuwspdgrtejiiud"

pos = []

# returns a list with all indicies of char in string
def find_all(string, char):
    l = []
    for i,x in enumerate(string):
        if x == char:
            l.append(i)
    return l

import itertools

# find all permuations for a b c and d then just combine them together
# s1 is nice since its 4 a's then 4 b's etc
for perma in itertools.permutations(find_all(t1,'a')):
    for permb in itertools.permutations(find_all(t1,'b')):
        for permc in itertools.permutations(find_all(t1,'c')):
            for permd in itertools.permutations(find_all(t1,'d')):
                pos.append(perma+permb+permc+permd)

# check if perm that works for s1 works for s2
ok = []
for perm in pos:
    # use t2 since we are reversing the permuation
    if ''.join(t2[perm[p]] for p in range(16)) == s2:
        ok.append(perm)

assert len(ok) == 1

# reverse for s3
print(''.join(t3[ok[0][p]] for p in range(16)))
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
