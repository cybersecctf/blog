
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
ords=blog.set([97, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79],1)
hexs=blog.set("",2)
blog.solveup("snakes search",ords,hexs)
