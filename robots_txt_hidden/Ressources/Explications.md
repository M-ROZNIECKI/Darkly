En allant sur le robots.txt du site, on obtient deux chemin a ne pas indexer.

![1](screenshot/1.png "1")

On va s'occuper ici du chemin /.hidden/:

![2](screenshot/2.png "2")

On tombe sur une foret de dossier.  
On pourais les parcourir a la main (long et fastidieux)  
ou utiliser un script.  
On a utiliser un script en python et obtenu ca:

![3](screenshot/3.png "3")

On finit par trouver un flag

L'obfuscation a coup de foret de dossier et fichier, n'est pas une solution.  
On peut facilement contourner ce genre d'obfuscation avec sois du temps sois avec un script qui va parcourir l'arborescence de fichier.

On peut corriger ca en ne mettant pas le fichier dans un chemin meme non indexer car visible par le robots.txt.

On peut aussi proteger certain fichier et chemin avec des .htaccess si vraiment il y a des fichier qui ne doivent pas etre acceder (exemple les fichiers de configue du serveur).