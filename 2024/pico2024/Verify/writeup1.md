
<!DOCTYPE html>
<html>

<body>
    <h1>Verify- picoctf2024</h1>

    <h2>Challenge Description</h2>
    <p> 
AUTHOR: JEFFERY JOHN

Description
People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.
You can download the challenge files here:
<a href="https://artifacts.picoctf.net/c_rhea/20/challenge.zip">challenge.zip</a>

Additional details will be available after launching your challenge instance.

</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
this is a challenge for check and verfy file with sha256sum .use this command for check and find file is valid with checksum.txt
    <pre>
──(kali㉿kali)-[~/…/Verify/home/ctf-player/drop-in]
└─$ ssh -p 52768 ctf-player@rhea.picoctf.net
 

The authenticity of host '[rhea.picoctf.net]:60831 ([3.136.191.228]:60831)' can't be established.
ED25519 key fingerprint is SHA256:QKdv+RGJL0UYRDM66IiGQ5dsXOX7DQFqB7umTylh+IU.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[rhea.picoctf.net]:60831' (ED25519) to the list of known hosts.
ctf-player@rhea.picoctf.net's password: 
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 6.5.0-1014-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ctf-player@pico-chall$ ls
checksum.txt  decrypt.sh  files
ctf-player@pico-chall$ cat checksum.txt
fba9f49bf22aa7188a155768ab0dfdc1f9b86c47976cd0f7c9003af2e20598f7
ctf-player@pico-chall$ cd files
┌──(kali㉿kali)-[~/…/home/ctf-player/drop-in/files]
└─$ sha256sum * |grep "fba9f49bf22aa7188a155768ab0dfdc1f9b86c47976cd0f7c9003af2e20598f7"
fba9f49bf22aa7188a15576l8ab0dfdc1f9b86c47976cd0f7c9003af2e20598f7  87590c24

