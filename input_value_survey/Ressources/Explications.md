En allant sur la page survey, on a un formulaire avec un vote qui nous est demandé.

En regardant le formulaire, on observe ça :

```html
<form action="#" method="post">
	<input type="hidden" name="sujet" value="2">
	<select name="valeur" onchange="javascript:this.form.submit();">
		<option value="1">1</option>
		<option value="2">2</option>
		<option value="3">3</option>
		<option value="4">4</option>
		<option value="5">5</option>
		<option value="6">6</option>
		<option value="7">7</option>
		<option value="8">8</option>
		<option value="9">9</option>
		<option value="10">10</option>
	</select>
</form>
```

On a testé de modifier la valeur d'une des options pour faire un vote d'une valeur exorbitante et voir si ça prenait en compte le vote.

Bingo, on obtient un flag et notre vote est pris en compte.

Pour éviter de se trouver avec ce genre de problème et potentiellement un vote/questionnaire truquer, il faut rajouter une vérification en backend que l'option choisie fait bien partie des options possibles.