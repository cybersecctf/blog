
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
from bs4 import BeautifulSoup
import requests
import webbrowser
def solve(url, word=""):
    # inspect  word in url
 if not "http" in url:
   url="https://"+url
 if word=="":
  webbrowser.open(url)
  return
 results=[]
 resp = requests.get(url)

 # get the response text. in this case it is HTML
 html = resp.text
 for line in html.splitlines() : 
      if word in line:
        results.append(line)
 return "\n".join(results)
if __name__ == "__main__" :
  print(solve("https://ctflearn.com/challenge/125","CTFlearn{"))
