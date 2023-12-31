# Permet d'importer string.punctuation, car il n'y a pas de string method pour les caractères spéciaux.
import string

# Pour avoir un input qui ne montre pas les caractères qui sont tapés.
import getpass

# Module pour les algorithmes de hashing.
import hashlib

import json

import random


# Pour lire le fichier .json, ou le créer si il n'existe pas
def file_reader():
    for times in range(2):
        try:
            with open("./password.json", "r") as file:
                password_list_file = file.read()
                return json.loads(password_list_file)
        except (json.JSONDecodeError, FileNotFoundError):
            with open("./password.json", "w") as file:
                empty = {}
                empty_json = json.dumps(empty)
                file.write(empty_json)


# Le menu principal
def menu():
    prompt = input(
        "1) Afficher mots de passe\n"
        "2) Nouveau mot de passe\n"
        "3) Sauvegarder mots de passe\n"
        "4) Quitter\n"
    )
    return prompt


# Pour voir les mots de passe crées
def view_password(password_list):
    for key, value in password_list.items():
        print(f"\nNom: {key}" f"\nHash: {value}")
    return ""


# Menu pour choisir le mode de création de mot de passe
def menu_password_creation():
    prompt = input("1) Manuel\n" "2) Génération automatique\n")
    return prompt


# Prompt pour obtenir le mot de passe, et dire à l'utilisateur si c'est valide.
def get_valid_password(password_list):
    name = input("\nNom:")
    password = getpass.getpass("Mot de passe: ")
    password_hash = hash_password(password)

    if name in password_list:
        return "\nCe nom existe déjà\n"
    elif not is_valid(password):
        return "\nLe mot de passe n'est pas valide\n"
    else:
        return [name, password_hash]


# Pour vérifier si il y a pas de conflits hash, et d'enregistrer le mot de passe si ce n'est pas le cas.
def register_password(input_list):
    name = input_list[0]
    password_hash = input_list[1]
    conflict = False
    for key, value in password_list.items():
        if password_hash == value:
            conflict = True
            return "\nCe mot de passe existe déjà\n"
    password_list[name] = password_hash
    return f"\nCe mot de passe est valide\n" f"Nom: {name}\n" f"Hash: {password_hash}\n"


# Pour sauvegarder les mots de passe dans le fichier .json
def save_password(password_list):
    password_history_json = json.dumps(password_list, indent=4)
    with open("password.json", "w") as file:
        file.write(f"{password_history_json}\n")
        return "Saving..."


# Permet de vérifier si le mot de passe qui est entré correspond aux critères.
def is_valid(password):
    return (
        len(password) >= 8
        and any(character.islower() for character in password)
        and any(character.isupper() for character in password)
        and any(character.isdigit() for character in password)
        and any(character in string.punctuation for character in password)
    )


# Pour générer un mot de passe selon les critères
def password_gen():
    name = input("\nNom:")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    combined = lowercase + uppercase + digits + punctuation

    password = ""

    password = (
        random.choice(lowercase)
        + random.choice(uppercase)
        + random.choice(digits)
        + random.choice(punctuation)
    )

    password_list = [
        password and random.choice(combined) for i in range(random.randint(8, 12))
    ]
    random.shuffle(password_list)
    password_shuffled = "".join(password_list)
    password_hash = hash_password(password_shuffled)
    return [name, password_hash]


# Pour encoder le mot de passe en SHA-256.
def hash_password(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode("ascii"))
    return sha256.hexdigest()


# La liste des mots de passe
password_list = file_reader()


# Boucle principale
while True:
    try:
        # Menu principal
        choice = menu()

        # Affichage mots de passe
        if choice == "1":
            output = view_password(password_list)
            print(output)

        # Création mot de passe
        elif choice == "2":
            choice = menu_password_creation()
            if choice == "1":
                password_output = get_valid_password(password_list)
                if isinstance(password_output, str):
                    print(password_output)
                else:
                    output = register_password(password_output)
                    print(output)
            elif choice == "2":
                password_output = password_gen()
                output = register_password(password_output)
                print(output)

        # Pour sauvegarder les mots de apsse
        elif choice == "3":
            output = save_password(password_list)
            print(output)

        # Pour quitter
        elif choice == "4":
            print("Quitting...")
            break

        # En cas d'option inconnue
        else:
            print("Option inconnue")

    # Pour quitter en faisant CTRL+C
    except KeyboardInterrupt:
        print("\nQuitting...")
        break

    # Pour afficher les erreurs sans arrêter le programme.
    except Exception as e:
        print(f"Erreur: {e}")
