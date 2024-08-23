<title>web/dicedicegoose-dicectf 2024</title>

<!DOCTYPE html>
<html>

<body>
    <h1>web/dicedicegoose-dicectf 2024</h1>

    <h2>Challenge Description</h2>
    <p>Follow the leader.
ddg.mc.ax:https://ddg.mc.ax/

</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        <li> let see javascript win code<pre> function win(history) {
    const code = encode(history) + ";" + prompt("Name?");

    const saveURL = location.origin + "?code=" + code;
    displaywrapper.classList.remove("hidden");

    const score = history.length;

    display.children[1].innerHTML = "Your score was: <b>" + score + "</b>";
    display.children[2].href =
        "https://twitter.com/intent/tweet?text=" +
        encodeURIComponent(
            "Can you beat my score of " + score + " in Dice Dice Goose?",
        ) +
        "&url=" +
        encodeURIComponent(saveURL);

    if (score === 9) log("flag: dice{pr0_duck_gam3r_" + encode(history) + "}");
}
</pre>
it seems we can win when get score and remore if not working for me so should modify hostory or simulate key press
if in console type <pre>history = [[[0,1],[9,9]] ,[[1,1],[9,8]] ,[[2,1],[9,7]] ,[[3,1],[9,6]] ,[[4,1],[9,5]] ,[[5,1],[9,4]] ,[[6,1],[9,3]] ,[[7,1],[9,2]] ,[[8,1],[9,1]]]</pre>
and then type <pre>win(history)</pre> can see flag in console .[0,1],[9,9]] is location of tas and gaoose and should reach each eather 

        <img src=" https://phantom1ss.github.io/blog/2024/practice/dicectf/dicedicegoose/console1.png" alt="ctf quetion image" class="inline"/>
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">dice{pr0_duck_gam3r_AAEJCQEBCQgCAQkHAwEJBgQBCQUFAQkEBgEJAwcBCQIIAQkB}
</p>

    <h2>Conclusion</h2>
    <p>this is a web exploitation challenge for work with javascript and html/p>
</body>
</html>


