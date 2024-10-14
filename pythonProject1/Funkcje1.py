from math import factorial


def wydrukuj_instrukcje():
    print('paczek 1')
    print('paczek 2')
    print('paczek 3')
    print('paczq9')
    a = 22
    b = 33
    c = a + b
    print(a)
    print(a + b + c)

print('tu zaczyna się funkcja: \n\n')

wydrukuj_instrukcje()

def cheer(who_to_cheer):
    print(f'siema {who_to_cheer}!')

cheer('Pączek')





print('\n\n')
def suma(zmienna1, zmienna2):
    print(f'suma zmiennej {zmienna1} oraz zmiennej {zmienna2} ')
    print(zmienna1+zmienna2)

suma(10,20)


print('\n\n')
print('\t \\ silnia \\')
print((factorial(5)))
print("\a")
print('łańcuchy specjalne ale też pomnożone wyświetlą się tyle razy jaki jest podany ich iloraz')
print(' \' \' ' * 10)
#input("aby zakończyć program wciśnij Enter")

quote = 'program zakonczony - opcja duzych liter \'on\''

print(quote.upper())
print(quote.replace('opcja', 'stan' ))

car = input('ile wydales na auto?: ')
car = int(car)
house = input('ile wydales na dom?: ')
house = float(house)

total = car + house
print('\n wydales: ', total, 'pln')


