
<!DOCTYPE html>
<html>

<body>
    <h1>Dachshud Atntacks- picoctf 2021</h1>

    <h2>Challenge Description</h2>
    <p> What if d is too small?

</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
       we run nc and this n and c and e values see info .when search  search google it comes with  <"https://en.wikipedia.org/wiki/Wiener%27s_attack">Wiener's attack </a> and search for code and found this with nc values and get flag after run it
<pre>
#python
from Crypto.Util.number import *
import owiener as p
from typing import Tuple, Iterator, Iterable, Optional
 
 
# Given value of n

n= 131578310029690167610031089254041332671184856622543243935622206955957641501082056807318692504416189624538541458978000853878024596610552752422068838128189550974133903368650298751349692992965393956322900921482180432999563659475736235922635321530359820067046966352099628624384929864587223809986189205500308278009
e= 56082788500541782554336418273877225568901437036823413673027101055728677759602011802300948905557131587134953265291125554913622575529862462752460798672403038560145024851853536307774690259298769734905057242663548104409231404637810222449450751718848892907319455674849665466448644610215810863811669023836730961729
c= 11631917238001568806242205168940882129349881459029178097116508436193438614755263146671726586575884553770854992313785032680292716618202672381042132168204326353571693389527526779007619745189450737678922431560828814178662305464293207796918054012576337648529098641087918185355247181328990224101472824907382968879
d =p. attack(e,n)###predicting d from wiener attack

if len(sys.argv)>1:
    n=sys.argv[1]
if len(sys.argv)>2:
    e=sys.argv[2]
if len(sys.argv)>3:
    c=sys.argv[3]
if d is None:
 print("Failed")
else:
 print("Hacked d={}".format(d))
M = pow(c,d,n)
print(long_to_bytes(M))
</pre>
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{proving_wiener_1146084}
</p>

    <h2>Conclusion</h2>
    <p>this is a     easy chanllenge for  work on rsa and Wiener's attack and small d and calculate it</p>
</body>
</html>


