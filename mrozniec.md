<h1 style="text-align: center">Piste suivi actuellement:</h1>

<table>
    <tbody>
        <tr>
            <td>1</td>
            <td>faille sql dans le champ search member by id</td>
        </tr>
        <tr>
            <td>2</td>
            <td>deux failles via le robots.txt
                <table>
                    <tbody>
                        <tr>
                            <td>2.1</td>
                            <td>via /whatever/ on trouve un passwd</td>
                        </tr>
                        <tr>
                            <td>2.2</td>
                            <td>via /.hidden/ ou on doit trouver le bon path dans une foret de dossier qui ne servent qu'as faire de l'obfuscation</td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
        <tr>
            <td>3</td>
            <td>sur la page survey, en changeant la valeur dans le code html de la page d'un vote</td>
        </tr>
        <tr>
            <td>4</td>
            <td>RECOVER PASSWORD qui a dans un champ hidden l'adress mail ou est envoyer la requete de recuperation de mot de pass</td>
        </tr>
        <tr>
            <td>5</td>
            <td>les trois lien facebook / twitter / insta qui peuvent etre changer dans le code html de la page et aucune verif dessus</td>
        </tr>
        <tr>
            <td>6</td>
            <td>avec l'argument page, on peut parcourir l'arboressence de fichier et remonter a coup de ../../../../etc/passwd pour recup quelque chose</td>
        </tr>
    </tbody>
</table>