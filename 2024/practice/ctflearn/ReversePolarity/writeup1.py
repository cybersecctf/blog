
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
def solve(s,operation="decode",length=8):
   result=""
   if operation=="decode":
    result= ''.join(chr(int(s[i*length:i*length+length],2)) for i in range(len(s)//length))
   else:
    result =   int(bin(s)[2:])
   return result
if __name__ == "__main__" :
 X=blog.set("01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101",1,"str")
 print(solve(X))
