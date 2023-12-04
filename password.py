import string

import getpass

punctuations = [punctuation for punctuation in string.punctuation]

while True:
    password = getpass.getpass("Entrez un mot de passe: ")

    if len(password) >= 8:
        length_good = True
    else:
        length_good = False

    contains_lowercase = any(character.islower() for character in password)
    contains_uppercase = any(character.isupper() for character in password)
    contains_digit = any(character.isdigit() for character in password)
    contains_punctuation = any(character in punctuations for character in password)


    if (
        length_good == True and
        contains_lowercase == True and
        contains_uppercase == True and
        contains_digit == True and
        contains_punctuation == True
        ):
        print("Le mot de passe est valide et sera enregistré")
        break
    else:
        print("Le mot passe est invalide, veuillez re-essayé")
