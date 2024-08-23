<title>Deep stego in the office- spcsctf</title>
def 
<!DOCTYPE html>
<html>

<body>
    <h1>Deep stego in the office- spcsctf</h1>

    <h2>Challenge Description</h2>
    <p> 
We hide the flag in the standard way. Almost the same as in any type of file


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


