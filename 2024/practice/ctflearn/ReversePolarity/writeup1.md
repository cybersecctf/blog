
<!DOCTYPE html>
<html>

<body>
    <h1>Reverse Polarity- ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> I got a new hard drive just to hold my flag, but I'm afraid that it rotted. What do I do? The only thing I could get off of it was this: 01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
first i think i should reverse string but letter i found is about reverse base and polarity and use this code for convert base to text
<pre>
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
 
</pre>
       
    and get flag
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTF{Bit_Flippin}

</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work  convert base to text</p>
</body>
</html>

