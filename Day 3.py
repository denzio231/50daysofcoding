def register_check(dictionary):
    counter = 0
    for k,v in dictionary.items():
        if v.lower() == 'yes':
            counter += 1
    return counter
print(register_check({'Michael' : 'yes', 'John' : 'no' , 'Peter' : 'Yes', 'Mary':'Yes'}))
            
def lowercase(l):
    to_return = []
    for items in l:
        if items.lower() == items:
            to_return.append(items)
    return tuple(to_return)
            
            
print(lowercase( ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]))
