# Les imports pour générer des chaines de caractères pour les tests
import random
import string

# Fonction qui permet d'afficher le miroir d'un texte
def miroir_str(initial_string):
    final_string = ''
    index = len(initial_string)
    while index > 0:
        final_string += initial_string[index - 1]
        index = index - 1
    return final_string

def rand_str(taille:int):
    return random.choices(string.ascii_uppercase, k=taille)

for i in range(0,10):
    t = ''.join(rand_str(10))
    print(f'{t} ========== >  {miroir_str(t)}')
