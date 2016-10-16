#To pretty print the json packets easily

import json
from glob import glob
from pprint import pprint

files = glob('*.txt')

print('Key : File\n----------')

for file in files:
    print("{}   : {}".format(files.index(file), file))

choice = int(input('\n\nWhich file do you want Pretty Printed?\n'))

with open(files[choice]) as file:
    file = json.load(file)
    pprint(file)

close = False
while close == False:

    next_thing = input('Press enter to exit, or type a key to Pretty Print smaller sections\n')

    if next_thing == '':
        close = True

    try:
        file = file[next_thing]
        pprint(file)
    except KeyError:
        print('invalid key')
