#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        L =[]
        for i in range(1,11):
            valeurs = input("choisissez une valeur: \n")
            L.append(valeurs)
    return sorted(L)


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        mot1 = input("choisissez un premier mot \n")
        mot2 = input("choisissez un premier mot \n")
        if len(mot1) == len(mot2):
            i = 0
            while i < len(mot1):
                if mot1[i] == mot2[len(mot2)-1-i]:
                    print('ok')
                    i += 1
                else:
                    break

        else:
            print('no')


def contains_doubles(items: list) -> bool:
    ensemble = set(items)
    return len(ensemble) != len(items)



def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_student = dict()
    for key, value in student_grades.items():
        avg = sum(value)/len(value)

        if len(best_student) == 0 or list(best_student.values())[0] < avg:
            best_student = {key: avg}

    return best_student



def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    frequency = dict()
    for letter in sentence:
        frequency[letter] = sentence.count(letter)

    sorted_keys = sorted(frequency,key =frequency.__getitem__, reverse = True)
    for key in sorted_keys:
        if frequency[key] > 5:
            print("Le caractere {0} revient {1} fois.".format(key, frequency[key]))



def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    recette = input("choisissez nom recette")
    ingredients = input("choisissez ingredients en séparant par des virgules").split(",")
    d = dict()
    d[recette] = ingredients
    return d



def print_recipe(ingredients: dict) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    deman = input("choiss nom recette")
    if deman in ingredients:
        print(ingredients[deman])
    else:
        print("recette n'existe pas")
        print_recipe(ingredients)



def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [1, 1, 5, 6, 16, 0]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
