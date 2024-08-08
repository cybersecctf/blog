
#python
# Given numbers
from sympy import mod_inverse

# Given values
x1 = 65001687610455615650
x2 = 880901038222735
x3 = 16032398895653777

# Initialize variables
a_candidate = None
c_candidate = None
m_candidate = None

# Brute force approach with a smaller step and focused range
for m_candidate in range(int(1e19), int(1.1e19), int(1e16)):  # Focused range, smaller step
    try:
        # Calculate 'a' using mod_inverse
        a_candidate = ((x3 - x2) * mod_inverse(x2 - x1, m_candidate)) % m_candidate
        # Calculate 'c' using the found 'a'
        c_candidate = (x2 - a_candidate * x1) % m_candidate

        # Check if these values generate the correct sequence
        if (a_candidate * x2 + c_candidate) % m_candidate == x3:
            # We've found a match, stop searching
            print(f"Found values: a = {a_candidate}, c = {c_candidate}, m = {m_candidate}")
            break
    except ValueError:
        # Skip if mod_inverse fails (i.e., gcd(x2 - x1, m_candidate) != 1)
        continue

# Only predict the next number if valid values were found
if a_candidate is not None and c_candidate is not None and m_candidate is not None:
    # Predict the next number in the sequence
    x4 = (a_candidate * x3 + c_candidate) % m_candidate
    print(f"Predicted next number: x4 = {x4}")

    # Convert the predicted number to ASCII characters (for the CTF flag)
    flag = ''.join(chr((x4 >> (8 * i)) & 0xFF) for i in range(8))[::-1]
    print(f"CTF Flag: CTFlearn{{{flag}}}")
else:
    print("Failed to find suitable values for a, c, and m.")


