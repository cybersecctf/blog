<title>The Simpsons--ctflearn  Writeup </title>
 

<!DOCTYPE html>
<html>
 
<body>
    <h1>The Simpsons--ctflearn  Writeup </h1>

    <h2>Challenge Description</h2>
    <p>  
Ya know, I was thinking... wouldn't the Simpsons use octal as a base system? They have 8 fingers... Oh, right! The problem! Ummm, something seems odd about this image... https://mega.nz/#!yfp1nYrQ!LOz_eucuKkjAaDqVvz3GWgbfdKWn8BhussKZbx6bUMg
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>with run this code and get exiftool and answer quetions and decode octals..
<pre>
#python
import blog
def basec(n,base):
 return int(n , base)
def solve(encoded,key="",base=8):
  if key=="":#if no code do base convert on base of problem or if have key do vigenere-cipher
   z=""
   for x in s1.split():
    z+=chr(basec(x,8))
   return z
  else:
   cipher = list(map(lambda x: int(x, 8), encoded.split()))
   s=[]
   for i in range(len(cipher)):
     s.append( chr(ord('a')+(cipher[i]-ord(key[i % len(key)])+26) % 26))
   return "".join(s)
print(blog.solveup("garden","strings ItsKrumpingTime.jpg",""))
z=""
z1=""
s1="152 162 152 145 162 167 150 172 153 162 145 170 141 162"
 
  
s2="110 157 167 040 155 165 143 150 040 144 151 144 040 115 141 147 147 151 145 040 157 162 151 147 151 156 141 154 154 171 040 143 157 163 164 077 040 050 104 151 166 151 144 145 144 040 142 171 040 070 054 040 164 157 040 164 150 145 040 156 145 141 162 145 163 164 040 151 156 164 145 147 145 162 054 040 141 156 144 040 164 150 145 156 040 160 154 165 163 040 146 157 165 162 051"
print(solve(s1),solve(s2))
key = round(847.63/8)+4
key = chr(key)
key = key + key + chr(ord(key)-4)
print(solve(s1,key))#if key !=""     do viigener cipher else base converter solve("10","",2)

</pre>
after exiftool file see numbers and find octal and convert them to ascii full two array 
of number print 
<code>
Ahh! Realistically the Simpsons would use octal instead of decimal!
encoded = 152 162 152 145 162 167 150 172 153 162 145 170 141 162
key = chr(SolutionToDis(110 157 167 040 155 165 143 150 040 144 151 144 040 115 141 147 147 151 145 040 157 162 151 147 151 156 141 154 154 171 040 143 157 163 164 077 040 050 104 151 166 151 144 145 144 040 142 171 040 070 054 040 164 157 040 164 150 145 040 156 145 141 162 145 163 164 040 151 156 164 145 147 145 162 054 040 141 156 144 040 164 150 145 156 040 160 154 165 163 040 146 157 165 162 051))
key = key + key + chr(ord(key)-4)
print(DecodeDat(key=key,text=encoded))
jrjerwhzkrexar How much did Maggie originally cost? (Divided by 8, to the nearest integer, and then plus four)
</code>
i search google answer of this is How much did Maggie originally cost?$847.63
so for find key and see is vigener cipher with key .for get flag run above code
 
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlearn{wearenumberone}
</p>

    <h2>Conclusion</h2>
    <p>this is a medium chanllenge for work on bases and vigener cipher</p>

</body>
</html>
