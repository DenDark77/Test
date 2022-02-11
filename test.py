
def like(*args):
    list=[]
    
    for name in args:
        for names in name:
            if len(name) > 10 or (names.isalpha() == False and name != ['']):
                return('Ошибка')
            elif name == ['']:
                return('Это никому не нравиться')
            else:
                list.append(names + ',')
    
    return(list)

lists=like(input().split(', '))

if len(lists) == 1 and 'Ошибка' not in lists and 'Это никому не нравиться' not in lists:
    print(*lists, 'лайкнул это')
elif 'Ошибка' in lists:
    print('Ошибка')
elif 'Это никому не нравиться' in lists:
    print('Это никому не нравиться')
else:
    print(*lists, 'лайкнули это')
