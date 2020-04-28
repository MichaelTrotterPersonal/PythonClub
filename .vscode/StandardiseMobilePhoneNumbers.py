import re

def tidy(func): 
	def wrapper_tidy(pnums):

		pnums_no_spaces = [num.replace(" ","") for num in pnums] #strip all white space
		pnums_no_sixone_or_zeros = [re.sub('(^61|^0)','+61',num) for num in pnums_no_spaces] #substitute leading 61 or 0 with +61
		tidy_pnums = [" ".join([num[i:i+3] for i in range(0, len(num), 3)]) for num in pnums_no_sixone_or_zeros] #add a space between every block of 3 characters 
		
		pnums = func(tidy_pnums) #pass list into tidy_sort for sorting now that the numbers are tidy

		return pnums

	return wrapper_tidy


@tidy #tidy decorator, tidy_sort() is passed to tidy() as an argument
def tidy_sort(pnums):

	pnums.sort()

	return pnums


yucky_phone_numbers=["0412870562", "+61403503991", "61412248021",  "61422 056 723", "0402 222 292", "+61423174844", "0429132197"]

print(tidy_sort(yucky_phone_numbers))

