##PYTHON PROJECT 3
import random
def main():
	#DECLARE VARABLES TO BE REFERENCED LATER
	format = "#" * 60

	_DICE = [
	[1, " ________ \n|        |\n|   O    |\n|        |\n ________ "],
	[2, " ________ \n|O       |\n|        |\n|       O|\n ________ "],
	[3, " ________ \n|O       |\n|   O    |\n|       O|\n ________ "],
	[4, " ________ \n|O      O|\n|        |\n|O      O|\n ________ "],
	[5, " ________ \n|O      O|\n|   O    |\n|O      O|\n ________ "],
	[6," ________ \n|O      O|\n|O      O|\n|O      O|\n ________ "],
	]
	"""x and y to be referneced for while loop menus at bottom"""
	x=True
	y= True
	history =[]

	def questions():
		#DEFINE ROLLING FUNTION TO BE REFERENCED LATER
		def rolling():
			roll_num = 1
			count = 0
			for num in range(int(rolls)):
				rollct = []
				print("\nRoll number: " ,roll_num)
				history.append(["Roll number: " ,roll_num])
				roll_num = roll_num + 1

				for num in range(1,3):
					dice_Num = random.randint(0,5)
					print(_DICE[dice_Num][1])
					count = count + int(_DICE[dice_Num][0])
					rollct.append(int(_DICE[dice_Num][0]))

					"""keep track of history to print if user requests"""

					'''keep track of previous 2 rolls to verify "snakeeyes" or "boxcar" '''
					if(len(rollct) == 2):
						history.append(rollct)
						if(rollct[0] == 6 and rollct[1] == 6):
							print("\n\t>>>BOX CAR!")
							history.append("BOXCAR")
						elif(rollct[0] == 1 and rollct[1] == 1):
							print("\n\t>>>SNAKE EYES!")
							history.append("SNAKEEYES")

			print("\nTotal: ", count)
			history.append(["CALCULATED TOTAL: " , count])
		#START OF QUESTIONS FUNCTION
		print("\n" + format)
		rolls = input("How many dice rolls would you like to do?\n\nHINT: Each roll contains 2 dice \n- You may choose a whole number between 1 and 9 rolls \n->")
		try:
			if(int(rolls) <=9 and int(rolls) >= 1):
				return rolling()
		except ValueError as rolls:
			"""errors catched are decimals and string values"""
			print("\n>>Invalid character(s) selection detected:\n")
			return questions()
		else:
			"""numbers over 9 or below 1 are caught here"""
			print("\n>>Not a valid input\n")
			questions()
		

	questions()
	
	"""while loop menu, text file and play agian options"""
	while(x):
		text_file = input("\n>>>>Print a history report to a text file? Y/N\n")

		if(str(text_file).lower() == "y"):
			"""text file writing operations"""
			f= open("answers.txt","w+")
			f.write(str(history))
			f.close()
			x=False
		elif(str(text_file).lower() == "n"):
			x=False
		else:
			print("\nInvalid Response\n")

	while (y):
		play_agian = input("\n>>>>Play agian Y/N?\n")

		if(str(play_agian).lower() == "y"):
			main()
		elif(str(play_agian).lower() == "n"):
			exit()
		else:
			print("\nInvalid Response\n")

main()
