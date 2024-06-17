
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
def solve(n,p=-1,q=-1):
  if p==-1 and q==-1:
   count=0
   for k in range(1,n+1):
     if   blog.solveup("gcd",n,k)==1:
                   count+=1
  else:
        count=(p-1)*(q-1)    
  return count
if __name__ == "__main__" :
 n=blog.set(-1,1)
 p = 857504083339712752489993810777
 q = 1029224947942998075080348647219
 n=p*q
 print(solve(n,p,q)) 
