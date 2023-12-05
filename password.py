# Permet d'importer string.punctuation, car il n'y a pas de string method pour les caractères spéciaux.
import string

# Pour avoir un input qui ne montre pas les caractères qui sont tapés.
import getpass

# Module pour les algorithmes de hashing.
import hashlib


# Le menu principal
def menu():
    prompt = input(
        "1) Afficher hash mots de passe\n" "2) Nouveau mot de passe\n" "3) Quitter\n"
    )
    return prompt


# Prompt pour obtenir le mot de passe, et dire à l'utilisateur si c'est valide.
def get_valid_password():
    password = getpass.getpass("\nEntrez un mot de passe: ")

    if not is_valid(password):
        return "Le mot de passe n'est pas valide"
    else:
        password_hash = hash_password(password)
        return (
            f"Le mot de passe est valide!\n"
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
        if choice == "2":
            output = get_valid_password()
            print(output)
        if choice == "3":
            print("Quitting...")
            break
    except KeyboardInterrupt:
        print("\nQuitting...")
        break
    except Exception as e:
        print(f"Erreur: {e}")
