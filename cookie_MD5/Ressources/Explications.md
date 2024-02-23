# Exploitation de Cookie via MD5
**Date de découverte :** 22 février 2024

## Contexte
Au cours de notre analyse de sécurité de l'application web, nous avons identifié un cookie qui est utilisé de manière significative pour le contrôle d'accès ou le suivi de l'état d'un utilisateur avec des privilege. Ce cookie semble encoder certaines valeurs.

![cookie](screenshot/1.png)

## Observation
1. **Identification du Cookie**:
   - Le cookie `I_am_admin` a attiré notre attention en raison de son nom et de sa présence constante lors de différentes actions sur le site.

2. **Utilisation du MD5**:
   - En examinant de plus près les mécanismes de sécurité du site, nous avons remarqué l'utilisation fréquente du chiffrement MD5.

3. **Déchiffrement du Cookie**:
   - Nous avons tenté de décoder la valeur du cookie MD5 en utilisant un service de déchiffrement en ligne, ce qui a résulté en une sortie `false`.

## Exploitation Testée
Pour tester une potentielle vulnérabilité, nous avons procédé comme suit :
1. **Chiffrement de la valeur `true`**:
   - Nous avons généré le hachage MD5 correspondant à la chaîne `true` pour remplacer la valeur originale du cookie.

2. **Modification du Cookie**:
   - Le cookie original a été remplacé par la nouvelle valeur MD5 dans le navigateur, dans le but de modifier le comportement attendu de l'application (par exemple, bypasser une restriction ou modifier un état d'authentification).

## Impact Potentiel
Cette méthode pourrait permettre à un attaquant de manipuler l'état de l'application côté client, en fonction de la manière dont le cookie est utilisé (par exemple, contournement de l'authentification, élévation de privilèges, etc.).

## Recommandations
- **Abandonner MD5 au profit d'algorithmes plus sécurisés** : MD5 est considéré comme obsolète pour les applications de sécurité en raison de ses vulnérabilités connues. Utiliser des algorithmes de hachage plus robustes comme SHA-256.
- **Validation côté serveur** : S'assurer que toutes les valeurs de cookie sont validées côté serveur pour éviter les manipulations côté client.
- **Utilisation de mécanismes de sécurisation des cookies** : Implémenter des attributs de cookies tels que `HttpOnly` et `Secure` pour renforcer la sécurité.

## Conclusion
La découverte de cette vulnérabilité souligne l'importance d'utiliser des pratiques de sécurisation modernes et robustes pour la gestion des cookies et des sessions. En suivant les recommandations fournies, l'application web peut être rendue plus résistante contre ce type d'exploitation.
