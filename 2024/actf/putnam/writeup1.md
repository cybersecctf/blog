<title>putnam- angstromctf2024</title>

<!DOCTYPE html>
<html>

<body>
    <h1>putnam- angstromctf2024</h1>

    <h2>Challenge Description</h2>
    <p> Solve the putnam, get the flag. Easy right?

Connect to it at nc challs.actf.co 31337
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
 we use this for connect stable to nc challs.actf.co 31337 and get flag and add sum 
in this challenge you can do manually by hand but not alway:) in some challenges use random number
and have random results 
<pre>
from pwn import *
import blog
# Set up pwntools for the correct architecture
context.update(arch='i386')
exe = 'otp.py'

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141


def local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

def remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return local(argv, *a, **kw)
    else:
        return remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB

def solve(host,port,recvutill):
 io = start()
 s=io.recvuntil(recvutill)
 x=str(s).split("=")
 x1,x2=x[0].split('+')
 x1 = int(x1[2:-1])
 x2 = int(x2)
 print(x1,x2)
 io.send( str(x1+x2)+"\n")
 print(io.recvall())
if __name__ == "__main__" :
 host =blog.set('challs.actf.co',1)
 port = blog.set( 31337,2)
 rec = blog.set( "\n",3)
 solve(host,port,rec)
</pre>
 
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">actf{just_a_tad_easier_than_the_actual_putnam} 
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for connect to nc and find sum number </p>
</body>
</html>

