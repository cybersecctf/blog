#python
import sys
a=11
if len(sys.argv)>1:
 a=int(sys.argv[1])
b=6
if len(sys.argv)>2:
 b=int(sys.argv[2])
c=8146798528947
if len(sys.argv)>3:
 c=int(sys.argv[3])
d=17
if len(sys.argv)>4:
 d=int(sys.argv[4])
x = a % b
y = c % d
if len(sys.argv)>2:
 print(x)
if len(sys.argv)>4:
 print(y)
flag=x
if x>y:
 flag=y
 print("flag:",flag)
def are_congruent(numbers, n): 
    remainders = [num % n for num in numbers]
    return len(set(remainders)) == 1

# Test the function with two numbers
print(are_congruent([a, b], c))   

# Test the function with four numbers
print(are_congruent([a, b, c, d], c))