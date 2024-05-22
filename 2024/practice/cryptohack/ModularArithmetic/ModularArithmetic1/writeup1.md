
<!DOCTYPE html>
<html>

<body>
    <h1>Modular Arithmetic 1-cryptohack</h1>

    <h2>Challenge Description</h2>
    <p> Imagine you lean over and look at a cryptographer's notebook. You see some notes in the margin:

4 + 9 = 1
5 - 7 = 10
2 + 3 = 5

At first you might think they've gone mad. Maybe this is why there are so many data leaks nowadays you'd think, but this is nothing more than modular arithmetic modulo 12 (albeit with some sloppy notation).

You may not have been calling it modular arithmetic, but you've been doing these kinds of calculations since you learnt to tell the time (look again at those equations and think about adding hours).

Formally, "calculating time" is described by the theory of congruences. We say that two integers are congruent modulo m if a ≡ b mod m.

Another way of saying this, is that when we divide the integer a by m, the remainder is b. This tells you that if m divides a (this can be written as m | a) then a ≡ 0 mod m.

Calculate the following integers:

11 ≡ x mod 6
8146798528947 ≡ y mod 17

The solution is the smaller of the two integers.
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
      this is challenge for calculate mod of two number and from two pair find smallest we use this code
<pre>
#python
import sys
import blog
a=11
a=blog.set(11,1)
b=6
x=0
y=0
b=blog.set(6,2)
if b!=6:
 x = a % b
 print(x)
c=blog.set(8146798528947,3)
d=17
d=blog.set(17,3)
if d!=17: 
  d=int(sys.argv[4])
  y = c % d
  print(y)
flag=x
if x>y:
 flag=y
 print("flag:",flag)
def are_congruent(numbers, n): 
    remainders = [num % n for num in numbers]
    return len(set(remainders)) == 1

# Test the function with two numbers
print(are_congruent([a, b], c))  # should print True

# Test the function with four numbers
print(are_congruent([a, b, c, d], c))  # should print False
</pre>
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">4
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on  calculate mods and congruent number</p>
</body>
</html>

