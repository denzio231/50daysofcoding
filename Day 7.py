def str_range(num):
	return str(list(range(0,num))).replace(',','.').replace('',' ' ).replace('[','').replace (']', '') 
	
def nameswiths(names):
	to_return = {}
	for name in names:
		
		if name[0].lower() == "s" and name not in to_return:
			to_return[name]= 1
		elif name[0].lower() == "s":
			to_return[name] += 1
	return to_return
		
print(str_range(5))
print(nameswiths(["Adam","Sasha","Wopal","Sala","Sala"]))
