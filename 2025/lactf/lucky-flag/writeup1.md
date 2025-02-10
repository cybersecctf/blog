<title>web/lucky-flag-lactf2025</title>

<!DOCTYPE html>
<html>

<body>
    <h1>web/lucky-flag-lact2025</h1>

    <h2>Challenge Description</h2>
    <p> Just click the flag :) <a href="https://lucky-flag.chall.lac.tf/">lucky-flag.chall.lac.tf</a>
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
we open link see page 
<img src=" https://cybersecctf.github.io/blog/2025/lactf/lucky-flag/luckyflag.PNG" alt="ctf quetion image" width="500" height="600" class="inline"/>
it seems click on right button and find flag but with many buttons see isn't possible so in reality should check script 
<code>
const $ = q => document.querySelector(q);
const $a = q => document.querySelectorAll(q);

const boxes = $a('.box');
let flagbox = boxes[Math.floor(Math.random() * boxes.length)];

for (const box of boxes) {
  if (box === flagbox) {
    box.onclick = () => {
      let enc = `"\\u000e\\u0003\\u0001\\u0016\\u0004\\u0019\\u0015V\\u0011=\\u000bU=\\u000e\\u0017\\u0001\\t=R\\u0010=\\u0011\\t\\u000bSS\\u001f"`;
      for (let i = 0; i < enc.length; ++i) {
        try {
          enc = JSON.parse(enc);
        } catch (e) { }
      }
      let rw = [];
      for (const e of enc) {
        rw['\x70us\x68'](e['\x63har\x43ode\x41t'](0) ^ 0x62);
      }
      const x = rw['\x6dap'](x => String['\x66rom\x43har\x43ode'](x));
      alert(`Congrats ${x['\x6aoin']('')}`);
    };
    flagbox = null;
  } else {
    box.onclick = () => alert('no flag here');
  }
};
</code>

that is xor code with 0x62 aqnd can use python code or javascript with console.log and print flag
this python code
<pre>
import ast

# Encrypted string (from the JavaScript code)
enc = "\\u000e\\u0003\\u0001\\u0016\\u0004\\u0019\\u0015V\\u0011=\\u000bU=\\u000e\\u0017\\u0001\\t=R\\u0010=\\u0011\\t\\u000bSS\\u001f"

# Convert the string with Unicode escapes into actual characters
decoded = enc.encode('utf-8').decode('unicode_escape')

# XOR each character with 0x62 and convert to the original character
flag = ''.join(chr(ord(c) ^ 0x62) for c in decoded)

# Print the decoded flag
print(f"Decoded Flag: {flag}")

</pre>  
    after running get flag that is here
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">lactf{w4s_i7_luck_0r_ski11}

</p>

    <h2>Conclusion</h2>
    <p>this is a    easy chanllenge for work on develper tools in in chrome and web exploitations and xor decoding in javascript or python</p>
</body>
</html>


 