
import base64
import sys

sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog

def solve(operation, a):
    try:
        if operation == "decode":
            # Decode the base64 string to bytes, then decode bytes to string
            decoded_bytes = base64.b64decode(a)
            return decoded_bytes.decode('utf-8')
        else:
            # Encode the string to bytes, then to base64
            if isinstance(a, str):
                a = a.encode('utf-8')
            return base64.b64encode(a).decode('utf-8')
    except Exception as e:
        return f"not a base64 number {str(e)}"

if __name__ == "__main__":
    a = blog.set("d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2kyMDRoa2o2fQ==", 1)
    print(solve("decode", a))