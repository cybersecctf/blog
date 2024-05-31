#python
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog

def solve(s, n):
    try:
        ords = blog.solveup("encode/decode full", "encode", s, "ascii")
        hexs = hex(int(n))
        hexs = int(hexs, 16)
        result = "".join(chr(o ^ hexs) for o in ords)
        return result
    except Exception as e:
        return "err" + str(e)

if __name__ == "__main__":
    s = blog.set("label", 1)
    n = blog.set(13, 2)
    print(solve(s, n))