
from genRandomStr import fFiveWord,lFiveWord
from colorama import Fore as F
from time import sleep

#encoding func
def encoding(words):
		splited_word = words.split()
		myStrList = []
		for word in splited_word:
			#print(word)
			if len(word) >= 3:
				takeStartingWord = word [0]
			#print(takeStartingWord)
				#remove starting word
				rStartingWord = word[1:]
				startingWord = rStartingWord
				#print(startingWord)
				#append starting word in ending
				#firstFinalWord = startingWord + takeStartingWord
				#print(firstFinalWord)
				rWord_1 = fFiveWord()
				rWord_2 = lFiveWord()
				finalWord = rWord_1 + startingWord + takeStartingWord + rWord_2
				myStrList.append(finalWord)
				#print(finalWord)
			else:
				rev_word = word[::-1]
				#print(word)
				myStrList.append(rev_word)
		print("\nYOUR ENCODED WORD IS=>\n"+F.MAGENTA+" ".join(myStrList)+F.RESET)
		return myStrList

def decoding(words):
	splited_word = words.split()
	myStrList=[]
	for word in splited_word:
		#print(word)
		if len(word) >=3:
			#print(word)
			remFirstFiveWord = word[5:]
			#print(remFirstFiveWord)
			remLastFiveWord = remFirstFiveWord[:-5]
			#print(remLastFiveWord)
			takeLastWord = remLastFiveWord[-1]
			remLastWord = remLastFiveWord[:-1]
			finalWord= takeLastWord + remLastWord
			#print(tempFinalWord)
			myStrList.append(finalWord)
		else:
			rev_me = word[::-1]
			myStrList.append(rev_me)
	print("\nYOUR DECODED WORD IS :\n"+F.MAGENTA+" ".join(myStrList)+F.RESET)
	return myStrList


#decoding("9cQgqellohHuTeQ ym 4ImjcamencORF3 si W4uk6HMED-ORACLEAsq4n8")

#some shit things (you can ignore it)
print(F.CYAN+"\n\tENCODER & DECODER BY AHMED-ORACLE")
print("-"*43)
print(F.RED+"READ ME!!!"+F.RESET)
print("WHAT DO YOU WANNA DO\n"+F.BLUE+"ENCODING"+F.BLACK +" ||"+F.YELLOW+" DECODING"+F.BLACK)
print("FOR ENCODING ENTER "+F.BLUE+"E"+F.BLACK)
print("FOR DECODING ENTER "+F.YELLOW+"D"+F.BLACK)
print(F.RED+"ENTER EXIT FOR EXIT\n"+F.BLACK)

yourChoice = input(F.WHITE+"ENTER YOUR CHOICE: "+F.MAGENTA).upper()
print(F.RESET)
while 1:
	if yourChoice == "E":
		user_word = input("\nENTER YOUR ENCODING WORD: ")
		encoding(user_word)
		print("\nWHAT YOU WANNA DO NEXT\nE FOR ENCODING || D FOR DECODING ||\nENTER EXIT FOR EXIT")
		en_dc_again = input("\nENTER YOUR CHOICE: ").upper()
		if en_dc_again == "E" or en_dc_again == "ENCODING":
			enc_word = input("\nENTER YOUR ENCODING WORD: ")
			encoding(enc_word)
			break
		elif en_dc_again == "D" or en_dc_again == "DECODING":
			dec_word = input ("\nENTER YOUR DECODING WORD:")
			decoding(dec_word)
			break
		elif en_dc_again == "EXIT" or en_dc_again == "EX":
			print("\nYOU HAVE BEEN EXITED\nAS YOU HAVE ENTERED EXIT")
			break
		else:
			print("\nWRONG PROMPT\nRE-RUN YOUR PROGRAM AND ENTER CORRECT FORM")
			break
					
		# print("\nWANNA ENCODE AGAIN")
		# print("Y FOR YES || N FOR NO || D FOR DECODING")
		# encode_decode_again=input("\nENTER YOUR CHOICE: ").upper()
		# if encode_decode_again == "Y":
		# 	user_word = input("ENTER YOUR ENCODING WORD: ")
		# 	encoding (user_word)
		# elif encode_decode_again == "N":
		# 	print(F.MAGENTA+"\nOK NO ENCODING"+F.RESET)
		# 	break
		# elif encode_decode_again == "D":
		# 	decode_again=input("ENTER YOUR DECODING WORD:")
		# 	decoding(decode_again)
		# else:
		# 	print("\nYOU HAVE ENTERED WRONG PROMPT!!!")
		# 	break
	elif yourChoice == "D":
		user_word = input("\nENTER YOUR DECODING WORD: ")
		decoding(user_word)
	elif yourChoice == "EXIT":
		print("\nYOU HAVE BEEN EXITED SUCCESSFULLY!!!")
		break
	else:
		print("\nWORNG PROMPT")
		break

	
	



