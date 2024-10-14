import random
import time

'''
#import opcji generowania liczb

proba1 = random.randint(1,6)
proba2 = random.randrange(6) + 1

password = input('Wprowadz haslo: ')
if password == 'Harry123':
    print('access permit')
else:
    print('access denied')
'''

""""
def print_sum(zmienna1, zmienna2):
    print(zmienna1+zmienna2)

print_sum(3,4)
"""

""""
#stars = '*'
ilosc_Gwiazd = int(input('ile gwiazd mam pokazać?: '))

if ilosc_Gwiazd > 100:
    print('podałeś liczbę większą niż 100, potrzebujesz aż tylu ?')

elif ilosc_Gwiazd <= 0:
    print('gwiazd nie może być \'NIC\' minus oznaczalby, ze gwiazdy zostaly wchloniete przez czarna dziure')
else:
    print(f'{ilosc_Gwiazd} gwiazd swieci dla Ciebie')
    print('*' * ilosc_Gwiazd)

#ilość gwiazd wersja w funkcji
"""

""""
def ilosc_gwiazd2 ():
    star = int(input('podaj liczbę gwiazd'))
    if star > 100:
        print('podałeś liczbę większą niż 100, potrzebujesz aż tylu ?')

    elif star <= 0:
        print('gwiazd nie może być \'NIC\' minus oznaczalby, ze gwiazdy zostaly wchloniete przez czarna dziure')
    else:
        print(f'{star} gwiazd swieci dla Ciebie')
        print('*' * star)

ilosc_gwiazd2()
"""

"""
fruit = ['grapefruit', 'mango', 'passion_fruit', 'banan', 'pomelo', 'mango']
fruit.append("figa")
fruit.append("orange")
print(fruit)
print(fruit[7])
print(len(fruit))

paczek = ['jagodzianka' , 'bajaderka' , 'beza' , 'wuzetka' , 'kremowka' , 'gowno']

if paczek[2] == 'beza':
    print('to jest beza')

input('podaj liczbę od 0 do 5 aby dowiedziec sie czym jestes? : ')

jagodzianka = paczek[0]
bajaderka = paczek[1]
beza = paczek[2]
wuzetka = paczek[3]
kremowka = paczek[4]
gowno = paczek[5]
"""

#print(1000 * 60 * 60 * 24)

#zamiana dni na milisekundy
def day_to_mills(x):
    return x * 1000 * 60 * 60 * 24
print(day_to_mills(2))

#obliczanie pola trojkata
def triangle_area(a,b):
    return a * b / 2
print(triangle_area(1,1))

#wybor najwiekszej liczby z podanych wartosci
def biggest(x,y,z):
   return max(x,y,z)
print(biggest(5,10,20))

print('\n\noperacja ne listach')

#wielkie litery
slowo = 'operacje na listach'
slowo_upper = slowo.upper()
print(slowo_upper)

#Listy i operacje na lista
Lista = ['mapa', 'zegarek' , 'termos' , 'czekolada' , 'czapka' , 'kurtka' , 'okulary' , 'lornetka']
print(f'elementy listy = + {Lista}')
print(f'dlugosc listy =  {len(Lista)} ')
#print(len(Lista))

#wybieranie obiektow z listy
owoc = 'kiwi'
print(owoc)
litery = owoc[2]
print(litery)

odpowiedz = input('czy chcesz sprawdzić swoj nastrój (tak/nie) : ')
odpowiedz = str(odpowiedz)

if odpowiedz == 'tak':
    print('przechodze do sprawdzania Twojego nastroju, używając skomplikowanych algorytmów...')

    ten_seconds=[]
    for i in range(11):
        ten_seconds.append(i)
        ten_seconds.reverse()
    print('START ODLICZANIA')
for k in(ten_seconds):
    time.sleep(1) #- opóźnienie 1 sek
    print(k)
print('KONIEC ODLICZANIA')







