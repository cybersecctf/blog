
<!DOCTYPE html>
<html>
 <title>practice picoCTF 2019- Insp3ct0r Challenge Writeup</title> 
<body>
    <h1>practice picoCTF 2019- Insp3ct0r Challenge Writeup</h1>

    <h2>Challenge Description</h2>
    <p>AUTHOR: SYREAL
web exploitation
Description
AUTHOR: ZARATEC/DANNY

Description
Kishor Balan tipped us off that the following code may need inspection: https://jupiter.challenges.picoctf.org/problem/41511/ (link) or http://jupiter.challenges.picoctf.org:41511
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        <li>open web right click on inspect(or other ways on your browser) and go to developer tools on your browser </li>
       <li>click on element and see source this is first part of flag then got to source and page and second and third part of flag is there
<pre>
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
from collections import deque

def solve(url, search_terms):
    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text

        # Split content into lines and search for each term
        lines = content.splitlines()
        for line_number, line in enumerate(lines, start=1):
            for term in search_terms:
                if re.search(term, line, re.IGNORECASE):
                    print(f"Found '{term}' in {url}, line {line_number}: {line.strip()}")
                    break  # Avoid duplicate lines if multiple terms match

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

def solve(base_url, search_terms, max_urls=20):
    try:
        visited = set()  # To keep track of visited URLs
        queue = deque([base_url])  # Queue for BFS crawling
        count = 0  # Counter to limit the number of URLs crawled

        while queue and count < max_urls:
            url = queue.popleft()
            if url in visited:
                continue
            visited.add(url)
            count += 1

            try:
                # Fetch the page content
                response = requests.get(url)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, 'html.parser')

                # Search for terms in the current page content
                print(f"\nSearching for {search_terms} in {url}:")
                content = soup.get_text()
                lines = content.splitlines()
                for line_number, line in enumerate(lines, start=1):
                    for term in search_terms:
                        if re.search(term, line, re.IGNORECASE):
                            print(f"Found '{term}' in {url}, line {line_number}: {line.strip()}")
                            break  # Avoid duplicate lines if multiple terms match

                # Check comments and meta tags
                for comment in soup.find_all(string=lambda text: isinstance(text, str) and any(re.search(term, text, re.IGNORECASE) for term in search_terms)):
                    print(f"Found in comment: {comment.strip()}")
                for meta in soup.find_all('meta'):
                    if any(re.search(term, meta.get('content', ''), re.IGNORECASE) for term in search_terms):
                        print(f"Found in meta tag: {meta}")

                # Extract all URLs from the page
                for tag in soup.find_all(['a', 'link', 'script', 'img', 'iframe']):
                    if tag.get('href'):
                        new_url = urljoin(base_url, tag['href'])
                        if new_url not in visited and new_url.startswith(base_url):
                            queue.append(new_url)
                    if tag.get('src'):
                        new_url = urljoin(base_url, tag['src'])
                        if new_url not in visited and new_url.startswith(base_url):
                            queue.append(new_url)

            except requests.exceptions.RequestException as e:
                print(f"Error fetching {url}: {e}")

    except Exception as e:
        print(f"Error during crawling: {e}")

# Example usage
if __name__=='__main__':
 website_url = "https://jupiter.challenges.picoctf.org/problem/9670/"
 search_terms = "flag", "part", "secret", "search"  # Add any words you want to search for
 solve(website_url, search_terms, max_urls=20)  # Limit to 20 URLs
 
</pre>
  </li>
    
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?832b0699}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on develper tools in in chrome and web exploitations</p>
</body>
</html>
