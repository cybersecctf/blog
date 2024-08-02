
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
blog.islog=True
ords=blog.set([97, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79],1)
hexs=blog.set("d",2)
blog.solveup("snakes search",ords,hexs)#will publish ascii of this list of numbers
import os
os.system(f"python {blog.py_file_path} '{ords}' {hexs}")#run writeups py files with this command also

