
<!DOCTYPE html>
<html>

<body>
    <h1>lactf2024- web/terms-and-conditions</h1>

    <h2>Challenge Description</h2>
    <p> web/terms-and-conditions
aplet123

Welcome to LA CTF 2024! All you have to do is accept the terms and conditions and you get a flag!

https://terms-and-conditions.chall.lac.tf
 
</p>

    <h2>Solution Approach</h2>
    
    <ol>
        <li> i open website and see a button that can't accept it and move with mouse and should accept and get flag </li>
 <img src=" https://phantom1ss.github.io/blog/2024/lactf2024/termsandconditions/web.png" alt="ctf quetion web" class="inline"/>

    so i open site and see script code was like this
<pre><code>
 
            const accept = document.getElementById("accept");
            document.body.addEventListener("touchstart", (e) => {
                document.body.innerHTML = "<iv><h 1>NO TOUCHING ALLOWED</h 1></d iv>";
            });
            let tx = 0;
            let ty = 0;
            let mx = 0;
            let my = 0;
            window.addEventListener("mousemove", function (e) {
                mx = e.clientX;
                my = e.clientY;
            });
            setInterval(function () {
                const rect = accept.getBoundingClientRect();
                const cx = rect.x + rect.width / 2;
                const cy = rect.y + rect.height / 2;
                const dx = mx - cx;
                const dy = my - cy;
                const d = Math.hypot(dx, dy);
                const mind = Math.max(rect.width, rect.height) + 10;
                const safe = Math.max(rect.width, rect.height) + 25;
                if (d < mind) {
                    const diff = mind - d;
                    if (d == 0) {
                        tx -= diff;
                    } else {
                        tx -= (dx / d) * diff;
                        ty -= (dy / d) * diff;
                    }
                } else if (d > safe) {
                    const v = 2;
                    const offset = Math.hypot(tx, ty);
                    const factor = Math.min(v / offset, 1);
                    if (offset > 0) {
                        tx -= tx * factor;
                        ty -= ty * factor;
                    }
                }
                accept.style.transform = `translate(${tx}px, ${ty}px)`;
            }, 1);
            let width = window.innerWidth;
            let height = window.innerHeight;
       <a href="https://phantom1ss.github.io/blog/2024/lactf2024/termsandconditions/Document.html">full code on this file</a>
</code></pre>
i remove this code contain touchstart and mouse move on here after saved page offline 
<pre><code>
   document.body.addEventListener("touchstart", (e) => {
                document.body.innerHTML = "< div><h 1>NO TOUCHING ALLOWED</h 1></ div>";
            });
            let tx = 0;
            let ty = 0;
            let mx = 0;
            let my = 0;
            window.addEventListener("mousemove", function (e) {
                mx = e.clientX;
                my = e.clientY;
            });
</code></pre>
and click button and get flag
 <img src=" https://phantom1ss.github.io/blog/2024/lactf2024/termsandconditions/flag.png" alt="ctf quetion flag" class="inline"/>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">lactf{that_button_was_definitely_not_one_of_the_terms}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on develper tools in in chrome and web exploitations</p>
</body>
</html>


 

