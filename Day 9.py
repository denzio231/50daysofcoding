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
    list = sorted(list)
    for num in list:
        if num == 0:
            i+=1
    
    for n in range(0,i):
        list.remove(0)
        list.append(0)
    return list
            









print(zeros_last([1,0,9,3,0,2]))


print(biggest_odd('23569'))
