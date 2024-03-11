# Source :

## Pist1

https://book.hacktricks.xyz/pentesting-web/login-bypass

`autocomplete="off"`
https://www.beyondsecurity.com/resources/vulnerabilities/autocomplete-not-disabled

####NOP

## PIST2

`X-Powered-By: PHP/5.5.9-1ubuntu4.29`

<!-- ## Exploitation Upload file:
21/02/2024

Pour commencer je me suis documenter sur les vunerabiliter et les eploits utilise sur l'upload de fichier :
- j'ai revisioner la video suivante : https://www.youtube.com/watch?v=ndAk6ymxxvM
- J'ai chercher quel extension de fichier fonctionais et j'ai remarquer que seul .jpg et .jpeg fonctionnais.
- j'ai donc tester une multitude de fichier:
- - `script.jpg`: `<?php phpinfo();?>`
- - `<?php phpinfo();?>.jpg`
- - `script.php.jpg`: `<?php phpinfo();?>`
- - `script.php`: `<?php phpinfo();?>`
Puis j'ai tenter de modifier le `Content-Type` dans le header de la requet.
pour cela j'ai utiliser l'outils burp pour modifier la requet avant de l'envoyer.
J'ai d'abort recup le content type l'osrque ca fonctionais puis apres j'ai retenter d'envoyer le `script.php` mais avec `Content-Type: image/jpeg`.

Flag:
46910D9CE35B385885A9F7E2B336249D622F29B267A1771FBACF52133BEDDBA8 -->


<!-- ## Exploitation cookie:
22/02/2024

Depuis le debut nous avons remarquer un cookie dans le navigateur en sur d'autre flag on a remarquer que le site utiliais souvent le chiffrement md5, nous l'avons passer dans un dechifreur en ligne et nous avons optenu false.
On a donc test de chiffrer true en md5 et de remplcer l'anciene valeur du cokkie par la nouvelle.

Flag:
df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3 -->

<!-- ## UserAgents:
23/02/2024

Sur la page suivante:
`http://10.13.200.24/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f`
Grace au indice dans les commentaires
![1.jpg](image)
Utiliser Burp pour modifier la requet:
Changer le `User-Agent` pour faire croire que le navigateur s'appel `ft_bornToSec`.
Et modifier `Referer` pour simuler la page web precedament visiter soit egale a `https://www.nsa.gov/`.
![2.jpg](image2)

flag: F2A29020EF3132E01DD61DF97FD33EC8D7FCD1388CC9601E7DB691D17D4D6188 -->

<!-- ## Feedback stored xss:
23/02/2024

J'ai remarquer dans la balise `<script>` qu'il y avais une erreur sur le check de champ `Message` cependent j'ai rien trouver de faisable avec, pourtant je me suis concentrer la dessus.

Apres avoir tester de nombreuse chose avec la fonctionaliter feedback

j'ai remarquer dans le champ `Name` que `<h1>o</h1>` a ete interpreter

j'ai donc tester:

`<php>alert('hello');</php>` : No
`<script>console.log('hello');</script>`: No
`<img src="x" onerror="alert('XSS')">` : Script exec

a force de tenter des truc la page feedback lancais trop de script j'ai donc redemarer la vm, mais tous avais disparus sauf `mes scrypts`. J'ai donc tenter de renvoyer un feedback et un flag est apparut.

flag:
0FBB54BBF7D099713CA4BE297E1BC7DA0173D8B3C21C1811B916A3A86652724E -->

## Brut-force login page

Apres de multiple tentative de brut-force en utilisant des combnaison de liste pour le login et e password j'ai remarquer que l'image sur la page de login etais marvin qui pointe sur le champs username du form j'ai donc tenter une ataque par dictionaire en gardant le username `marvin`

`hydra -l marvin -P /home/ar_ruc/Téléchargements/rockyou.txt 10.13.200.24 http-get-form "/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login#:images/WrongAnswer.gif"`

flag:B3A6E43DDF8B4BBB4125E5E7D23040433827759D4DE1C04EA63907479A80A6B2
