text = input('Insert a string: ')
if len(text) > (20):
    print(text[(len(text) - 20):len(text)])
else:
    print(text.rjust(20))