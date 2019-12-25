with open('xmen.txt', 'w+') as my_file:
    my_file.write('Beast\n')
    my_file.write('Phoenix\n')
    my_file.writelines(['Lena\n'])

my_file = open('xmen.txt', 'r')
with my_file:
    print(my_file.read())
