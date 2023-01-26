string = input('Insert a String: ')
integer = input('Insert an Integer: ')
if(int(integer)) > len(string):
    print('Error: Index Out of Range')
else:
    print(string[int(integer)], string[-int(integer)])