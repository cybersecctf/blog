
<!DOCTYPE html>
<html>

<body>
    <h1>Binary Search-picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: JEFFERY JOHN

Description
Want to play a game? As you use more of the shell, you might be interested in how they work! Binary search is a classic algorithm used to quickly find an item in a sorted list. Can you find the flag? You'll have 1000 possibilities and only 10 guesses.
Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics. Practicing the fundamentals manually might help you in the future when you have to write your own tools!
You can download the challenge files here:

<a href="https://artifacts.picoctf.net/c_atlas/4/challenge.zip">  challenge.zip</a>
Additional details will be available after launching your challenge instance.
-----------------------------------------------------------------
Connect with the challenge instance here:

nc mimas.picoctf.net  52113 
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
      i downloa dfile and unzip it and go to file
<p id="code1">
$wget https://artifacts.picoctf.net/c_atlas/4/challenge.zip
$unzip challenge.zip
$cd home
$cd ctf-player
$cd drop-in
$./guessing_game.sh
 </p>
       a saple easy approach is guess number can get flag after some trys
<pre>
 ssh -p 63159 ctf-player@atlas.picoctf.net

ctf-player@atlas.picoctf.net's password: 
Welcome to the Binary Search Game!
I'm thinking of a number between 1 and 1000.
Enter your guess: 500
Higher! Try again.
Enter your guess: 900
Lower! Try again.
Enter your guess: 700
Higher! Try again.
Enter your guess: 800
Lower! Try again.
Enter your guess: 720
Higher! Try again.
Enter your guess: 750
Higher! Try again.
Enter your guess: 770
Higher! Try again.
Enter your guess: 790
Lower! Try again.
Enter your guess: 780
Lower! Try again.
Enter your guess: 772
Congratulations! You guessed the correct number: 772
Here's your flag: picoCTF{g00d_gu355_ee8225d0}

</pre>
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{g00d_gu355_ee8225d0}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for binary search on server </p>
</body>
</html>


