def only_floats(a,b):
    to_return = 0
    if type(a) == float:
        to_return += 1
    if type(b) == float:
        to_return += 1
    return to_return
def word_index(word_list):
    max_index = 0
    i = 0
    for word in word_list:
        if len(word) > len(word_list[max_index]):
            max_index = i
        i += 1
    return max_index
    
print(only_floats(1.2,3))
print(word_index( ["Hate", "remorse", "vengeance"]))
print(word_index(["Hate","Love"]))
