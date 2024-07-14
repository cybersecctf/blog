
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
s3 = "your_custom_s3_string"

result_with_t3 = solve(s1, t1, s2, t2, t3=t3)
result_with_s3 = solve(s1, t1, s2, t2, s3=s3)

print("Result with t3:", result_with_t3)
print("Result with s3:", result_with_s3)

