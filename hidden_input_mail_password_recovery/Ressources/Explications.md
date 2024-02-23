En allant sur la page de recuperation de mots de pass, on s'appercoit qu'il n'y a qu'un bouton submit et aucun champ a remplir.  
Je decide donc de regarder le code html de la page a cet endroit:

```
<form action="#" method="POST">
	<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
	<input type="submit" name="Submit" value="Submit">
</form>
```

Il y a un champ cacher appeler mail.

Il suffis donc de changer sa valeu pour que le mail de recuperation arrive ailleur.

Ainsi, on peut exploiter cela de deux maniere possible:

1. recevoir le mail de recuperation de mots de pass a la place de l'adress mail d'origine.  
Cela nous permet de forger un faux mail de recovery a envoyer a la bonne adress

2. spammer un envois de mail vers d'autres personnes via se formulaire.

Un moyen de s'en proteger serais de definir ce mail en backend dans la fonction qui va envoyer le mail et ainsi eviter ces deux problemes.