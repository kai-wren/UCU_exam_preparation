from array import array
from random import shuffle

horses = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12', 'H13', 'H14', 'H15', 'H16', 'H17', 'H18', 'H19', 'H20', 'H21', 'H22', 'H23', 'H24', 'H25']

def race(list):
    shuffle(list)
    return list

def tournament(horses_list):
    i = 0
    count = 0
    while i < len(horses_list)-4:
        print(i)
        print(horses_list[i:i+5])
        horses_list[i:i+5] = reversed(race(horses_list[i:i+5]))
        print(horses_list[i:i+5])
        i = i+2
        count = count+1
    print('count =', count)
    print(horses_list)
    return horses_list[len(horses_list)-3:len(horses_list)]
        

res = tournament(horses)
print(res)
