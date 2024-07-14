
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
