
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog

import os,subprocess
def msb(num, pos):
    ret = (num & (1 << pos[0])) >> pos[0]
    for p in pos[1:]:
        ret ^= (num & (1 << p)) >> p
    return ret

def get_next(last, pos):
    m = msb(last, pos)
    return (m << 7)|(last >> 1)

def solve(cipher,prefix,msb_pos):
   
    last = 0
    last = prefix[-1] ^ cipher[len(prefix)-1]

    output=''
    
    for i in range(len(prefix), len(cipher)):
        last = get_next(last, msb_pos)
        output += chr(cipher[i] ^ last)
        
    return prefix + output.encode()
if __name__ == "__main__" :
 cipher = blog.set("./PRNG/secretMessage.hex",1)
 prefix =blog.set( b"CTFlearn{",2)
 msb_pos = blog.set([6,5,3,2,0],3)
 print(solve(cipher,prefix,msb_pos))
 
