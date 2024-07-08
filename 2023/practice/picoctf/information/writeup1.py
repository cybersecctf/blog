 
import os
def solve(file):
 os.system(f"exiftool {file}")
if __name__ == "__main__" :
 solve("cat.jpg")
