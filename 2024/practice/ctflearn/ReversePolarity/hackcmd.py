import sys
def decode_string(s,base):
    return ''.join(chr(int(s[i*8:i*8+8],base)) for i in range(len(s)//8))
X="01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101"
base=2
if len(sys.argv)>1:
  X=sys.argv[1]
if len(sys.argv)>2:
  base=sys.argv[1]
print(decode_string(X,base))