import random

print('To jest mini-gra, w której komputer rzuca monetą 100 razy\n'
      ', następnie informuje Cię o ilości wyrzuconych orzełków i reszek\n')

print('This is a mini-game in which the computer flips a coin 100 times,\n'
      ' then informs you about the number of heads and tails.')

go = str(input('wpisz \'START\' aby rozpocząć - Type \'START\''))

orzel = 0
reszka = 0

if go == 'START':

    for _ in range(100):
            try1 = random.choice(['heads', 'tails'])
            if try1 == 'heads':
                  orzel += 1
            else:
                  reszka += 1

print(f'Orzeł wypadł {orzel} razy')
print(f'Reszka pokazała się {reszka} razy')
#print(f'{one_hundred_times}')






'''
generuj losowa liczbe x 100
wynik to - jesli wynik
jesli liczba ma modulo 0 to orzel czyli parzysta - ORZEŁ
jelsi liczba ma modulo rozne od 0 czyli nieparzysta - RESZKA
count Orzeł
count Reszka

print(count1, count2)

'''








