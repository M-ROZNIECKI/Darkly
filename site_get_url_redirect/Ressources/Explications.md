Dans le footer des pages du site, on a trois lien vers facebook, insta et twitter/x.

Pour faire la redirection, le lien est un lien vers le site actuel avec un parametre get appeller site.

On va essayer de rentrer autre chose comme paramettre, par exemple www.google.com et de lancer le lien.

On obtient le flag.

Ce genre de faille pourrait permettre de faire une campagne de fishing par mail avec le lien du site legit avec juste en paramettre get notre redirection vers le faux site.

Pour ce proteger de cela, il suffit de verifier si le lien en paramettre fait parti d'une liste de site accepter pour la redirection.