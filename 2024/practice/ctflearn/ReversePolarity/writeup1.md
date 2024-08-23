<title>Reverse Polarity- ctflearn</title>

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
import blog
def solve(s,operation="decode",length=8):
   result=""
   if operation=="decode":
    result= ''.join(chr(int(s[i*length:i*length+length],2)) for i in range(len(s)//length))
   else:
    result =   int(bin(s)[2:])
   return result
if __name__ == "__main__" :
 X=blog.set("01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101",1,"str")
 print(solve(X))
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

