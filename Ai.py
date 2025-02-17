
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog

def solve(x1,iv,c):
 # c = Ek(iv xor x1)    ci = Ek(c(i-1) xor xi)
 y1 = "SEND_NUDES_MELA!"
 iv2 = []
 # c will be the same if   iv xor x1 = iv2 xor y1
 #                         iv2 = (iv xor x1) xor y1
 #        s                  flag{iv2,c}
 for i in range(len(iv)):
    #print("",ord(x1[i]),end="")
    #iv1.append(iv[i])
    d=blog.solveup("venona","encode",iv[i]^ord(x1[i])^ord(y1[i]),"int hex").replace("0x","")  
    iv2.append(d)
 return "".join(iv2)
if __name__ == "__main__" :
 x1 =blog.set( "FIRE_NUKES_MELA!",1)
 iv =blog.set( b'\x39\x1e\x95\xa1\x58\x47\xcf\xd9\x5e\xce\xe8\xf7\xfe\x7e\xfd\x66',2)
 c =blog.set( b'\x84\x73\xdc\xb8\x6b\xc1\x2c\x6b\x60\x87\x61\x9c\x00\xb6\x65\x7e',3) 
 iv2=solve(x1,iv,c)
 print(iv2)
