<!DOCTYPE html>
<html>
<head>
<title>
picopractice(2021)- Python  Wrangling Challenge Writeup
</title>
</head>
<body>
    <h1>picopractice(2021)- Python  Wrangling Challenge Writeup</h1>

    <h2>Challenge Description</h2>
    <p>Python scripts are invoked kind of like programs in the Terminal... Can you run this Python script using this password to get the flag?
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        <li>i save links...</li>
        <li>analysis python scripts and decide use this command </li>
           <li> python ende.py -d flag.txt.en ask for password get it from pw.txt then show me flag after it</li      
             <li>or on base of this code< pre> if sys.argv[1] == "-e":
    if len(sys.argv) < 4:
        sim_sala_bim = input("Please enter the password:")
    else:
        sim_sala_bim = sys.argv[3] 
</pre>
use password as forth argument after python like from
<pre>python ende.py -d flag.txt.en dbd1bea4dbd1bea4dbd1bea4dbd1bea4</pre>
      
    </ol>

    <h2>Flag</h2>
    <p class="flag">picoCTF{4p0110_1n_7h3_h0us3_dbd1bea4}</p>

    <h2>Conclusion</h2>
    <p>easy ctf for general python skills and use  them  with  linux command</p>
     <p>use more on reversing and other code related  challenges
</body>
</html>
