#python
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
def are_congruent(numbers, n): 
    remainders = [num % n for num in numbers]
    return len(set(remainders)) == 1
def solve(a,b,c=8146798528947,d=17,type="2mod"):
 x=a%b
 y=c%d
 if type=="2mod":
    return x
 elif type=="4mod":
  return x,y
 elif type=="2congruent":
   return are_congruent([a, b], c) 
 elif type=="4congruent":
   return are_congruent([a, b, c, d], c)
 else:
   return a%b
if __name__ == "__main__" :
  a=blog.set(11,1)
  b=blog.set(6,2)
  c=blog.set(8146798528947,3)
  d=blog.set(17,3)
  print("flag:",min(solve(a,b,c,d,"4mod")))