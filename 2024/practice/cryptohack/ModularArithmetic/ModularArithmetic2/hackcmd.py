import blog
def fermat_test(a, p):
    return pow(a, p - 1, p)
import sys
# Test the function with your number and a prime

a=blog.setval(273246787654,1)

p=blog.setval(17,2)
print(fermat_test(a, p))