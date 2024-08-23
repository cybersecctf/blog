<title>trip- angstromctf2024</title>
<!DOCTYPE html>
<html>

<body>
    <h1>trip- angstromctf2024</h1>

    <h2>Challenge Description</h2>
    <p> What road was this this <a href="https://cybersecctf.github.io/blog/2024/actf/trip/trip.jpeg">photo</a> taken on?

For example, if the road was "Colesville Road" the flag would be actf{colesville}.
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
  it looks like a osint problem but via category misc we use exiftools 
<pre> 
#python
import blog 
import os
def solve(file="trip.jpeg"):
  blog.solveup("exiftool linux",file)
if __name__ == "__main__" :
  solve("trip.jpeg")
</pre>
   and get flag that is road namevia cordinateds of gps in info:
 <img src=" https://cybersecctf.github.io/blog/2024/actf/trip/google.png" alt="google search result" class="inline"/>

    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">actf{chincotegue}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for use exiftools in linux</p>
</body>
</html>



