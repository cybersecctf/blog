import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog

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
import sys
#one number
def square_root(p,n):
 for a in range(1, p):
    if (a*a) % p == n:
        print(f"The square root of {n} modulo {p} is {a}")
        break
    else:
           print(f"No square root found for {n} modulo {p}")
p=blog.setval(29,1)
ints =blog.setval( "[14, 6, 11]",2)

residues, non_residues = find_square_roots_modulo(p, ints)

print("Quadratic residues and their square roots:")
for i, a in residues:
    print(f"{i} has square roots {a} and {-a % p}")

print("\nQuadratic non-residues:")
for a in non_residues:
    print(a)
qr = [a for a in range(p) if pow(a,2,p) in ints]
print(f"flag {min(qr)}")

 

 
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog