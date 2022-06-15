
#The world map Bitmap


"""Bitmap Message, by BELAMIR Zakarya kakaa2993@gmail.com
Displays a text message according to the provided bitmap image."""


import sys



bitmap = """


....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 *              *************    **   **  *
                  *                ***********      *  ** ***
                   *******          ********          * *** ****
                   *********         ******  *        **** ** * **
                    ********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ***                *                 *******   *
                    **                                        *    *
                     *     *                    *
....................................................................

"""

# We will put the input into a list named ListInput then append to the list 1000 words of
# the input to use it for replace the stars "*" in the bitmap with one letter from the input. 


def main():
	print('Bitmap Message, by BELAMIRI Zakarya kakaa2993@gmail.com')
	print('Enter the message to display with the bitmap.')

	# take input from the user
	Message = input("> ")

	# Print the error message and ask again if the user want to play
	if Message =='':
		print("You should write something as a missage to display with the bitmap! " )
		#print("Do you want to try again?(yes/no) : ")
		#player_answer = input("> ")
		#if player_answer.lower() == "yes" or player_answer.lower() == "y":
		main()
		#else:
		#	sys.exit()
	#replace the stars with the inputs
	ListOfBitmap =  bitmap.split("/n")
	for line in ListOfBitmap:
		ListOfNewBitmap=[]
		for i, character in enumerate(line):
			if character==" " or character == "\n":
				ListOfNewBitmap.append(character)
			else:
				ListOfNewBitmap.append(Message[ i % len(Message)])
	print("".join(ListOfNewBitmap))
	print("Do you want to try again?(yes/no) : ")
		player_answer = input("> ").lower()
		if player_answer == "yes" or player_answer == "y":
			main()
		else:
			sys.exit()
if __name__== '__main__':
	main()
	
