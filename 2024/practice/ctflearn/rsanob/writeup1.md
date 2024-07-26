 
<!DOCTYPE html>
<html>
 
<body>
    <h1>RSA Noob--ctflearn  Writeup </h1>

    <h2>Challenge Description</h2>
    <p> These numbers were scratched out on a prison wall. Can you help me decode them? https://mega.nz/#!al8iDSYB!s5olEDK5zZmYdx1LZU8s4CmYqnynvU_aOUvdQojJPJQ
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>we open attached file and see this text
<code>

</code> 
that are nsa and so solve this vars with this code
<pre>
import blog
def solve(n,e,c):
 return blog.solveup("rsa",n,e,c)
if __name__ == "__main__" :
 e= 1
 c=9327565722767258308650643213344542404592011161659991421
 n= 245841236512478852752909734912575581815967630033049838269083
 print(solve(n,e,c))
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{more_than_m33ts_the_3y3657BaB2C}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on develper tools in in chrome and web exploitations</p>

</body>
</html>
