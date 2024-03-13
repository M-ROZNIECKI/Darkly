En allant sur la page de récupération de mots de pass, on s'aperçoit qu'il n'y a qu'un bouton submit et aucun champ à remplir.  
Je décide donc de regarder le code HTML de la page à cet endroit :

```
<form action="#" method="POST">
	<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
	<input type="submit" name="Submit" value="Submit">
</form>
```

Il y a un champ caché appelé 'mail'.

Il suffit donc de changer sa valeur pour que le mail de récupération arrive ailleurs.

Ainsi, on peut exploiter cela de deux manières possibles :

1. recevoir le mail de récupération de mots de pass a la place de l'adresse mail d'origine.  
Cela nous permet de forger un faux mail de recovery à envoyer à la bonne adresse

2. spammer des envois de mail vers d'autres personnes via ce formulaire.

Un moyen de s'en protéger serait de définir ce mail en backend dans la fonction qui va envoyer le mail et ainsi éviter ces deux problèmes.