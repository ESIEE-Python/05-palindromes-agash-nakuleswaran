#### Fonction secondaire
import unicodedata
import string

def ispalindrome(p):
    """
    Vérifie si une chaîne de caractères est un palindrome.
    
    Args:
        p (str): La chaîne de caractères à vérifier.

    Returns:
        bool: True si p est un palindrome, False sinon.
    """
    # Normalisation pour enlever les accents
    normalized = unicodedata.normalize('NFD', p)
    cleaned = ''.join(c for c in normalized if unicodedata.category(c) != 'Mn')

    # Création de la table de traduction pour enlever la ponctuation et les espaces
    table = str.maketrans('', '', string.punctuation + ' ')
    cleaned = cleaned.translate(table).lower()
    
    # Vérification si la chaîne nettoyée est un palindrome
    return cleaned == cleaned[::-1]

#### Fonction principale

def main():
    """
    Fonction principale qui teste plusieurs chaînes pour déterminer si elles sont des palindromes.
    """
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()

