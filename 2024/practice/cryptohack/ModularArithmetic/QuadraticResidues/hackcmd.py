def find_square_roots_modulo(p, ints):
    residues = []
    non_residues = []
    for a in range(1, p):
        for i in ints:
            if (a*a) % p == i:
                residues.append((i, a))
                break
        else:
            non_residues.append(a)
    return residues, non_residues

p = 29
ints = [14, 6, 11]
residues, non_residues = find_square_roots_modulo(p, ints)

print("Quadratic residues and their square roots:")
for i, a in residues:
    print(f"{i} has square roots {a} and {-a % p}")

print("\nQuadratic non-residues:")
for a in non_residues:
    print(a)
p = 29
ints = [14, 6, 11]

qr = [a for a in range(p) if pow(a,2,p) in ints]
print(f"flag {min(qr)}")