<title>vault-door-training- picoctf2019</title>

<!DOCTYPE html>
<html>

<body>
    <h1>vault-door-training- picoctf2019</h1>

    <h2>Challenge Description</h2>
    <p> AUTHOR: MARK E. HAASE

Description
Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility. The source code for the training vault is here: <a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/vaultdoortraining/VaultDoorTraining.java">VaultDoorTraining.java</a>
</p>
merge
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
      downloa dfile and open it and see code of it
<p id="code1">
import java.util.*;

class VaultDoorTraining {
    public static void main(String args[]) {
        VaultDoorTraining vaultDoor = new VaultDoorTraining();
        Scanner scanner = new Scanner(System.in); 
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
    String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
    if (vaultDoor.checkPassword(input)) {
        System.out.println("Access granted.");
    } else {
        System.out.println("Access denied!");
    }
   }

    // The password is below. Is it safe to put the password in the source code?
    // What if somebody stole our source code? Then they would know what our
    // password is. Hmm... I will think of some ways to improve the security
    // on the other doors.
    //
    // -Minion #9567
    public boolean checkPassword(String password) {
        return password.equals("w4rm1ng_Up_w1tH_jAv4_eec0716b713");
    }
}

</p>
       password is in end of code and should wrap with picoctf{password} for granted access like this
<pre>
                                                                                                                                                           
┌──(kali㉿kali)-[~/…/2024/practice/picoctf/vaultdoortraining]
└─$ java VaultDoorTraining.java
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
Enter vault password: picoCTF{w4rm1ng_Up_w1tH_jAv4_eec0716b713}
Access granted.

</pre>
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{w4rm1ng_Up_w1tH_jAv4_eec0716b713}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for reverse engineering with java</p>
</body>
</html>


