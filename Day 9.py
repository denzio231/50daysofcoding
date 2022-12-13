def biggest_odd(numbers):
    list = []
    to_return = 0
    for num in numbers:
        list.append(int(num))
    list = sorted(list)
    for n in list:
        if n % 2 != 0:
            to_return = n
    return to_return

def zeros_last(list):
    i = 0
    Saved = list[:] 

    list = sorted(list)
    for num in list:
        if num == 0:
            i+=1
    if i == 0:
        return list
    
    for n in range(0,i):
        Saved.remove(0)
        Saved.append(0)
    return Saved
            









print(zeros_last([1,0,9,3,2]))


print(biggest_odd('23569'))
