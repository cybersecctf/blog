 

<!DOCTYPE html>
<html>
 
<body>
    <h1>Polycrypto--ctflearn </h1>

    <h2>Challenge Description</h2>
    <p> Polynomials are a very useful branch of mathematics. 
They can also hide secrets. Can you find what this one is hiding? https://mega.nz/#!mLJXWCIS!ZLpbPEGzhPevFeLGwUv6imuRTl19jiO5q-P7_dVaXoM https://en.wikipedia.org/wiki/Finite_field_arithmetic
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>when open link see this text 

<code>
f = x^206 + x^205 + x^202 + x^201 + x^198 + x^197 + x^195 + x^194 + x^190 + x^189 + x^184 + x^182 + x^181 + x^178 + x^177 + x^176 + x^174 + x^173 + x^172 + x^171 + x^169 + x^168 + x^166 + x^165 + x^164 + x^157 + x^156 + x^150 + x^149 + x^147 + x^146 + x^142 + x^141 + x^140 + x^139 + x^136 + x^134 + x^133 + x^131 + x^130 + x^129 + x^126 + x^125 + x^123 + x^122 + x^121 + x^120 + x^118 + x^117 + x^115 + x^114 + x^112 + x^109 + x^108 + x^104 + x^102 + x^101 + x^96 + x^94 + x^93 + x^91 + x^90 + x^86 + x^85 + x^84 + x^81 + x^80 + x^78 + x^76 + x^75 + x^74 + x^73 + x^72 + x^69 + x^68 + x^66 + x^62 + x^61 + x^60 + x^57 + x^53 + x^52 + x^49 + x^48 + x^46 + x^44 + x^43 + x^42 + x^41 + x^40 + x^38 + x^37 + x^35 + x^33 + x^32 + x^29 + x^28 + x^21 + x^20 + x^14 + x^13 + x^11 + x^10 + x^6 + x^5 + x^4 + x^3 + x^2 + 1
</code>
after try ways we see that if convert positions to binary 
in way that every position like 206 205 is 1 and then convert it to long and convert to to byte it 
give us flag after run this code
<pre>
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


</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">flag{p0lynom1als_4r3_k00l}
</p>

    <h2>Conclusion</h2>
    <p>this is a hard challenge for convert polynominal to binary and long and bytes</p>

</body>
</html>
