
<!DOCTYPE html>
<html>

<body>
    <h1>IntroToBurp-picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: NANA AMA ATOMBO-SACKEY & SABINE GISAGARA

Description
Additional details will be available after launching your challenge instance.
-----------------------------------------------------------------------------
Try <a href="http://titan.picoctf.net:61369/">here</a> to find the flag
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
open burpsuit(on base of hints) and see registeration page 
 <img src=" https://phantom1ss.github.io/blog/2024/pico2024/IntroToBurp/register.png" alt="register" class="inline"/>
    add some random detail and click register.
and go to next with click on forward on proxy in this part below(via browser configured on burpsuit)
 <img src=" https://phantom1ss.github.io/blog/2024/pico2024/IntroToBurp/forward1.png" alt="forward" class="inline"/>
and go to page say enter otp
 <img src=" https://phantom1ss.github.io/blog/2024/pico2024/IntroToBurp/otp.png" alt="otp" class="inline"/>
enter random otp say is incorrect but after some trys see if remove last line and click forward
 <img src=" https://phantom1ss.github.io/blog/2024/pico2024/IntroToBurp/lastlineremove.png" alt="remove last line" class="inline"/>
will see page have flag
<img src=" https://phantom1ss.github.io/blog/2024/pico2024/IntroToBurp/final.png" alt="flag" class="inline"/>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{#0TP_Bypvss_SuCc3$S_6bffad21}
</p>

    <h2>Conclusion</h2>
    <p>this is a    easy chanllenge for work on  burpsuit and register page and otp</p>
</body>
</html>








 