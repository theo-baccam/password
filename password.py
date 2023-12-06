# Permet d'importer string.punctuation, car il n'y a pas de string method pour les caractères spéciaux.
import string

# Pour avoir un input qui ne montre pas les caractères qui sont tapés.
import getpass

# Module pour les algorithmes de hashing.
import hashlib

import json


def file_reader():
    try:
        with open("./password.json", "r") as file:
            password_list_file = file.read()
            return json.loads(password_list_file)
    except (json.JSONDecodeError, FileNotFoundError):
        with open("./password.json", "w") as file:
            empty = {}
            empty_json = json.dumps(empty)
            file.write(empty_json)
        with open("./password.json", "r") as file:
            password_list_file = file.read()
            return json.loads(password_list_file)


# Le menu principal
def menu():
    prompt = input(
        "1) Afficher mots de passe\n"
        "2) Nouveau mot de passe\n"
        "3) Sauvegarder mots de passe\n"
        "4) Quitter\n"
    )
    return prompt


def view_password(password_list):
    for key, value in password_list.items():
        print(f"\nNom: {key}"
              f"\nHash: {value}"
        )
    return ""


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


def register_password(input_list):
    name = input_list[0]
    password_hash = input_list[1]
    for key, value in password_list.items():
        if password_hash == value:
            conflict = True
        else:
            conflict = False
    if conflict == False:
        password_list[name] = password_hash
        return(
            f"\nCe mot de passe est valide\n"
            f"Nom: {name}\n"
            f"Hash: {password_hash}\n"
        )
    else:
        return "\nCe mot de passe existe déjà\n"


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


# Pour encoder le mot de passe en SHA-256.
def hash_password(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode("ascii"))
    return sha256.hexdigest()


password_list = file_reader()


# Boucle principale
while True:
    try:
        choice = menu()
        if choice == "1":
            output = view_password(password_list)
            print(output)
        elif choice == "2":
            password_output = get_valid_password(password_list)
            if isinstance(password_output, str):
                print(password_output)
            else:
                output = register_password(password_output)
                print(output)
        elif choice == "3":
            output = save_password(password_list)
            print(output)
        elif choice == "4":
            print("Quitting...")
            break
        else:
            print("Option inconnue")
    except KeyboardInterrupt:
        print("\nQuitting...")
        break
    except Exception as e:
        print(f"Erreur: {e}")
