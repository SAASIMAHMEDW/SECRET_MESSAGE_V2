from string import ascii_letters,digits
from random import sample

#string.ascii_letters
#strimg.ascii_upppercase
#string.ascii_lowercase
#string.digits
#string.punctuation
#string.hexdigits
#string.octdigits

#first five word
def fFiveWord():
	myStr = ascii_letters
	myDigits = digits
	combination = myStr + myDigits
	len = 5
	rWord_1 = "".join(sample(combination,len))
	#print(rWord_1)
	return rWord_1

#last five word
def lFiveWord():
	myStr = ascii_letters
	myDigits = digits
	combination = myStr + myDigits
	len = 5
	rWord_2 = "".join(sample(combination,len))
	#print(rWord_2)
	return rWord_2

if __name__ == "__main__":
	print(fFiveWord())
	print(lFiveWord())
