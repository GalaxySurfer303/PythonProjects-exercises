
#pierwsza najwazniejsza opcja, gdzie nie bylo jej opsu w 3 książkach, to dla autorow jest tak oczywiste,
#żz nie napisali, ze kolejny element do kontenerow danych dodaje sie na koncu, to samo tyczy sie usuwania

main_container = []
techno = ['Robert Hood', 'Derrick May' , 'Plastikam' , 'Adam Beyer' , 'Ben Sims' , 'UVB' , 'Abdullah Rashim' , 'Marcel Dettmann']
electro = ['Aux88' , 'Exzakt' , 'Galaxy Surfer' , 'Drexciya' , 'Ectomorph' , 'DJ Stingray 313' , 'Alien FM']
dance = ['Pączek Dance' , 'Space Pączek' , 'Backstreet Pączek' , 'N-Pączek' , 'Destinity Pączek']

main_container.append(techno)
main_container.append(electro)
main_container.append(dance)

techno = main_container[0]
electro = main_container[1]
dance = main_container[2]

#print(techno)

# Dodanie jednego elementu
techno.append('Techno Pączek')

# Lub, jeśli chcesz dodać kilka elementów
techno.extend(['Techno Pączek2', 'Piotr Klejment'])




#definijuje nowa liste
locations = []

#dodaje liste do mojej glownej listy
main_container.append(locations)

print(main_container[3])
print('\n\n')

#definiuje krotkę
warsaw = (56.4567, 76.2345)
cracow = (57.5623, 79.6345)
la = (34.5346, 63.2345)

#dodaje krotke do glownego kontenera
locations.append(warsaw)
locations.extend([cracow, la])
print('ostatni lista - locations')
print(main_container[3])
print('\n\n')
#print('wszystkie dane z list i krotek umieszcoznych na liscie \'main container\'')
print('\033[31mwszystkie dane z list i krotek umieszcoznych na liscie \'main container\'\033[0m')
print(main_container)