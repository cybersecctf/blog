
<!DOCTYPE html>
<html>

<body>
    <h1>Magikarp Ground Mission- picoctf2021</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: SYREAL

Description
Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `abcba9f7`
Additional details will be available after launching your challenge   <button id="instance">instance</button>
    <div id="content" style="display: none;">
        This content will be shown/hidden.
    </div>
</p>
merge
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
         go to terminal follow this process with ls and cat command
<pre>
$ls
$ls -lah for show all files and  permissions
</pre>
 and get flag in three part in different directories.full process is here
<pre>
┌──(kali㉿kali)-[~/Desktop/blog]
└─$ ssh ctf-player@venus.picoctf.net -p 58791

The authenticity of host '[venus.picoctf.net]:58791 ([3.131.124.143]:58791)' can't be established.
ED25519 key fingerprint is SHA256:P1f6h95BrSVnJbm2AKhphfHHGEyAeThib/rN/AwKs24.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[venus.picoctf.net]:58791' (ED25519) to the list of known hosts.
ctf-player@venus.picoctf.net's password: 
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 5.4.0-1041-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ctf-player@pico-chall$ ls -lah
total 16K
drwxr-xr-x 1 ctf-player ctf-player 4.0K Mar 16  2021 .
drwxr-xr-x 1 ctf-player ctf-player 4.0K Mar 26 16:27 ..
-rw-r--r-- 1 ctf-player ctf-player   14 Mar 16  2021 1of3.flag.txt
-rw-r--r-- 1 ctf-player ctf-player   56 Mar 16  2021 instructions-to-2of3.txt
ctf-player@pico-chall$ cat 10f3.flag.txt
cat: 10f3.flag.txt: No such file or directory
ctf-player@pico-chall$ cat 1of3.flag.txt
picoCTF{xxsh_
ctf-player@pico-chall$ ls ..
3of3.flag.txt  drop-in
ctf-player@pico-chall$ ls .
1of3.flag.txt  instructions-to-2of3.txt
ctf-player@pico-chall$ cat instructions-to-2of3.txt
Next, go to the root of all things, more succinctly `/`
ctf-player@pico-chall$ cd  /
ctf-player@pico-chall$ 
ctf-player@pico-chall$ ls
2of3.flag.txt  etc                       lib64  proc  srv  var
bin            home                      media  root  sys
boot           instructions-to-3of3.txt  mnt    run   tmp
dev            lib                       opt    sbin  usr
ctf-player@pico-chall$ cad 2of3.flag.txt
-bash: cad: command not found
ctf-player@pico-chall$ cat 2of3.flag.txt
0ut_0f_\/\/4t3r_
ctf-player@pico-chall$ cd home
ctf-player@pico-chall$ ls
ctf-player
ctf-player@pico-chall$ cd ctf-player
ctf-player@pico-chall$ ls
3of3.flag.txt  drop-in
ctf-player@pico-chall$ cat 3of3.flag.txt
21cac893}

</pre>
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{xxsh_0ut_0f_\/\/4t3r_21cac893}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on  linux  and ls and cat commands</p>
</body>
</html>

