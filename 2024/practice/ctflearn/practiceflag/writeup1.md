 

<!DOCTYPE html>
<html>
 
<body>
    <h1>Practice Flag---ctflearn  Writeup </h1>

    <h2>Challenge Description</h2>
    <p> This is what a challenge on CTFlearn looks like. Each challenge has a flag, which is the key to solving it.

We've gone ahead and given you the flag for this challenge. As challenges get harder the flags will be more difficult to find.

Try inputting the flag: CTFlearn{4m_1_4_r3al_h4ck3r_y3t}

Don't forget to join our discord to ask questions and learn with thousands of others!
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>copy and past flag simply(in this challenge) or for inspect flag in big site
use this python code

<pre>
import blog
from bs4 import BeautifulSoup
import requests
def solve(url, word=""):
    # inspect  word in url
 results=[]
 resp = requests.get(url)

 # get the response text. in this case it is HTML
 html = resp.text
 for line in html.splitlines() : 
      if search in line:
        results.append(line)
 return results
if __name__ == "__main__" :
  print(solve("https://ctflearn.com/challenge/125","CTFlearn{"))
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlearn{4m_1_4_r3al_h4ck3r_y3t}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge forcopy and past flag and inspect in web</p>

</body>
</html>
