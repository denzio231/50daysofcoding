def word_count(string):
	char_count = 0
	word_count = 0
	special_count = 0
	is_word = False
	for letter in string:
		if letter != ' ':
			char_count += 1
		if letter.isalpha():
			is_word=True
		elif not letter.isalpha() and is_word:
			word_count += 1
		if not letter.isalnum():
			special_count +=1
	if is_word:
		word_count +=1
	return [word_count,special_count,char_count]
print(word_count('Python has a string format operator %. This functions analogously to printf format strings in C, e.g. "spam=%s eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2".'))
