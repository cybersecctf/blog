import requests

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
print(check_robots_txt(url))