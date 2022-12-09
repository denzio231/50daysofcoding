def username(email):
	return email.split('@')[0]

print(username('denzio@gmail.com'))

def zeroed(nums):
	nums [0],nums[-1] = 0,0
	return nums

	
print(zeroed([1,3,5,7,9,11]))
