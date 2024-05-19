
#python
def fermat_test(a, p):
    return pow(a, p - 1, p)
import sys
# Test the function with your number and a prime
a = 273246787654
if len(sys.argv)>1:
  a=sys.argv[1]

p = 17  # example of a prime number
if len(sys.argv)>2:
  p=sys.argv[2]
print(fermat_test(a, p))