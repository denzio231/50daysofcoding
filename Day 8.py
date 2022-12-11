def odd_even(nums):
    odd = []
    even = []
    for num in nums:
        if num%2 == 0:
            even.append(num)
        else:
            odd.append(num)
    odd.sort()
    even.sort()
    return even[-1] - odd[0]
print(odd_even([1,2,4,6]))


def prime_numbers(number):
    prime = True
    to_return = []
    for nums in range(2,number):
        for nums2 in range(2,nums):
            if nums % nums2 == 0:
                prime = False
        if prime:
            to_return.append(nums)
        prime = True
                
    return to_return
print(prime_numbers(10))
            
