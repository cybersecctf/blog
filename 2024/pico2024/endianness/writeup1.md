
<!DOCTYPE html>
<html>

<body>
    <h1>endianness- picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p>   AAUTHOR: NANA AMA ATOMBO-SACKEY

Description
Know of little and big endian?
nc titan.picoctf.net 56898. 
Browse <a href="https://artifacts.picoctf.net/c_titan/116/flag.c">Source</a> , and find the flag!
 
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
   we open code and modify it to print little and big Endian  and enter it on netcat and get flag 
this is c code for convert text tolittle and big endian  and print it on base of this <a href="https://phantom1ss.github.io/blog/2024/pico2024/endianness/flag.c">code</a>
<pre>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

char *find_little_endian(const char *word) {
    size_t word_len = strlen(word);
    char *little_endian = (char *)malloc((2 * word_len + 1) * sizeof(char));

    for (size_t i = word_len; i-- > 0;) {
        snprintf(&little_endian[(word_len - 1 - i) * 2], 3, "%02X", (unsigned char)word[i]);
    }

    little_endian[2 * word_len] = '\0';
    return little_endian;
}

char *find_big_endian(const char *word) {
    size_t length = strlen(word);
    char *big_endian = (char *)malloc((2 * length + 1) * sizeof(char));

    for (size_t i = 0; i < length; i++) {
        snprintf(&big_endian[i * 2], 3, "%02X", (unsigned char)word[i]);
    }

    big_endian[2 * length] = '\0';
    return big_endian;
}

int main() {
    char user_word[100];
    printf("Enter the challenge word: ");
    fflush(stdout);
    scanf("%99s", user_word);

    char *challenge_word = strdup(user_word);
    printf("Word: %s\n", challenge_word);
    printf("littleindian: %s\n", find_little_endian(challenge_word));
    printf("bigindian: %s\n", find_big_endian(challenge_word));
    fflush(stdout);

    

    return 0;
}

</pre>
run and and in input add word get from netcat and input result to netcat later
<pre>
──(kali㉿kali)-[~/…/blog/2024/pico2024/endianness]
└─$ ./a.out
Enter the challenge word: bawie
Word: bawie
littleindian: 6569776162
bigindian: 6261776965
Enter the Little Endian representation: ^Z
zsh: suspended  ./a.out
┌──(kali㉿kali)-[~/…/blog/2024/pico2024/endianness]
└─$ nc titan.picoctf.net 59079
Welcome to the Endian CTF!
You need to find both the little endian and big endian representations of a word.
If you get both correct, you will receive the flag.
Word: bawie
Enter the Little Endian representation: 6569776162
Correct Little Endian representation!
Enter the Big Endian representation: 6261776965
Correct Big Endian representation!
Congratulations! You found both endian representations correctly!
Your Flag is: picoCTF{3ndi4n_sw4p_su33ess_91bc76a4}
</pre>
and get flag after enter correct results.
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{pr3tty_c0d3_51d374f0}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for  convert text to little and big Endian with c</p>
</body>
</html>

 

