import string

import getpass

import hashlib
sha256 = hashlib.sha256()


def is_valid(input_string):
    punctuations = [punctuation for punctuation in string.punctuation]

    if (
        len(input_string) >= 8
        and any(character.islower() for character in input_string)
        and any(character.isupper() for character in input_string)
        and any(character.isdigit() for character in input_string)
        and any(character in punctuations for character in input_string)
    ):
        return True
    else:
        return False


while True:
    password = getpass.getpass("Entrez un mot de passe: ")

    if not is_valid(password):
        print("Le mot de passe n'est pas valide")
        continue
    else:
        print("Le mot de passe est valide!")
        break

sha256.update(password.encode("ascii"))

password_hash = sha256.hexdigest()
print(f"Le hash du mot de passe:\n{password_hash}")
