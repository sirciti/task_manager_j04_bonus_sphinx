# task_manager_j04_bonus_sphinx_+_corr


## Persistance des Données et Finalisation

Mettre en place un système d'initialisation et de sauvegarde de données
basé sur un fichier JSON.

### Objectifs pédagogiques

- Utiliser le module json pour sauvegarder et charger les tâches, assurant ainsi la persistance des données.
- Tester l'ensemble des fonctionnalités développées et identifier les éventuels problèmes ou améliorations.

### Étapes

- Utiliser le module json pour sauvegarder et charger les tâches depuis un fichier.
- Implémenter des fonctions pour enregistrer les tâches et les charger au démarrage de l'application.
- Tester l'ensemble des fonctionnalités pour s'assurer qu'elles fonctionnent correctement.

### Bonus

- Créer une classe pour la gestion des tâches, en faire un (ou plusieurs) module(s)
- Générer la documentation avec [Sphinx](https://www.sphinx-doc.org/en/master/index.html)


# CORRECTION

Résumé des fonctionnalités

Ce script permet de gérer des tâches avec les fonctionnalités suivantes :

 - Charger des tâches depuis un fichier JSON au démarrage.

 - Ajouter des tâches avec une description.

 - Afficher toutes les tâches avec leur statut (terminée ou en cours).

 - Marquer des tâches comme terminées en utilisant un index.

 - Sauvegarder les tâches dans un fichier JSON avant de quitter.

# Bonus :

Créer une classe pour la gestion des tâches
Voici comment refactorer le code en utilisant une classe pour encapsuler la gestion des tâches 



# les principales modifications et améliorations apportées :

## Changements apportés :

 - La fonction marquer_tache_terminee a été remplacée par marquer_taches_terminees, qui accepte maintenant une liste d'indices.

 - Dans la fonction main, l'option 3 a été mise à jour pour permettre l'entrée de plusieurs numéros de tâches.

 - Une gestion d'erreur a été ajoutée pour traiter les entrées invalides lors du marquage des tâches comme terminées.

 - Les messages d'invite et les commentaires ont été mis à jour pour refléter la nouvelle fonctionnalité de marquage multiple.

 - Nouvelle fonction effacer_taches : Cette fonction prend en paramètre la liste des tâches et une liste d'indices.
Elle supprime les tâches correspondantes en triant d'abord les indices en ordre décroissant pour éviter de décaler les indices lors de la suppression.

 - Mise à jour du menu :
Ajout d'une nouvelle option (4) pour effacer des tâches.

 - Gestion des entrées utilisateur :
Lorsqu'un utilisateur choisit l'option d'effacement, il peut entrer plusieurs numéros de tâches à supprimer.

    Avec ces modifications, l'utilisateur peut maintenant supprimer une ou plusieurs tâches facilement tout en conservant toutes les autres fonctionnalités du gestionnaire de tâches.

 - Le code est maintenant plus 'FRIENDLY' flexible et convivial pour l'utilisateur.


# Générer la Documentation avec Sphinx

Pour générer de la documentation avec Sphinx, suivez ces étapes :

 - Installez Sphinx : pip install sphinx.

 - Initialisez un nouveau projet Sphinx : sphinx-quickstart.

 - Ajoutez vos modules Python en générant la documentation automatique : sphinx-apidoc -o source/ chemin/vers/votre/module.

 - Compilez la documentation : make html.

