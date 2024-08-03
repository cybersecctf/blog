
from Crypto.Util.number import long_to_bytes
def solve(position,len=207,type="byte"):
 bin_sequence = ["0"] * len
 for position in positions:
    bin_sequence[206 - position] = "1"
 if type=="binary":
  return "".join(bin_sequence)
 s=int("".join(bin_sequence), 2)
 if type=="long":
   return s 
 return long_to_bytes(s)#default is bytes
if __name__ == "__main__" :
 positions = [206, 205, 202, 201, 198, 197, 195, 194, 190, 189, 184, 182, 181, 178, 177, 176, 174, 173, 172, 171, 169, 168, 166, 165, 164, 157, 156, 150, 149, 147, 146, 142, 141, 140, 139, 136, 134, 133, 131, 130, 129, 126, 125, 123, 122, 121, 120, 118, 117, 115, 114, 112, 109, 108, 104, 102, 101, 96, 94, 93, 91, 90, 86, 85, 84, 81, 80, 78, 76, 75, 74, 73, 72, 69, 68, 66, 62, 61, 60, 57, 53, 52, 49, 48, 46, 44, 43, 42, 41, 40, 38, 37, 35, 33, 32, 29, 28, 21, 20, 14, 13, 11, 10, 6, 5, 4, 3, 2, 0]
 print(solve(positions,207))


