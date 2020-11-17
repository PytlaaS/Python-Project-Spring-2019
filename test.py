# Definie une fonction
def main():
    age = input("How old are you?")
    name = input("What's your name?")
    print("Hello " + name + " agé de " + str(age) + " ans")
    print("Je vais donc calculer ta moyenne!")
    note_1 = int(input("Quelle est ta moyenne en Math ? "))
    note_2 = int(input("Celle d'anglais ? "))
    note_3 = int(input("Et celle de physique ? "))
    moyenne = int((note_1 + note_2 + note_3) / 3)
    if moyenne <= 14:
        print("T'es Mauvais " + name + " T'es Mauvais! ")
        print(f"Avec un résultat excecrable comme {moyenne} de moyenne tu compte reussir dans la vie ? ")
    else:
        print("Bravo " + name + " t'es un champion! ")
        print(f'Avec des resultat comme {moyenne} de moyenne tu pourrais bien devenir notre prochain président')


if __name__ == '__main__':
    main()
