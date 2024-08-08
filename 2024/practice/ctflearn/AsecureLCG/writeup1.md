 
<!DOCTYPE html>
<html>
 
<body>
    <h1>ctflearn---A secure LCG?  Writeup </h1>

    <h2>Challenge Description</h2>
    <p>  A secure LCG?
70 points Hard
My friend has lately told me that he's implemented a Pseudorandom Number Generator.

It sounded pretty cool, apart from the fact that he's always been a script kiddie...

He gave me some additional info and wanted to see if it was possible to predict the next number based on the 3 previous numbers.

Additional info:

PRNG is based on "LCG", https://en.wikipedia.org/wiki/Linear_congruential_generator;
    Meaning: x_n+1 = (a*x_n + c) mod m

Generated numbers are natural numbers;

Biggest possibly generated value is: 121409833232633162280;

He chose "special values" for "a" and "c", so that "it's harder to break it";
The following numbers were generated sequentially:

x1 = 65001687610455615650

x2 = 880901038222735

x3 = 16032398895653777
I think I've tried already every "LCG breaker" tool out there on the internet, but none of them has happened to work (each threw some strange error).

Would you please help me?

P.S.

The flag format is: CTFlearn{ASCII representation of the predicted number}

E.g. predicted number = 84698384, then the flag is: CTFlearn{TEST} (84 => "T", 69 => "E"...)
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>after using binawalk and exiftool not working using 

<pre>
#python
# Given numbers
x1 = 65001687610455615650
x2 = 880901038222735
x3 = 16032398895653777

# Given modulus
m = 121409833232633162280

# Calculate a and c
a = (x3 - x2) * pow(x2 - x1, -1, m) % m
c = (x2 - a * x1) % m

print(f"a: {a}, c: {c}, m: {m}")

# Predict the next number
x4 = (a * x3 + c) % m
print(f"Predicted next number: {x4}")

# Convert the predicted number to ASCII representation
flag = ''.join(chr(int(str(x4)[i:i+2])) for i in range(0, len(str(x4)), 2))
print(f"Flag: CTFlearn{{{flag}}}")

</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{more_than_m33ts_the_3y3657BaB2C}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on develper tools in in chrome and web exploitations</p>

</body>
</html>
