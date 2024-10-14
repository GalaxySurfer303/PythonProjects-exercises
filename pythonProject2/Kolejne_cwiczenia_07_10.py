#tworzenie slownika opcja 1
slownik = {'prog' : 'programowanie' , 'gam' : 'gaming' , 'sp' : 'spanie' , 'oek' : 'odpoczynek'}

#tworzenie slownika opcja 2
moj_slownik = dict()

#dodawanie klucza i wartosci do slownika
moj_slownik['bg'] = 'bieganie'
moj_slownik['pi'] = 3.14

#wyswietlanie slownikow i sprawdzanie czy pojawiaja sie wskazane klucze
print(slownik)
print(moj_slownik['pi'])
print('bg' in moj_slownik)
print('fg' not in moj_slownik)

#usuwanie ze słownika

del slownik['sp']
print(slownik)


opcje = {'1':'PLAY >' , '2':'STOP []' , '3':'PAUSE ||' , '4':'REV <<,' , '5':'FWD .>>' , '6':'RECORD *'}

print('\nto jest magnetofon\nwłożyłeś kasetę\n')
print('1-odtwarzanie\n2-zatrzymanie\n3-pauza\n4-przewijanie w tył\n5-przewijanie do przodu\n6-nagrywanie')
n = input('\npodaj liczbę, a ja powiem czy magnetofon działa: ')

if n in opcje:
    opcja = opcje[n]
    print(f'Magnetofon odpowiada:{opcja}')
else:
    print(100 * ('!!!Magnetofon nie ma takiej opcji, nie żartuj!!!\n'))
    










