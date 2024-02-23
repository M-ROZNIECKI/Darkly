En allant sur le robots.txt du site, on obtient deux chemin a ne pas indexer.

![1](screenshot/1.png "1")

On va s'occuper ici du chemin /whatever/:

![2](screenshot/2.png "2")

dans htpasswd, on va trouver un couple id:hash

On va donc chercher ce que l'on peut en faire.

En testant a plusieur endroit, on fini par trouver une page admin sur le site.

On va donc essayer de si connecter.

Apres avoir essayer avec le hash en tant que mot de pass, ce qui n'as pas marcher, j'ai essayer de decrypter le hash.

Au vu de la proportion de hash en md5 sur ce site, je vais tester avec ca en premier. Bingo, j'obtient quelque chose.

En testant avec le resultat, on obtient le flag.

Pour ce proteger de ce genre de cas, deja ne pas garder ces password comme ca dans un fichier, meme non indexer.  
Il suffit de regarder le robots.txt pour les trouver comme ici.

On peut aussi proteger certain fichier et chemin avec des .htaccess si vraiment il y a des fichier qui ne doivent pas etre acceder (exemple les fichiers de configue du serveur).