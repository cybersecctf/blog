<!DOCTYPE html>
<html>

<body>
    <h1>ASCII- cryptohack</h1>

    <h2>Challenge Description</h2>
    <p>ASCII is a 7-bit encoding standard which allows the representation of text using the integers 0-127.

Using the below integer array, convert the numbers to their corresponding ASCII characters to obtain a flag.

[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

 In Python, the chr() function can be used to convert an ASCII ordinal number to a character (the ord() function does the opposite).
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
run this code and get flag
<pre>
#python
import blog
def solve(nums):
  print("".join((chr(o) for o in nums)))
if __name__ == "__main__" :
  
  nums=blog.set("[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]",1)
  solve(nums)
 
</pre>
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">crypto{ASCII_pr1nt4bl3}

</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for  convert decimal to ascii</p>
</body>
</html>

