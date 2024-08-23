<title>osctf2024-cyberquize Writeup </title>
 
<!DOCTYPE html>
<html>
 
<body>
    <h1>osctf2024-cyberquize Writeup </h1>

    <h2>Challenge Description</h2>
    <p> 100
Misc
My teacher assigned me this quiz and told me that I have to answer each question correctly otherwise I won't be able to pass the test. Can you help me? Pwease

Author: @5h1kh4r

nc 34.16.207.52 12345
</p>

    <h2>Solution Approach</h2>
<a href="">certificate of participate</a>
  <img src="https://cybersecctf.github.io/blog/2024/osctf/cyberquize/cert.png" alt="Girl in a jacket" width="100" height="100">
 
 <p>Here are the steps we took to solve the challenge:</p>
    <ol>  <a href="https://cybersecctf.github.io/blog/?q=cyberquize%20osctf2024">open full version here</a>
we connect nc and see al otof quetions and swer them correctly for get flag .careful for lowercase or uppercases
and at end see flag if not answered them one flag cant show should guess one of them if can't answer one or two..of them or use this pwn code:
<pre>
#python
import socket
import blog
# Predefined answers for the given questions
answers = {
    "What is the default port for HTTP?": "80",
    "Who invented the World Wide Web?": "Tim Berners-Lee",
    "What does DNS stand for?": "Domain Name System",
    "What is the process of converting data into a coded format called?": "Encryption",
    "What protocol is commonly used for secure communication over the internet?": "HTTPS",
    "What does SQL stand for?": "Structured Query Language",
    "What is a common type of attack that involves injecting malicious code into a website?": "SQL Injection",
    "What type of malware encrypts files and demands payment for their release?": "Ransomware",
    "What is the practice of disguising communication to appear as though it is coming from a trusted source?": "Spoofing",
    "What is a file called that contains a digital certificate?": "Certificate",
    "What term describes the attempt to gain sensitive information by disguising as a trustworthy entity?": "Phishing",
    "What is a network device that filters and monitors incoming and outgoing network traffic?": "Firewall",
    "What type of attack involves overwhelming a system with traffic to disrupt service?": "DDoS",
    "What is the primary protocol used for sending email over the internet?": "SMTP",
    "What does VPN stand for?": "Virtual Private Network",
    "What is the name of the vulnerability that allows arbitrary code execution in software?": "Buffer Overflow",
    "What is the term for a software update that fixes bugs and vulnerabilities?": "Patch",
    "What does MFA stand for in cybersecurity?": "Multi-Factor Authentication",
    "What is a tool that scans a network for open ports and services?": "Nmap",
    "What is the name of the secure file transfer protocol that uses SSH?": "SFTP",
    "What does XSS stand for in web security?": "Cross-Site Scripting"
}

def solve(host,port):
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        while True:
            data = s.recv(1024).decode()
            print(data)

            if "Answer the following" in data:
                continue

            # Extract the question
            question = data.strip().split("\n")[-1]

            if question in answers:
                answer = answers[question]
                print(f"Question: {question}")
                print(f"Answer: {answer}")
                s.sendall((answer + "\n").encode())

            if "Final flag:" in data:
                print("FLAG found!")
                break

if __name__ == "__main__":
 
 host=blog.set('34.16.207.52',1)
 port=blog.set(12345,2)
 solve(host,port)
</pre>
and result of runniong this code is:
<code>
Answer the following cybersecurity questions to reveal the flag:

What is the default port for HTTP? 
Question: What is the default port for HTTP?
Answer: 80
Correct! O____________________

Who invented the World Wide Web? 
Question: Who invented the World Wide Web?
Answer: Tim Berners-Lee
Correct! OS___________________

What does DNS stand for? 
Question: What does DNS stand for?
Answer: Domain Name System
Correct! OSC__________________

What is the process of converting data into a coded format called? 
Question: What is the process of converting data into a coded format called?
Answer: Encryption
Correct! OSCT_________________

What protocol is commonly used for secure communication over the internet? 
Question: What protocol is commonly used for secure communication over the internet?
Answer: HTTPS
Correct! OSCTF________________

What does SQL stand for? 
Question: What does SQL stand for?
Answer: Structured Query Language
Correct! OSCTF{_______________

What is a common type of attack that involves injecting malicious code into a website? 
Question: What is a common type of attack that involves injecting malicious code into a website?
Answer: SQL Injection
Correct! OSCTF{L______________

What type of malware encrypts files and demands payment for their release? 
Question: What type of malware encrypts files and demands payment for their release?
Answer: Ransomware
Correct! OSCTF{L3_____________

What is the practice of disguising communication to appear as though it is coming from a trusted source? 
Question: What is the practice of disguising communication to appear as though it is coming from a trusted source?
Answer: Spoofing
Correct! OSCTF{L33____________

What is a file called that contains a digital certificate? 
Question: What is a file called that contains a digital certificate?
Answer: Certificate
Correct! OSCTF{L33t___________

What term describes the attempt to gain sensitive information by disguising as a trustworthy entity? 
Question: What term describes the attempt to gain sensitive information by disguising as a trustworthy entity?
Answer: Phishing
Correct! OSCTF{L33t___________

What is a network device that filters and monitors incoming and outgoing network traffic? 
Question: What is a network device that filters and monitors incoming and outgoing network traffic?
Answer: Firewall
Correct! OSCTF{L33t_K_________

What type of attack involves overwhelming a system with traffic to disrupt service? 
Question: What type of attack involves overwhelming a system with traffic to disrupt service?
Answer: DDoS
Correct! OSCTF{L33t_Kn________

What is the primary protocol used for sending email over the internet? 
Question: What is the primary protocol used for sending email over the internet?
Answer: SMTP
Correct! OSCTF{L33t_Kn0_______

What does VPN stand for? 
Question: What does VPN stand for?
Answer: Virtual Private Network
Correct! OSCTF{L33t_Kn0w______

What is the name of the vulnerability that allows arbitrary code execution in software? 
Question: What is the name of the vulnerability that allows arbitrary code execution in software?
Answer: Buffer Overflow
Correct! OSCTF{L33t_Kn0wl_____

What is the term for a software update that fixes bugs and vulnerabilities? 
Question: What is the term for a software update that fixes bugs and vulnerabilities?
Answer: Patch
Correct! OSCTF{L33t_Kn0wl3____

What does MFA stand for in cybersecurity? 
Question: What does MFA stand for in cybersecurity?
Answer: Multi-Factor Authentication
Correct! OSCTF{L33t_Kn0wl3D___

What is a tool that scans a network for open ports and services? 
Question: What is a tool that scans a network for open ports and services?
Answer: Nmap
Correct! OSCTF{L33t_Kn0wl3Dg__

What is the name of the secure file transfer protocol that uses SSH? 
Question: What is the name of the secure file transfer protocol that uses SSH?
Answer: SFTP
Correct! OSCTF{L33t_Kn0wl3Dg3_

What does XSS stand for in web security? 
Question: What does XSS stand for in web security?
Answer: Cross-Site Scripting
Correct! OSCTF{L33t_Kn0wl3Dg3}

Final flag: OSCTF{L33t_Kn0wl3Dg3}

FLAG found!
>>>
</code>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">OSCTF{L33t_Kn0wl3Dg3}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy misc or pwn chanllenge for connect to pwn and check correct answer of answers.</p>

</body>
</html>
