
from random import randint
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
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

if __name__ == "__main__" :
    FLAG=blog.solveup("read file","output.txt","")
  
    s=FLAG
    d=decrypt(s)
    print(d)
