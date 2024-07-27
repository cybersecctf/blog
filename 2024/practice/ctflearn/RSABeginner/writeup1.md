 

<!DOCTYPE html>
<html>
 
<body>
    <h1>RSA Beginner--ctflearn </h1>

    <h2>Challenge Description</h2>
    <p> I found this scribbled on a piece of paper. Can you make sense of it? https://mega.nz/#!zD4wDYiC!iLB3pMJElgWZy6Bv97FF8SJz1KEk9lWsgBSw62mtxQg
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>we open  link and see 3 rsa parameters  e=3,c=219878849218803628752496734037301843801487889344508611639028,n= 245841236512478852752909734912575581815967630033049838269083
this is rsa attack    “Low Public Exponent Attack”. where e is small around 3 and can solve with code
<pre>
import blog


def solve(n,e,c):
    return blog.solveup("rsa",n,e,c)

if __name__ == "__main__" :
  e=3
  c=219878849218803628752496734037301843801487889344508611639028
  n= 245841236512478852752909734912575581815967630033049838269083
  print(solve(n,e,c))
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">abctf{rs4_is_aw3s0m3}
</p>

    <h2>Conclusion</h2>
    <p>this is a medium chanllenge for work on  rsa easy attacks</p>

</body>
</html>
