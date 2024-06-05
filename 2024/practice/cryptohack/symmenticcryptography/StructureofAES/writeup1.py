import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return bytes(sum(matrix, []))
def solve(operation,matrix):
   if operation=="matrixtobyte":
                 return matrix2bytes(matrix)
   else:
          if operation=="bytetomatrix":
                 return bytes2matrix(matrix)
if __name__ == "__main__" :
 matrix=blog.set( [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
],1)
 operation="matrixtobyte"
 print(solve(operation,matrix))