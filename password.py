# Permet d'importer string.punctuation, car il n'y a pas de string method pour les caractères spéciaux.
import string

# Pour avoir un input qui ne montre pas les caractères qui sont tapés.
import getpass

# Module pour les algorithmes de hashing.
import hashlib


# Permet de vérifier si le mot de passe qui est entré correspond aux critères.
def is_valid(password):
    return (
        len(password) >= 8
        and any(character.islower() for character in password)
        and any(character.isupper() for character in password)
        and any(character.isdigit() for character in password)
        and any(character in string.punctuation for character in password)
    )


# Pour encoder en SHA-256.
def hash_password(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode("ascii"))
    return sha256.hexdigest()


# Boucle principale
while True:
    password = getpass.getpass("Entrez un mot de passe: ")

    if not is_valid(password):
        print("Le mot de passe n'est pas valide")
        continue
    else:
        print("Le mot de passe est valide!")
        password_hash = hash_password(password)
        print(f"Le hash du mot de passe:\n{password_hash}")
        break
