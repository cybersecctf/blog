
<!DOCTYPE html>
<html>

<body>
    <h1>what do with ppc- spcsctf</h1>

    <h2>Challenge Description</h2>
    <p> 
PPC (Professional Programming and Coding) - a competition to solve interactive problems.

The task is located on the server (executed in a remote terminal) and is available using the command

nc ip-adress port

however, it is not possible to solve it “manually” due to limitations in response time and/or the large number of repetitions.

A typical situation is that it is necessary to intercept data from a certain port and quickly respond to the content of this data.

How to deal with such tasks? We connect to the server, receive data from it on our computer, solve the problem, send a response, etc., until we receive the flag. Our flags are in the format grodno{0-9a-zA-Z!+-}

from time import sleep
import socket

sock = socket.socket()
sock.connect(("ip-adress", port))

while True:
     sleep(1)
    # get data from server
     data = sock.recv(1024).decode('utf-8')
    # check if there is already a flag there?
     if 'grodno{' in data:
         print(data)
         break
     task = f1(data) # extract task condition from data
     result = f2(task) # calculate the answer
    # send reply
     sock.send((str(result) + '\r\n').encode())

sock.close()
If everything is clear, enter the flag 0
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
understand this code and enter flag 0
<pre>
from time import sleep
import socket

sock = socket.socket()
sock.connect(("ip-adress", port))

while True:
     sleep(1)
    # get data from server
     data = sock.recv(1024).decode('utf-8')
    # check if there is already a flag there?
     if 'grodno{' in data:
         print(data)
         break
     task = f1(data) # extract task condition from data
     result = f2(task) # calculate the answer
    # send reply
     sock.send((str(result) + '\r\n').encode())

sock.close()
</pre>        
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">0
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work onsocket code and competetion style </p>
</body>
</html>


