import sys

file_name = 'recepes.txt'

try:
    my_file= open(file_name, 'w')
    my_file.write('Meatballs\n')
    my_file.close()
except:
    print('The file ' + file_name + ' already exists.')
    sys.exit(1)
