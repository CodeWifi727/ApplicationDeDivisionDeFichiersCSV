import tkinter as tk
from tkinter import filedialog
import os

# Créer une fenêtre Tkinter
root = tk.Tk()
root.withdraw()  # Cacher la fenêtre principale

# Demander à l'utilisateur de sélectionner un fichier
file_path = filedialog.askopenfilename()

# Initialiser la variable lines_by_client
lines_by_client = {}

if file_path:
    # Demander à l'utilisateur de sélectionner un dossier pour enregistrer les fichiers divisés
    output_folder = filedialog.askdirectory(title="Sélectionnez un dossier de destination")

    if output_folder:
        # Lire le contenu du fichier sélectionné
        with open(file_path, 'r') as file:
            lines = file.readlines()

           # Parcourir les lignes à partir de la deuxième ligne (la première contient les titres des colonnes)
        for line in lines[1:]:
            if line.strip():  # Vérifier si la ligne n'est pas vide
                values = line.strip().split(';')
                if len(values) >= 5:  # Vérifier si la ligne a suffisamment de valeurs
                    client_ref = values[4]

                    # Si le client_ref n'est pas déjà dans le dictionnaire, créer une nouvelle liste pour lui
                    if client_ref not in lines_by_client:
                        lines_by_client[client_ref] = []

                    # Ajouter la ligne au client_ref approprié
                    lines_by_client[client_ref].append(line)

        # Créer le dossier de destination s'il n'existe pas
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Écrire les lignes dans des fichiers séparés pour chaque client_ref
        for client_ref, client_lines in lines_by_client.items():
            filename = os.path.join(output_folder, f"client_{client_ref}.csv")
            with open(filename, 'w') as client_file:
                client_file.write(lines[0])  # Écrire les titres des colonnes
                client_file.writelines(client_lines)

        print("Fichiers divisés créés avec succès !")

    else:
        print("Aucun dossier de destination sélectionné.")

else:
    print("Aucun fichier sélectionné.")

# Fermer la fenêtre Tkinter
root.destroy()
