#!/usr/bin/env python3
<pre>
import sys
# import this

import blog
def solve(ords,search="crypto"):

 for i in range(300):
 
  s="".join(chr(o ^ i) for o in ords)
  if search in s:
   print("Here is your flag:")
   print(s,i,hex(i))
if __name__ == "__main__" :
 ords=blog.set([81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79],1)
 search=blog.set("crypto",2);
 solve(ords,search)
</pre> 