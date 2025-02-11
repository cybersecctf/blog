from Crypto.Util.number import getPrime

p = getPrime(64)
while p % 65537 != 1:
    p = getPrime(64)
q = getPrime(64)

print(p)
print(q)