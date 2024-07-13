
#python
import codecs
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
def solve(val,type):
 return codecs.encode( val, type)
if __name__ == "__main__" :
 val=blog.set("cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_GYpXOHqX}",1)
 type=blog.set("rot13",2)
 print(solve( val, type))

  