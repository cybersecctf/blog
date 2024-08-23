<title>lactf2024- web/flaglang</title>

<!DOCTYPE html>
<html>

<body>
    <h1>lactf2024- web/flaglang</h1>

    <h2>Challenge Description</h2>
    <p> Do you speak the language of the flags?
https://flaglang.chall.lac.tf/
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        <li> i open code chose two  list of countries and in second flagstan to get flag ion base of code </li>
        <li>and should select country in first list have no ambargo from flagestaan country on second list and show flag</li>
        <li>in first view i see nothing in code but in yaml i see that iso of norway is NO</li>
        <pre>
Northern Mariana Islands:
  iso: MP
  msg: Hello world
  deny: []
Norway:
  iso: NO
  msg: Hallo verden
  deny: []
Oman:
  iso: OM
  msg: مرحبا بالعالم
  deny: []</pre>
       <li>and in app.js search in js and check if valid and send flag</li>
<pre>

app.get('/view', (req, res) => {
  if (!req.query.country) {
    res.status(400).json({ err: 'please give a country' });
    return;
  }
  if (!countries.has(req.query.country)) {
    res.status(400).json({ err: 'please give a valid country' });
    return;
  }
  const country = countryData[req.query.country];
  const userISO = req.signedCookies.iso;
  if (country.deny.includes(userISO)) {
    res.status(400).json({ err: `${req.query.country} has an embargo on your country` });
    return;
  }
  res.status(200).json({ msg: country.msg, iso: country.iso });
});

app.get('/', (req, res) => {
  const template = fs.readFileSync(path.join(__dirname, 'index.html')).toString();
  const iso = req.signedCookies.iso || 'US';
  const country = isoLookup[iso];
  res
    .status(200)
    .type('html')
    .send(template
      .replaceAll('$msg$', country.msg)
      .replaceAll('$name$', country.name)
      .replaceAll('$iso$', country.iso)
      .replaceAll('$countries$', countryList)
    );
});

app.listen(3000);
</pre>
    in yaml no means no and becaouse app.js check iso and norway iso is "No" so should select countries norway and flagstan for get
flag becaouse in yaml no means false
 <img src=" https://phantom1ss.github.io/blog/2024/lactf2024/flaglang/flag.png" alt="ctf flag  image" class="inline"/>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">lactf{n0rw3g7an_y4m7_f4ns_7n_sh4mbl3s}</p>

    <h2>Conclusion</h2>
    <p>this is a     easy chanllenge for work on web challenge and yaml and javascript/p>
</body>
</html>

