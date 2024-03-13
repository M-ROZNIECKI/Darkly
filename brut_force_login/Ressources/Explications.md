# Brut-force sur la page de connexion
**Date de découverte :** 11 mars 2024

## Contexte

Au cours de notre analyse de sécurité de l'application web cible, une série de tentatives de brut-force a été lancée contre la page de connexion, guidée par des indices visuels présents sur cette dernière.

## Observation
**Indice Visuel** :
	- L'image affichée sur la page de connexion représentait Marvin, suggérant que le nom d'utilisateur pour l'attaque de brut-force devrait être marvin.
**Stratégie d'Attaque** :
	- En se basant sur cet indice, une attaque par dictionnaire a été décidée, en fixant le nom d'utilisateur à marvin et en utilisant une liste de mots de passe courants.

## Tentatives Échouées
Avant de parvenir à une attaque réussie, plusieurs tentatives ont échoué, soulignant l'importance de persévérance et d'ajustement dans la méthodologie d'attaque :

**Essais avec Différents Noms d'Utilisateur** :
	- Des tentatives préliminaires sans utiliser l'indice de l'image n'ont pas abouti, soulignant l'importance de l'indice visuel.
**Variations de Commandes Hydra** :
	- Plusieurs configurations de la commande Hydra ont été testées, ajustant les paramètres pour mieux cibler la structure du formulaire de connexion.

## Commande Hydra Utilisée
La commande suivante a été exécutée pour tenter l'attaque de brut-force :

```
hydra -l marvin -P /{PATH}/rockyou.txt 10.13.200.24 http-get-form "/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login#:images/WrongAnswer.gif"
```

- **Outil** : Hydra
- **Nom d'utilisateur** : marvin
- **Liste de Mots de Passe** : rockyou.txt
- **Cible** : 10.13.200.24
- **Paramètres de la Requête** : Détaillés pour correspondre aux champs de formulaire de la page de connexion.

## Conclusion et Recommandations
Cette expérience démontre la nécessité d'adapter continuellement les stratégies d'attaque en fonction des feedbacks et des indices recueillis. Les échecs initiaux ont joué un rôle crucial dans la compréhension de la cible et dans l'ajustement des techniques d'attaque pour réussir finalement.

Pour améliorer la sécurité contre de telles attaques, nous recommandons :

- **Implémentation de Limites de Taux** : Pour décourager les attaques automatisées, limiter le nombre de tentatives de connexion autorisées par IP sur une période donnée.

- **Introduction de CAPTCHA** : Un CAPTCHA peut efficacement freiner les attaques automatisées, en obligeant à une interaction humaine.
- **Politiques de Mot de Passe Robustes** : Encourager les utilisateurs à créer des mots de passe forts et uniques pour réduire la probabilité de succès des attaques par brut-force.
- **Mise en place de service tiers** : L'installation et la configuration de service comme **fail2ban** ou **CrowdSec** qui analyse les logs pour ban les IP malveillantes.

L'analyse des tentatives échouées et réussies offre une vision complète du processus d'attaque et souligne l'importance de la persévérance et de l'adaptation dans les tests de sécurité.
