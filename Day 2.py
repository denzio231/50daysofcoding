
def convert_add(list_num):
    to_return = 0
    for num in list_num:
        to_return += int(num)
    return to_return



def check_duplicates(list_str):
    flag =  False
    l = set()
    i = 1
    r = 1
    for items in list_str:
        
        for robins in list_str:
            if items == robins and i != r:
                flag = True
                l.add(items)
            r += 1
        r = 1
        i += 1
    if flag:
        return l
    else:
        return 'No duplicates'
        
    
    
        
    
print(convert_add(['1','2']))
print(check_duplicates( ['apple', 'apple', 'peach', 'peach', 'banana']))
