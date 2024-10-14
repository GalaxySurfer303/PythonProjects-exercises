
print('ćwiczenia pętli while')
print('\n\n')

printed_times = 0

while printed_times <= 5:
    print(f'Wypisane dla =  {printed_times}')
    printed_times = printed_times + 1
    #printed_times =+ 1

    #dopóki zmienna printed_times jest mniejsza od 5 do tego czasu wypisuj napis "Wypisane dla = "
    #dodaje to 'printed_times =+ 1' - to jest glowny motor petli
print('\n\n')



i = 7
while i <100:
    print(i)
    i += 7

for i in range(0, 100):
    print(f'wynik funkcji range 1-100 {i + 0.3}')


for i in range(0, 5, 100):
    print(f'wynik funkcji range 1-100 {i + 0.1}')
    i =+ 1

 

def wydrukuj_instrukcje():
    print('paczek 1')
    print('paczek 2')
    print('paczek 3')
    a = 22
    b = 33
    c = a + b
    print(a)
    print(a+b+c)

    wydrukuj_instrukcje()


