
class Paris(object):
    def __init__(self):
        print('to sie wykona najpierw')

    def talk(self):
        print('objekt talk')

    def count(self, number):
        number = 10
        operation = 'nie wie mco robie'
        for _ in range(10):
            print(operation)
            number += 1

objek1 = Paris()
#objek1.count()



author = 'Jan Tuwim'
year = '1873'
nowy_format = f'{author} urodził sie w {year} roku'.format(author, year)
print(nowy_format)




