<title>I'm a dump-ctflearn</title>

<!DOCTYPE html>
<html>

<body>
    <h1>I'm a dump-ctflearn</h1>

    <h2>Challenge Description</h2>
    <p>The keyword is hexadecimal, and removing an useless H.E.H.U.H.E. from the flag. The flag is in the format CTFlearn{*}


 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        it is elf  file that  dump of it can be accessible by cat but for professional analysis  use another command
when use cat 
<pre>
$cat $1
</pre>
can see <pre>CTFlearnH�{fl4ggyfH�E�H�U�H�E�l4g}H�E�H�E��H�E�dH3%</pre>in midle of text dump
h e means hex and if delete H� and E� and U�.... can get flag

       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlearn{fl4ggyfl4g}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on dump file and cat and linux </p>
</body>
</html>

