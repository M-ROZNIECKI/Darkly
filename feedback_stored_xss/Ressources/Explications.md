# Exploitation de Stored XSS via le formulaire de Feedback
**Date de découverte :** 23 février 2024

## Contexte
Au cours de notre analyse de sécurité, nous avons identifié une vulnérabilité de type Stored Cross-Site Scripting (XSS) dans le formulaire de feedback de l'application web. Cette vulnérabilité permet l'exécution de scripts malveillants sur le navigateur des utilisateurs finaux.

## Découverte et Exploitation
1. **Analyse Initiale**:
   - Une erreur a été observée dans la balise `<script>` liée au traitement du champ `Message`, bien qu'aucune exploitation directe n'ait été identifiée à ce stade.

2. **Concentration sur Message filed**:
   - Après avoir testé diverses entrées dans la fonctionnalité de feedback avec un focus particulier sur le champ `Message` du a la restriction de taille et de l'erreur precedente.

3. **Tests d'Injection XSS**:
   - Le test avec `<h1>o</h1>` dans le champ `Name` a montré que le HTML était interprété, ce qui indique une mauvaise échappement des entrées utilisateur.
   - Plusieurs payloads ont été testés pour l'exécution de scripts tout en modifiant la restriction de size :
     - `<php>alert('hello');</php>` : Échec
     - `<script>console.log('hello');</script>` : Échec
     - `<img src="x" onerror="alert('XSS')">` : Succès de l'exécution du script

4. **Impact de l'Exploitation**:
   - L'exploitation réussie a conduit à l'exécution de scripts arbitraires, ce qui a été confirmé par l'exécution du script via l'attribut `onerror` d'une balise `<img>`.
   - Après un redémarrage de la VM dû à un excès de scripts lancés, il a été observé que les scripts malveillants persistaient, ce qui a mené à l'apparition d'un flag lors du renvoi d'un feedback.

## Impact Potentiel
Cette vulnérabilité Stored XSS permet à un attaquant d'injecter des scripts persistants qui peuvent être exécutés sur les navigateurs des utilisateurs finaux, menaçant ainsi l'intégrité et la confidentialité des données utilisateur.

## Recommandations
- **Échappement des Entrées Utilisateur** : S'assurer que toutes les entrées utilisateur sont correctement échappées avant d'être rendues dans le navigateur, particulièrement dans les champs susceptibles de recevoir du code HTML ou JavaScript.
- **Utilisation de Politiques de Sécurité de Contenu (CSP)** : Implémenter des CSP pour réduire les risques d'attaques XSS en spécifiant les sources fiables pour l'exécution des scripts.
- **Audits de Sécurité Réguliers** : Effectuer des audits de sécurité réguliers et des tests de pénétration pour identifier et corriger les vulnérabilités de sécurité.

## Conclusion
La découverte de cette vulnérabilité de Stored XSS met en évidence l'importance de valider et d'échapper correctement toutes les entrées utilisateur pour prévenir l'exécution de scripts malveillants. La mise en œuvre des recommandations fournies aidera à améliorer la sécurité de l'application web contre les attaques XSS et autres vulnérabilités similaires.
