
<!DOCTYPE html>
<html>

<body>
    <h1>Modern Gaius Julius Caesar- ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> One of the easiest and earliest known ciphers but with XXI century twist! Nobody uses Alphabet nowadays right? Why should you when you have your keyboard?

BUH'tdy,|Bim5y~Bdt76yQ
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
Modern Gaius Julius Caesar  and alphabet maybe means keyboard shift chipher that is use keyboard alphabet for shift number 
like caesar so use this code and get flag  CTFlearn{Cyb3r-Cae54r]
that should changed to have correct version of flag.
<pre>
#python
import sys,os
typekey="qwertyus"
ciphertext = "BUH'tdy,|Bim5y~Bdt76yQ"
if len(sys.argv)>1:
 ciphertext=sys.argv[1]
shift = 2  # Replace with the actual shift used
if len(sys.argv)>2:
 shift=int(sys.argv[2])
if len(sys.argv)>3:
 typekey=sys.argv[3] 
 
import subprocess

# Define the command as a list
command = ["python", "solve.py", ciphertext, str(shift), str(typekey)]

# Run the command
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Get the output and error (if any)
stdout, stderr = process.communicate()
# Print the output
print(stdout.decode())
# Print the error (if any)
if stderr:
    print(stderr.decode())

</pre>
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlearn{Cyb3r_Cae54r}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for keyboard shift cipher and crypto</p>
</body>
</html>

