
<!DOCTYPE html>
<html>
<body>
<h1>WPA-ing Out- picoGym Exclusive</h1>

<h2>Challenge Description</h2>
<p> Description
I thought that my password was super-secret, but it turns out that passwords passed over the AIR can be CRACKED, especially if I used the same wireless network password as one in the rockyou.txt credential dump.
Use this<a href="https://artifacts.picoctf.net/c/41/wpa-ing_out.pcap">'pcap file'</a>  and the rockyou wordlist. The flag should be entered in the picoCTF{XXXXXX} format.

</p>
this challenge  
<h2>Solution Approach</h2>
<p>Here are the steps we took to solve the challenge:</p>
<ol>
 on base of instruction in challenge we use this command for get password from pcap file if have rockyou.txt
<pre>
$aircrack-ng -w /usr/share/wordlists/rockyou.txt wpa-ing_out.pca
</pre>
if in your linux have /usr/share/wordlists/rockyou.gz.txt then you should use <a href="https://www.geeksforgeeks.org/how-to-extract-rockyou-txt-gz-file-in-kali-linux/">this</a> command in terminal as root for unzip it 
<pre>
$gzip -d /usr/share/wordlists/rockyou.gz.txt
</pre>
and get flag.
 <img src=" https://phantom1ss.github.io/blog/2024/practice/picoctf/WPA-ingOut/aircrack.png" alt="aircrack in linux kali" class="inline"/>

</ol>
<br>
<h2>Flag</h2>
<p class="flag">picoCTF{mickeymouse}


<h2>Conclusion</h2>
<p>this is a  easy challenge for get password from pcap file</p>

</body>
</html>


 


