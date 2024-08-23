<title>Where Can My Robot Go?- ctflearn</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Where Can My Robot Go?- ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> Where do robots find what pages are on a website?

Hint:

What does disallow tell a robot?
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
       robots on website are in home address/robots.txt or can use this code for get robots.txt on any address if forget it
<pre>
#python
import requests,sys

def check_robots_txt(url):
    
            
    robots_url = "http://"+url.split('//')[1].split('/')[0] + '/robots.txt'
    print(robots_url)
    response = requests.get(robots_url)
    if response.status_code == 200:
        print(response.text) 
        return True
    else:
        return False

# Usage
url = 'https://ctflearn.com/challenge/107'
if len(sys.argv)>1:
    url=sys.argv[1]
print(check_robots_txt(url))

</pre>
 and get this text 
<pre>
http://ctflearn.com/robots.txt

        User-agent: *<br>
        Disallow: /70r3hnanldfspufdsoifnlds.html
</pre>      
    disallow are url of site that not listed in search engines so go to 
http://ctflearn.com/70r3hnanldfspufdsoifnlds.html and get flag
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlearn{r0b0ts_4r3_th3_futur3}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for find robbots on site</p>
</body>
</html>

