# Piste suivi actuellement:
1. [ ] faille sql dans le champ search member by id

2. [ ] deux failles via le robots.txt
    * via /whatever/ on trouve un passwd
    * via /.hidden/ ou on doit trouver le bon path dans une foret de dossier qui ne servent qu'as faire de l'obfuscation

3. [x] sur la page survey, en changeant la valeur dans le code html de la page d'un vote

4. [x] RECOVER PASSWORD qui a dans un champ hidden l'adress mail ou est envoyer la requete de recuperation de mot de pass

5. [ ] les trois lien facebook / twitter / insta qui peuvent etre changer dans le code html de la page et aucune verif dessus

6. [ ] avec l'argument page, on peut parcourir l'arboressence de fichier et remonter a coup de ../../../../etc/passwd pour recup quelque chose