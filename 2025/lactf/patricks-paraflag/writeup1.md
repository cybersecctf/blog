<title>lactf2025---rev/patricks-paraflag  Writeup </title>
 

<!DOCTYPE html>
<html>
 
<body>
    <h1>lactf2025---rev/patricks-paraflag  Writeup  </h1>

    <h2>Challenge Description</h2>
    <p>  I was going to give you the flag, but I dropped it into my parabox, and when I pulled it back out, it got all scrambled up!

Can you recover the flag?
downloads

<a href="https://chall-files.lac.tf/uploads/05b449309cc237871116bcb53346db413e902ddec7515eaad904ac0c45726f1d/patricks-paraflag">patricks-paraflag</a>
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>
we run file see need input for flag and check if flag and even length is same 
say is correect
<code>
└─$ ./patricks-paraflag
What do you think the flag is? flag
Bad length >:(
                 
</code>
we open ghidra and check code and see it<img src="https://cybersecctf.github.io/blog/2025/lactf/patricks-paraflag/patrick1.PNG" alt="ctf writeup" width="500" height="600"/>
we see that commare text with target and  The user input is split into two halves.
The first half is interleaved with the targetand then result iscompare target if is equal say correct
if click on target in ghidra and then address in end see image below
<img src="https://cybersecctf.github.io/blog/2025/lactf/patricks-paraflag/patrick2.PNG" alt="ctf writeup" width="500" height="600"/>
that is target and modify it to get flag via reversing upper process in below python code
<pre>
def solve(target):
    # Length of the target
    target_len = len(target)
    
    # Validate that target length is even
    if target_len % 2 != 0:
        raise ValueError("Target length must be even.")
    
    # Half length of the target
    half_len = target_len // 2
    
    # Unscramble the target
    part1 = target[0::2]  # Characters at even indices
    part2 = target[1::2]  # Characters at odd indices
    
    # Reconstruct the original input
    inp = part1 + part2
    return inp

# Given target
target = "l_alcotsft{_tihne__ifnlfaign_igtoyt}"

# Unscramble the flag
flag = unscramble_flag(target)
print(f"Recovered Flag: {flag}")

</pre>
</li>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">lactf{the_flag_got_lost_in_infinity}

</p>

    <h2>Conclusion</h2>
    <p>this is a easy chanllenge for reverse binary with ghidra </p>

</body>
</html>
