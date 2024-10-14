price = 1.4
print(f'x =  {price}')


value = 1234
print('wartosc to ' + str(value))


kieszen_paczka = 'Pusta'
print(f'kieszen paczka jest {kieszen_paczka}')

#kieszen_paczka = 'Pusta'
#print('kieszen paczka jest ' str(kieszen_paczka))

a = 'A'
b = 'B'

print(f'a = {a} \nb = {b}' )

name = None
print(name is None)
print(kieszen_paczka is str('Pusta'))

#print("___" \n "__")


paczek_style = "cool"
kleju_style ="cool"
sebix_style = "not_cool"

if paczek_style == "ncool":
    print("paczek nie ma stylu")
elif kleju_style == "nncool":
    print("Kleju to lamus")
elif sebix_style == "cool":
    print('seba jest faszjonista')
elif sebix_style == "not_cool":
    print ('Pączek ma Styl')
    print ('Kleju też miewa')
    print ('seba ma czerwone buty')

print('\n\n')
print('wyrażenia logiczne')

is_grounded = 'ma szlaban'
passed_test = 'zdał test'
cleaned_room = 'posprzątał pokój'
print('- ' + is_grounded + ' \n- ' + passed_test + '\n- ' + cleaned_room )

print('\n\n')

#cleaned_room = False
#passed_test = True

if not (cleaned_room or not passed_test):
    print('nie jest tak, że ' + cleaned_room + ' albo  ' + 'nie' +  passed_test + 'u')
else:
    print('if not (cleaned_room or not passed_test)')
    print('nie jest tak, że ' + cleaned_room + ' albo ' + 'nie ' + passed_test + '-u')

print('\n\n')
print('ćwiczenia')


has_computer = True
passed_test = False
is_grounded = False

print(has_computer and passed_test)
print(passed_test or is_grounded)
print(has_computer and not passed_test)

can_play_games = has_computer and not is_grounded
print(can_play_games)

if not passed_test:
    is_grounded = True

    print(can_play_games)
    print(passed_test or not is_grounded)
    print(not (not has_computer or not passed_test))


