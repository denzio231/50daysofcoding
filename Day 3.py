def register_check(dictionary):
    counter = 0
    for k,v in dictionary.items():
        if v.lower() == 'yes':
            counter += 1
    return counter

def lowercase(l):
    to_return = []
    for items in l:
        if items.lower() == items:
            to_return.append(items)
            print(to_return)
    return tuple(to_return)
            
            
