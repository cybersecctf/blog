import requests
import jwt

# URL of the Flask app
url = "https://i-spy.chall.lac.tf/" 

# Secret key used for encoding/decoding tokens
secret_key = "in page"

# Function to decode the token
def decode_token(token):
    try:
        decoded = jwt.decode(token, secret_key, algorithms=['HS256'])
        return decoded['value']
    except:
        return None
def solve():
 # Step 1: Get the HTML source code
 response = requests.get(url)
 print("HTML Source Code:", response.text)

 # Step 2: Get the JavaScript console logs (this requires a browser environment, not directly possible with requests)

 # Step 3: Get the stylesheet
 response = requests.get(f"{url}/styles.css")
 print("Stylesheet:", response.text)

 # Step 4: Get the JavaScript code
 response = requests.get(f"{url}/thingy.jss")
 print("JavaScript Code:", response.text)

 # Step 5: Get the header
 response = requests.get(url)
 x_token = response.headers.get("X-Token")
 print("Header X-Token:", x_token)

 # Step 6: Get the cookie
 cookies = response.cookies
 stage_token = cookies.get("stage_token")
 decoded_stage_token = decode_token(stage_token)
 print("Cookie stage_token:", decoded_stage_token)

 # Step 7: Get the robots.txt
 response = requests.get(f"{url}/robots.txt")
 print("robots.txt:", response.text)

 # Step 8: Get the sitemap.xml
 response = requests.get(f"{url}/sitemap.xml")
 print("sitemap.xml:", response.text)
 
 # Step 9: Make a DELETE request
 response = requests.delete(url)
 print("DELETE Request Response:", response.text)
if __name__ == "__main__":
 solve()