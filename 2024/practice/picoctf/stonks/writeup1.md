<title>picoctf 2021 Stonks</title>

<!DOCTYPE html>
<html>
 
<body>
    <h1>picoctf 2021 Stonks</h1>

    <h2>Challenge Description</h2>
    <p> I decided to try something noone else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure! vuln.c:https://mercury.picoctf.net/static/fdf270d959fa5231e180e2bd11421d0c/vuln.c
nc mercury.picoctf.net 16439
 
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
   Looking to code we find an interesting function:
    <pre>
int buy_stonks(Portfolio *p) {
    if (!p) {
        return 1;
    }
    char api_buf[FLAG_BUFFER];
    FILE *f = fopen("api","r");
    if (!f) {
        printf("Flag file not found. Contact an admin.\n");
        exit(1);
    }
    fgets(api_buf, FLAG_BUFFER, f);

    int money = p->money;
    int shares = 0;
    Stonk *temp = NULL;
    printf("Using patented AI algorithms to buy stonks\n");
    while (money > 0) {
        shares = (rand() % money) + 1;
        temp = pick_symbol_with_AI(shares);
        temp->next = p->head;
        p->head = temp;
        money -= shares;
    }
    printf("Stonks chosen\n");

    // TODO: Figure out how to read token from file, for now just ask

    char *user_buf = malloc(300 + 1);
    printf("What is your API token?\n");
    scanf("%300s", user_buf);
    printf("Buying stonks with token:\n");
    printf(user_buf);

    // TODO: Actually use key to interact with API

    view_portfolio(p);

    return 0;
}
</pre>

       This function reads the flag onto the stack and then asks the user to enter input before printing it using printf. Based on this we know that this is a format string vulnerability and that we want to read off of the stack.

I then wrote the following script to connect to the server and send lots of %x (prints stack) before reading and parsing that to ascii:<a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/stonks/solve.py">code</a>
  and run code and get flag  
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{3qu4l1ty_n0t_4551gnm3nt_f6a5aefc}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on develper tools in in chrome and web exploitations</p>
</body>
</html>

