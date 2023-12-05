# Permet d'importer string.punctuation, car il n'y a pas de string method pour les caractères spéciaux.
import string

# Pour avoir un input qui ne montre pas les caractères qui sont tapés.
import getpass

# Module pour les algorithmes de hashing.
import hashlib


password_history = {}


# Le menu principal
def menu():
    prompt = input(
        "1) Afficher hash mots de passe\n" "2) Nouveau mot de passe\n" "3) Quitter\n"
    )
    return prompt


def view_password(dict):
    for name, password_hash in dict.items():
        if name == None:
            break
        print(f"\nNom: {name}\n" f"Hash: {password_hash}\n")


# Prompt pour obtenir le mot de passe, et dire à l'utilisateur si c'est valide.
def get_valid_password(dict):
    name = input("\nNom:")
    password = getpass.getpass("Mot de passe: ")
    password_hash = hash_password(password)

    if name in dict:
        return "\nCe nom existe déjà\n"
    elif not is_valid(password):
        return "\nLe mot de passe n'est pas valide\n"
    else:
        dict[name] = password_hash
        return (
            f"\nLe mot de passe est valide!\n"
            f"Nom: {name}\n"
            f"Le hash du mot de passe:\n"
            f"{password_hash}\n"
        )


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


# Boucle principale
while True:
    try:
        choice = menu()
        if choice == "1":
            view_password(password_history)
        elif choice == "2":
            output = get_valid_password(password_history)
            print(output)
        elif choice == "3":
            print("Quitting...")
            break
        else:
            print("Option inconnue")
    except KeyboardInterrupt:
        print("\nQuitting...")
        break
    except Exception as e:
        print(f"Erreur: {e}")
