 

<!DOCTYPE html>
<html>
 
<body>
    <h1>htbctf2024---Dynastic  Writeup </h1>

    <h2>Challenge Description</h2>
    <p>You find yourself trapped inside a sealed gas chamber,
 and suddenly, the air is pierced by the sound of a distorted voice played through a pre-recorded tape. Through this eerie transmission, you discover that within the next 15 minutes,
 this very chamber will be inundated with lethal hydrogen cyanide. As the tape’s message concludes, a sudden mechanical whirring fills the chamber,
 followed by the ominous ticking of a clock. 
You realise that each beat is one step closer to death. Darkness envelops you,
 your right hand restrained by handcuffs, and the exit door is locked.
 Your situation deteriorates as you realise that both the door and the handcuffs demand the same passcode to unlock. Panic is a luxury you cannot afford;
 swift action is imperative. As you explore your surroundings, your trembling fingers encounter a torch. Instantly, upon flipping the switch,
 the chamber is bathed in a dim glow, unveiling cryptic letters etched into the walls and a disturbing image of a Roman emperor drawn in blood.
 Decrypting the letters will provide you the key required to unlock the locks.
 Use the torch wisely as its battery is almost drained out!
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>we open <a href="https://cybersecctf.github.io/blog/2024/htbctf/Dynastic/source.py">source.py</a>
and see modified version of caesar that work with 0x41 twice and encrypt function that print encrypted flag in 
<a href="https://cybersecctf.github.io/blog/2024/htbctf/Dynastic/output.txt">output.tx</a>  .
so  we must decryp tthis value with reverse encrypt function and get flag just
change location of to_identity_map and from_identity_map + to - and 
with this code get flag


<pre>
import blog
from random import randint

import blog
FLAG="HTB{fake}"
def to_identity_map(a):
    return ord(a) - 0x41

def from_identity_map(a):
    return chr(a % 26 + 0x41)

def encrypt(m):
    c = ''
    for i in range(len(m)):
        ch = m[i]
        if not ch.isalpha():
            ech = ch
        else:
            chi = to_identity_map(ch)
            ech = from_identity_map(chi + i)
        c += ech
    return c
 
def decrypt(enc):
    flag = ''
    for i in range(len(enc)):
        ech = enc[i]
        if not ech.isalpha():
            m = ech
        else:
            echi = to_identity_map(ech)
            m = from_identity_map(echi - i)
        flag += m
    return flag

    

import os,subprocess

def solve(word, operation="decrypt file"):

    if "file" in operation :
      word=blog.solveup("read file",word,"")
    if "encrypt" in operation :
      return encrypt(word)
    
    if "decrypt" in operation :
       return decrypt(word)
    return f"not valid operation solveup({word},{operation})"
   

if __name__ == "__main__" :
  file=blog.set("output.txt",1)
  operation=blog.set("decrypt file",2)
  print(solve("output.txt",operation))
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">HTB{DID_YOU_KNOW_ABOUT_THE_TRITHEMIUS_CIPHER?!_IT_IS_SIMILAR_TO_CAESAR_CIPHER
}
</p>

    <h2>Conclusion</h2>
    <p>this is a easy chanllenge for reverse python in custom caesar</p>

</body>
</html>