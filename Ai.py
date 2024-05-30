import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
s=blog.set("label",1)
n=blog.set(13,2)
print(s)
print(blog.solveup("xor string integer",s,n))