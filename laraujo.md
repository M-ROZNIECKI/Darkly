# Source :

## Pist1

https://book.hacktricks.xyz/pentesting-web/login-bypass

`autocomplete="off"`
https://www.beyondsecurity.com/resources/vulnerabilities/autocomplete-not-disabled

####NOP

## PIST2

`X-Powered-By: PHP/5.5.9-1ubuntu4.29`

## Exploitation Upload file:
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
46910D9CE35B385885A9F7E2B336249D622F29B267A1771FBACF52133BEDDBA8

## Exploitation cookie:
22/02/2024

Depuis le debut nous avons remarquer un cookie dans le navigateur en sur d'autre flag on a remarquer que le site utiliais souvent le chiffrement md5, nous l'avons passer dans un dechifreur en ligne et nous avons optenu false.
On a donc test de chiffrer true en md5 et de remplcer l'anciene valeur du cokkie par la nouvelle.

Flag:
df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3

##