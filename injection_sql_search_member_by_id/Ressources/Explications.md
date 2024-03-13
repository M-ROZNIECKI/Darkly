Sur la page qui permet de chercher un utilisateur via son id,  
on s'aperçoit que l'on peut faire de l'injection SQL dans le champ de recherche.

![1](screenshot/1.png "1")

![2](screenshot/2.png "2")

On va donc pouvoir récupérer les différentes colonnes et tables qui composent la base de donnée avec cette requête dans le champ de recherche :

`1 union SELECT column_name, table_name FROM information_schema.columns`

Je vais vous épargner les différentes requêtes pour parcourir les différentes colonnes et seulement mettre la requête qui a permis de récupérer quelque chose d'intéressant :

`1 union SELECT Commentaire, countersign FROM users`

![3](screenshot/3.png "3")

Pour le dernier résultat, nous obtenons un hash et des instructions pour trouver le flag.

Après décryptage en md5 du hash, on obtient : FortyTwo
Plus qu'à passer le tout en lowercase puis de le sh256

Ça y est, on a le flag

Pour se protéger de ce genre de faille, on peut sanitize ce que l'on reçoit dans le backend et par exemple dans le cas précis, refuser si on reçoit autre chose que ce qui est attendu, un nombre.