ctf-player@pico-chall$ ls
047MJYW7  AOAysod6  LQJNuVhs  URYYNGxZ  fQnfnq06  t3yYcEve
0CbGv6a3  AOgyIEGc  LkGAamWS  VR8O9EAS  fnrslV0R  t7jXqCcv
0E56AVSC  AlGTwKyO  LmicJDs8  W1Fiysnc  gDXNNquR  tQQuoksm
0QUxtltc  AmQLyNou  Lmt5Y0x2  WBbhtpsN  gIhaWdn0  tjZsxG5L
0XKkalUj  Ar2IDsE2  Lo86CvQ9  WBv990nM  gkqJibML  tzjdKlhj
0hBYiFqV  BD8hIik3  LxrBh9k1  WEqguSEY  gmcsCSX3  uDj1e5QR
0xx1tyUI  BtuwzSy0  M4k3wbII  WGlw8QMW  hBccpGRH  uJnJfk8o
1VpyYwwh  C8QQ7gyc  Ml2ne9bC  WWTBLhPp  hI05TCz1  ukl9M0t5
25jFiRcF  CIcPHsac  N18is4D1  WdGGv43K  hONfsBJg  ulFEMOKX
2B0GV1AB  CJ5U4hxW  NAKaekRz  X7yet6uw  hgfq6lwn  umDaEkFr
2SbMywFt  CmGCd6Vt  NEc5NL3C  XF3VmqVm  hnC2Necm  uvq4BDCM
2Yc6IWTg  D6DGyxjR  NH1pCwum  XFrufR80  hsW2u10K  uw3TvL3P
2oGGasVb  D9zwUVlq  NmuLJcjD  XQJcaZgW  i2LDbe1K  uwZIBYpw
2xPyec1z  DBQbeL0I  NqjC5VXz  XqRw2HGU  i4XAopa0  uz0yrxxD
3HtK7pJ0  DRnArSUC  O7knebdG  XuigwWF7  iKj2d6J4  v0LKVD3h
3MWxikbL  DSwFiycn  O9vttreT  Y1tTgMUD  iMQMDV0F  v9TEcwko
3P2iIh03  DgSvTEwj  OGiva8vH  YEjiR5zf  jHRn7Fub  vC1tHUr2
3ZyNMmFE  DhGmqcSh  OHjloRN0  YZ0OB1mt  jvtAQCHw  vGHNz4al
3eJU0bPR  DpTMOGCI  OaQl5g3e  Ylaf2TY1  lMx8gj9G  vL0JYb7n
3qDZ0GiM  DxlIKqf0  ObjxHPwy  Yn1Qg1dx  lURnFs0v  vY5qGrrd
3rXzZWry  EC1I5QwZ  Ofz0iqFX  Ypof7Dgr  lyYImb9U  vvJtzkqH
43UId6P7  EXORCadn  Ot4mYM7x  ZM8AYtlG  mMUJICI9  w3o3t3VK
4MQ26j79  EfRHiDLP  Ous2JVk2  ZVhZ6QYU  mpJ16YYd  wJD9dCMd
4UWHd6Hh  Eg5lVJUw  PJqcmuRt  ZWNJ0AhH  nMTwYBYg  wgvRImaG
4iAgLaET  ElM3tYhK  PfmG9EIR  ZZSXid5R  niXGrsgK  whevF4V0
51fpnVb7  FNRT4oFd  PvE5OAg4  a76e3swH  nr3IXKgz  x1wlAOTr
58VrA22G  FWmPesGL  Q94hibhx  aUzIEw0T  nvtdmSSg  xCDyjqeT
5HYKp822  FXHBxQjZ  QHkh1WHT  bE62hGOU  oQzbBXPT  xE1I24IF
5Hde480w  Fv7iksDZ  QRakKVta  bNDt5rfT  onqK4HP3  xP8hXfNR
5K1a6h06  G244hQnd  Qi0CXXRR  bf4r768r  opLYnq5q  xQMWIZBH
5P2RhVCm  GDrafQ2W  Qir73mSK  bvPuToXm  orV7qTqZ  xVPXvgB2
5UGLBciS  GHuWjeJ9  R0QJ2VKL  c6c8b911  oy2oXp1t  xgBUzxwD
5glLfO3M  GUEnrd1t  R9B10IsM  cYQJTzGN  pGGOwBsr  xjRhyYW5
60CeHYva  Gp1JEl2h  RT9fmHCO  coJvjQ1h  pOWsomAC  xrUttVxO
69891sbg  H7Ixs9CI  RiQGT34B  d3p6iNNZ  pQNOrEf0  xxr0iXrr
6ePyVUQ2  HDYiL2qX  SFAQKdZD  dDSS287o  pcG2OMtT  yAbc0Rj2
6nFsOudx  HNRI4jm0  SGQH2HKl  dDuPGuwH  pfB7wztg  yRrCeSQg
6wnVCfWh  HUiJtVz0  SQrS0l9A  dEVxJ2qG  pn2lFoDd  yi2zkQtL
7YlIOxWG  HhPvJ7d7  SREVuUw3  dJzWkU1Q  poTBHw5o  yj7yobL0
80btcs9b  Ht3OiHhF  Sus5gnJ8  e7U2gGar  pz7WGxJ4  yxVNk723
80f71Tlc  I1gghDYt  SzSn7OcI  eHMqnmO6  qJIJZA0v  z333mx7V
85k4844c  IJX4r4eM  TDjaKG6o  eUp5OdvA  qiKkh7L2  zNtZNpTg
86hYDjno  JB4PaRNY  TMEQwqGw  efPoh96A  qnxF5I1t  zSomJYUc
8SXF7mDb  JqYRPdED  Tb4MR5ML  egSaXF3D  rAQk2W0n  zUmtlpHw
8h1rOlXM  K4jUiynD  TcfR5Cf6  enUaRS4w  rDBnOYi8  zjK7vU2n
9CrGqrOf  KDp8EJSk  Td52rYaf  eoYlHLVB  rHtWBcCX  zlkIRSOv
9VFp8JdD  KbONzfRz  Texe1REf  exyTux3t  rK99ez1a
9YOFaoZl  Kd0WNtCU  ThXpDtur  fB2VnieD  rUmhKhnU
9fSkDlcH  Keoo2vTu  TtY9kI58  fJiZ2bMw  sOhwN7cV
9spBfMu7  KvvTfLSK  TxL3f6fM  fKCy1WTf  sTktzsdS
A0Xjfjyv  LP8coBqU  U7SEpsXd  fPrKO8V5  t3MxVbsm
ctf-player@pico-chall$ cd
ctf-player@pico-chall$ ls
drop-in
ctf-player@pico-chall$ cd
ctf-player@pico-chall$ ls
drop-in
ctf-player@pico-chall$ cd .
ctf-player@pico-chall$ ls
drop-in
ctf-player@pico-chall$ cd drop-in
ctf-player@pico-chall$ ls
checksum.txt  decrypt.sh  files
ctf-player@pico-chall$ ./decrypt.sh files/87590c24
picoCTF{trust_but_verify_c6c8b911}
ctf-player@pico-chall$ Connecshation to rhea.picoctf.net closed by remote host.
Connection to rhea.picoctf.net closed.
</pre>
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{trust_but_verify_87590c24}
</p>

    <h2>Conclusion</h2>
    <p>this is a     easy chanllenge for check file is valid with shasum256 and checksum.txt
</p>
</body>
</html>



