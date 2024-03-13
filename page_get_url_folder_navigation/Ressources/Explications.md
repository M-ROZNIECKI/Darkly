On observe sur l'URL un paramètre GET nommer page, on va s'en servir pour essayer de naviguer dans les dossiers et remonter jusqu'as /etc/passwd par exemple.

![1](screenshot/1.png "1")

On peut donc se balader sur l'arborescence de fichier du backend librement et donc obtenir soit des pages internet ou des fichiers que l'on ne serait pas censé pouvoir avoir accès.

Une solution serait de vérifier en backend ce que l'on reçoit dans le paramètre GET "page" et de le comparer à une liste de réponses valide.