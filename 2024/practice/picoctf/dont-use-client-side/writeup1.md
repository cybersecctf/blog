<title>picoctf2019- dont-use-client-side</title>

<!DOCTYPE html>
<html>
<head>
  
<body>
    <h1>picoctf2019- dont-use-client-side</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: ALEX FULTON/DANNY

Description
Can you break into this super secure portal? https://jupiter.challenges.picoctf.org/problem/37821/ (link) or http://jupiter.challenges.picoctf.org:37821
 
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
         client side in ctf quetion means scripts user can see  and check
         them but serverside is harder to find by hacker becaouse is in ctf or that site server  so open http://jupiter.challenges.picoctf.org:37821 and see script and find place  button becaouse button check verify flag and find this script
<pre>
if (checkpass.substring(0, split) == 'pico') {
      if (checkpass.substring(split*6, split*7) == 'a3c8') {
        if (checkpass.substring(split, split*2) == 'CTF{') {
         if (checkpass.substring(split*4, split*5) == 'ts_p') {
          if (checkpass.substring(split*3, split*4) == 'lien') {
            if (checkpass.substring(split*5, split*6) == 'lz_1') {
              if (checkpass.substring(split*2, split*3) == 'no_c') {
                if (checkpass.substring(split*7, split*8) == '9}') {
                  alert("Password Verified")
                  }
                }
              }
      
            }
          }
        }
      }
    }
    else {
      alert("Incorrect password");
    }

</pre>
       if our flag was correct button alert Password Verifiedso inspect script in this order 0, split,split*2...... and get flag and yes was correct
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{no_clients_plz_1a3c89}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for   client side attack and javascript</p>
</body>
</html>
