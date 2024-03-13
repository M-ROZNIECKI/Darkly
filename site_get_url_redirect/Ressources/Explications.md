Dans le footer des pages du site, on a trois liens vers facebook, insta et twitter/x.

Pour faire la redirection, le lien est un lien vers le site actuel avec un paramètre GET appelé site.

On va essayer de rentrer autre chose comme paramètre, par exemple www.google.com et de lancer le lien.

On obtient le flag.

Ce genre de faille pourrait permettre de faire une campagne de fishing par mail avec le lien du site legit avec juste en paramètre GET notre redirection vers le faux site.

Pour se protéger de cela, il suffit de vérifier si le lien en paramètre fait partie d'une liste de site accepter pour la redirection.