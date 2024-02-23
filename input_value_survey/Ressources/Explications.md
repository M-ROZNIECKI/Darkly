En allant sur la page survey, on as un formulaire avec un vote qui nous est demander.

En regardant le formulaire, on observe ca:

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

On as tester de modifier la valeur d'une des options pour faire un vote d'une valeur exorbitante et voir si ca prenais en compte le vote.

Bingo on obtient un flag et notre vote est pris en compte.

Pour eviter de ce trouver avec ce genre de probleme et potentiellement un vote/questionnaire truquer, il faut rajouter une verification en back end que l'option choisi fait bien parti des options possible.