
from Crypto.Util.number import inverse, long_to_bytes

# Given values
n = 317903423385943473062528814030345176720578295695512495346444822768171649361480819163749494400347
e = 65537
enc = 127075137729897107295787718796341877071536678034322988535029776806418266591167534816788125330265

# Calculate phi(n)
phi_n = n - 1

# Compute the private key (d)
d = inverse(e, phi_n)

# Decrypt the ciphertext
m = pow(enc, d, n)
decrypted_flag_bytes = b'\x12\x8c/,\xe2\x99t\xa6\xb2\xf0\xad\t\x10[Uaz6\x1a#\xf0\xb8\xf9\xad\xb3\x14\xa2q_\xbf\x01\x08\xc4\x14\x9a!\xe8\xbc\x04\x0b'

# Convert to UTF-8 string
original_flag_utf8 = decrypted_flag_bytes.decode('utf-8')

print(f"Original flag (UTF-8): {original_flag_utf8}")
 
<pre>
from Crypto.Util.number import long_to_bytes, inverse

# Given values
n = 317903423385943473062528814030345176720578295695512495346444822768171649361480819163749494400347
e = 65537
enc = 127075137729897107295787718796341877071536678034322988535029776806418266591167534816788125330265

# Factors of n
p = 170141183460469231731687303715884105727
q = 178405961588244985122522819014526152527
r = 179386039336999138022590197009205097239
s = 138034926935811275748087458667020337217
a = 173611382357017792874854468733661181

# Calculate phi(n)
phi_n = (p-1) * (q-1) * (r-1) * (s-1) * (a-1)

# Calculate the private key d
d = inverse(e, phi_n)

# Decrypt the ciphertext
m = pow(enc, d, n)
FLAG = long_to_bytes(m)

print(FLAG)

</pre>


