import random
import pdb#import metody random

#pokazyje tytuł wypisany wielkimi literami
title = 'To jest program - Zgadnija liczbę'
new_title = title.upper()
print(new_title)

#opcja wyswietlenia tyt normalnym tekstem
#print('To jest program - Zgadnija liczbę \n')

print('\nPostaraj się odnaleźć wygenerowanąprzez komputer liczbę w jak najmniejszej liczbie prób')

generated_number = random.randint(1, 100)

#zgadywany numer = zamien na intidżer(pobierz wartosc)
guessed_number = int(input('\033[37mPodaj liczbę: \033[0m')) #wyswietla z kolorem

tries = 1

while generated_number != guessed_number:
    if guessed_number > generated_number:
        print('\033[31mNie udałoi Ci się odgadnąć, podałeś za dużą wartość, próbuj dalej...\033[0m') #wyswietla z kolorem
    else:
        print('\033[31mNie udałoi Ci się odgadnąć, podałeś za małą wartość, próbuj dalej...\033[0m')

    guessed_number = int(input('\033[37mPodaj liczbę: \033[0m'))
    tries += 1

    if tries <= 3:
        print(f'Dobry wynik, zrobiłeś(aś) to w {tries} ruchach')
    else:
        print('Nieźle ale więcej niż 3 ruchy to średni wynik')
    break

print(f'Brawo! ta liczba to {guessed_number}')
print(f'Potrzebowałeś(aś) {tries} ruchów')
input('Naciśnij Enter abyu zakończyć')

pdb.set_trace()
