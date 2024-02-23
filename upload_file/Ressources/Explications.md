# Exploitation de Téléchargement de Fichiers
**Date de découverte :** 21 février 2024

## Introduction
L'objectif était d'explorer les vulnérabilités liées au téléchargement de fichiers sur l'application cible. Ce type de vulnérabilité peut permettre à un attaquant de télécharger des fichiers malveillants qui peuvent être exécutés côté serveur.

## Recherche Préliminaire
1. **Documentation et Tutoriels**:
   - Pour comprendre les vulnérabilités et les exploits courants dans l'upload de fichiers, j'ai consulté diverses ressources, dont une vidéo explicative sur YouTube: https://www.youtube.com/watch?v=ndAk6ymxxvM.

2. **Tests d'Extensions de Fichiers**:
   - J'ai identifié que seules les extensions `.jpg` et `.jpeg` étaient acceptées pour le téléchargement.

## Exploitation Testée
J'ai procédé à plusieurs tests pour évaluer la gestion des fichiers téléchargés par l'application :
1. **Fichiers Testés**:
   - `script.jpg` avec le contenu `<?php phpinfo();?>`
   - Fichier nommé `<?php phpinfo();?>.jpg`
   - `script.php.jpg` avec le contenu `<?php phpinfo();?>`
   - `script.php` avec le contenu `<?php phpinfo();?>`

2. **Manipulation des Headers HTTP**:
   - Utilisation de l'outil Burp Suite pour intercepter et modifier les requêtes HTTP, notamment en changeant le `Content-Type` en `image/jpeg` lors de l'envoi du fichier `script.php`.

## Résultats
Les tests ont révélé la possibilité de contourner les restrictions de l'application sur les types de fichiers en manipulant les headers HTTP. Cette technique peut potentiellement permettre l'exécution de code côté serveur si le fichier malveillant est exécuté.

## Recommandations
- **Validation Stricte des Fichiers** : Implémenter une validation stricte côté serveur pour vérifier à la fois l'extension et le type MIME des fichiers téléchargés.
- **Blocage de l'Exécution de Scripts** : S'assurer que les fichiers téléchargés ne peuvent pas être exécutés côté serveur par une configuration appropriée du serveur web.
- **Utilisation de Listes Blanches** : Privilégier les listes blanches d'extensions de fichiers autorisées au lieu de listes noires pour réduire le risque d'omission.

## Conclusion
Cette vulnérabilité souligne l'importance d'une validation rigoureuse des fichiers téléchargés pour prévenir l'exécution de code arbitraire sur le serveur. Les recommandations fournies visent à améliorer la sécurité de l'application en restreignant les types de fichiers pouvant être téléchargés et en empêchant l'exécution de scripts malveillants.
