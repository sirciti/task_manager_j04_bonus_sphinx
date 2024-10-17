'''
import json  # Importe le module JSON pour travailler avec des fichiers JSON
import os    # Importe le module os pour interagir avec le système de fichiers

# Définition du nom du fichier pour stocker les tâches
FICHIER_TACHES = "taches.json"

def charger_taches():
    """
    Charge les tâches depuis le fichier JSON.
    Retourne une liste vide si le fichier n'existe pas.
    """
    # Vérifie si le fichier existe
    if os.path.exists(FICHIER_TACHES):
        # Ouvre le fichier en mode lecture
        with open(FICHIER_TACHES, 'r') as fichier:
            # Charge et retourne les données JSON du fichier
            return json.load(fichier)
    # Retourne une liste vide si le fichier n'existe pas
    return []

def sauvegarder_taches(taches):
    """
    Sauvegarde les tâches dans le fichier JSON.
    """
    # Ouvre le fichier en mode écriture
    with open(FICHIER_TACHES, 'w') as fichier:
        # Écrit les tâches au format JSON dans le fichier
        json.dump(taches, fichier, indent=2)

def ajouter_tache(taches, description):
    """
    Ajoute une nouvelle tâche à la liste.
    """
    # Crée un dictionnaire représentant une tâche avec sa description et son statut
    tache = {"description": description, "terminee": False}
    # Ajoute la tâche à la liste des tâches
    taches.append(tache)
    print(f"Tâche ajoutée : {description}")

def afficher_taches(taches):
    """
    Affiche toutes les tâches avec leur statut.
    """
    # Vérifie si la liste des tâches est vide
    if not taches:
        print("Aucune tâche.")
    else:
        # Parcourt les tâches et affiche leur description et statut
        for i, tache in enumerate(taches, 1):
            statut = "Terminée" if tache["terminee"] else "En cours"
            print(f"{i}. {tache['description']} - {statut}")

def marquer_tache_terminee(taches, index):
    """
    Marque une tâche comme terminée.
    """
    # Vérifie si l'index de la tâche est valide
    if 1 <= index <= len(taches):
        # Marque la tâche comme terminée
        taches[index-1]["terminee"] = True
        print(f"Tâche '{taches[index-1]['description']}' marquée comme terminée.")
    else:
        print("Index de tâche invalide.")

def main():
    # Charge les tâches au démarrage de l'application
    taches = charger_taches()
    
    while True:
        print("\n--- Gestionnaire de Tâches ---")
        print("1. Ajouter une tâche")
        print("2. Afficher les tâches")
        print("3. Marquer une tâche comme terminée")
        print("4. Quitter")
        
        # Demande à l'utilisateur de choisir une option
        choix = input("Choisissez une option (1-4): ")
        
        if choix == '1':
            # Demande à l'utilisateur d'entrer la description de la tâche à ajouter
            description = input("Entrez la description de la tâche : ")
            ajouter_tache(taches, description)  # Ajoute la nouvelle tâche
        elif choix == '2':
            afficher_taches(taches)  # Affiche toutes les tâches
        elif choix == '3':
            afficher_taches(taches)  # Affiche toutes les tâches avant de marquer une tâche comme terminée
            index = int(input("Entrez le numéro de la tâche à marquer comme terminée : "))
            marquer_tache_terminee(taches, index)  # Marque la tâche sélectionnée comme terminée
        elif choix == '4':
            sauvegarder_taches(taches)  # Sauvegarde les tâches avant de quitter
            print("Tâches sauvegardées. Au revoir!")
            break  # Quitte la boucle et termine le programme
        else:
            print("Option invalide. Veuillez réessayer.")

# Vérifie si le script est exécuté directement
if __name__ == "__main__":
    main()  # Appelle la fonction principale pour démarrer l'application
    '''







#principales modifications et améliorations apportées

import json
import os

# Définition du nom du fichier pour stocker les tâches
FICHIER_TACHES = "taches.json"

def charger_taches():
    """
    Charge les tâches depuis le fichier JSON.
    Retourne une liste vide si le fichier n'existe pas.
    """
    if os.path.exists(FICHIER_TACHES):
        with open(FICHIER_TACHES, 'r') as fichier:
            return json.load(fichier)
    return []

def sauvegarder_taches(taches):
    """
    Sauvegarde les tâches dans le fichier JSON.
    """
    with open(FICHIER_TACHES, 'w') as fichier:
        json.dump(taches, fichier, indent=2)

def ajouter_tache(taches, description):
    """
    Ajoute une nouvelle tâche à la liste.
    """
    tache = {"description": description, "terminee": False}
    taches.append(tache)
    print(f"Tâche ajoutée : {description}")

def afficher_taches(taches):
    """
    Affiche toutes les tâches avec leur statut.
    """
    if not taches:
        print("Aucune tâche.")
    else:
        for i, tache in enumerate(taches, 1):
            statut = "Terminée" if tache["terminee"] else "En cours"
            print(f"{i}. {tache['description']} - {statut}")

def marquer_taches_terminees(taches, indices):
    """
    Marque plusieurs tâches comme terminées.
    """
    for index in indices:
        if 1 <= index <= len(taches):
            taches[index-1]["terminee"] = True
            print(f"Tâche '{taches[index-1]['description']}' marquée comme terminée.")
        else:
            print(f"Index de tâche invalide : {index}")

def effacer_taches(taches, indices):
    """
    Efface plusieurs tâches de la liste.
    """
    # On doit trier les indices en ordre décroissant pour éviter de décaler les indices lors de la suppression
    indices.sort(reverse=True)
    
    for index in indices:
        if 1 <= index <= len(taches):
            print(f"Tâche '{taches[index-1]['description']}' effacée.")
            del taches[index-1]  # Supprime la tâche à l'index donné
        else:
            print(f"Index de tâche invalide : {index}")

def main():
    taches = charger_taches()
    
    while True:
        print("\n--- Gestionnaire de Tâches ---")
        print("1. Ajouter une tâche")
        print("2. Afficher les tâches")
        print("3. Marquer une ou plusieurs tâches comme terminées")
        print("4. Effacer une ou plusieurs tâches")
        print("5. Quitter")
        
        choix = input("Choisissez une option (1-5): ")
        
        if choix == '1':
            description = input("Entrez la description de la tâche : ")
            ajouter_tache(taches, description)
        elif choix == '2':
            afficher_taches(taches)
        elif choix == '3':
            afficher_taches(taches)
            indices_input = input("Entrez le(s) numéro(s) de la/les tâche(s) à marquer comme terminée(s) (séparés par des espaces) : ")
            try:
                indices = [int(i) for i in indices_input.split()]
                marquer_taches_terminees(taches, indices)
            except ValueError:
                print("Entrée invalide. Veuillez entrer des numéros séparés par des espaces.")
        elif choix == '4':
            afficher_taches(taches)
            indices_input = input("Entrez le(s) numéro(s) de la/les tâche(s) à effacer (séparés par des espaces) : ")
            try:
                indices = [int(i) for i in indices_input.split()]
                effacer_taches(taches, indices)
            except ValueError:
                print("Entrée invalide. Veuillez entrer des numéros séparés par des espaces.")
        elif choix == '5':
            sauvegarder_taches(taches)
            print("Tâches sauvegardées. Au revoir!")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()