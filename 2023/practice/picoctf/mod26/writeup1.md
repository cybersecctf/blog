<!DOCTYPE html>
<html>
<head>
    <style>
      <title>picopractice(2021)- mode 26 Challenge Writeup</title>
    </style>
</head>
<body>
    <h1>picopractice(2021)- mode 26 Challenge Writeup</h1>

    <h2>Challenge Description</h2>
    <p>Cryptography can be easy, do you know what ROT13 is? cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_GYpXOHqX}
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        <li>use online tolls but for more pwn and rev and challenge like that is better use python code</li>
        <pre>import codecs
print(codecs.encode("cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_GYpXOHqX}", "rot_13"))

  </pre>
               

      
    </ol>

    <h2>Flag</h2>
    <p class="flag">picoCTF{next_time_I'll_try_2_rounds_of_rot13_TLcKBUdK}</p>

    <h2>Conclusion</h2>
    <p>easy ctf for cryptography and rot13 with  python code</p>
</body>
</html>
