
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
def decimal_to_ascii(decimal_sequence: list):
    return "".join([chr(decimal) for decimal in decimal_sequence]).encode()

def solve(sequence,hint,hint_suffix = b"}"):
 xor_hint_result = [seq ^ h for seq, h in zip(sequence, hint)]
 xor_hint_suffix_result = [sequence[-1] ^ hint_suffix[0]]
 xor_hint_total_result = xor_hint_result + xor_hint_suffix_result
 extended_key = bytes(decimal_to_ascii(xor_hint_total_result)) * 3
 return decimal_to_ascii([key ^ char for key, char in zip(extended_key, sequence)])
if __name__ == "__main__" :

 sequence = blog.set(b"\t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e",1)
 hint =blog.set( b"ctflearn{",2)
 hint_suffix = blog.set(b"}",3)
 print(solve(sequence,hint,hint_suffix))
