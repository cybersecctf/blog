
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
 
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes

def solve(n,e,ct):
 n = 110581795715958566206600392161360212579669637391437097703685154237017351570464767725324182051199901920318211290404777259728923614917211291562555864753005179326101890427669819834642007924406862482343614488768256951616086287044725034412802176312273081322195866046098595306261781788276570920467840172004530873767
 e = 1
 ct = 44981230718212183604274785925793145442655465025264554046028251311164494127485
 return long_to_bytes(ct)
if __name__ == "__main__" :
 n = blog.set(110581795715958566206600392161360212579669637391437097703685154237017351570464767725324182051199901920318211290404777259728923614917211291562555864753005179326101890427669819834642007924406862482343614488768256951616086287044725034412802176312273081322195866046098595306261781788276570920467840172004530873767,1)                                                                
 e = blog.set(1,2)
 ct = blog.set(44981230718212183604274785925793145442655465025264554046028251311164494127485,3)

 print(solve(n,e,ct,) )