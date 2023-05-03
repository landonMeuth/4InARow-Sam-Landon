#import
import os
import random
#vars
currentPlayer="Red"

humanisplaying=input("are you playing? ")

if humanisplaying in ["yes","y","yeaz!"]:
	humanisplaying=True
else:
	humanisplaying=False
	
iterationsOfOut=int(input("Output every so many numbers? "))

win=False

move=9

winnerData=[0,0,0]

weights=[[[87, 66, 55, -44, -32, -49, 22, 78, -21, 67, 50, -17, -63, -98, 37, 25, 47, -32, -18, 67, -47, 83, 58, 84, -68, -69, -45, -29, -4, -16, -64, 21, -23, -4, 85, -34, 41, -58, -40, 59, 35, 95], [-94, -62, 40, 1, -73, 28, 73, -76, -93, 94, 62, 94, -66, 49, 97, -52, 7, 57, -35, 63, 95, -6, 93, 51, 81, 31, 50, 49, 89, 39, 82, -23, -14, 73, 37, -85, 99, 92, 88, -23, -78, -30], [88, -78, -71, -43, 92, -6, -23, -92, -4, 61, 40, 66, -72, 56, 16, 34, -91, -3, -45, -37, -49, 83, 29, 9, 50, 65, -46, 85, 11, -66, -89, -65, -100, -9, 78, 35, 17, -4, 56, -86, 62, -50], [63, -64, -75, -30, 95, 93, 27, 72, -71, -46, 72, -81, -64, 25, -92, -46, -53, -95, -10, -85, 23, 27, -42, -65, -93, -38, -95, -86, -2, 93, -21, -9, -13, -5, 91, -89, 97, -68, 1, -44, 19, 50], [21, 36, -13, 14, -32, 85, 17, 0, 14, 36, -50, -8, -38, 40, 98, -100, 60, 33, 93, 62, -74, -86, 40, 1, 89, -83, -40, -77, -24, 75, 47, -35, 59, -61, 61, -95, -22, 98, -90, -20, -7, 85], [-64, -98, 78, 55, -16, -95, -94, 45, 83, -80, -5, 78, 52, 16, -14, -3, -16, 35, -69, -85, -100, -52, -56, -49, -83, -65, 16, -49, 84, -78, -68, -8, 97, -100, -69, -66, 31, -77, 82, 1, -57, 4], [-45, 12, 38, -29, -70, -61, 31, 85, 76, 53, -24, 53, -2, -61, 68, 34, -90, -69, -3, 17, 4, 32, -59, -60, -47, -98, 46, 35, -58, -74, -80, -16, -82, 78, -31, -71, 10, 89, -89, 98, -16, 87]], [[96, 74, -81, 13, -57, -66, 86], [7, 3, 97, 5, -33, -49, 96], [-6, 21, 69, 66, 77, -13, -68], [63, -49, 31, -2, -60, 63, 51], [-75, 56, -21, -13, 65, -81, -19], [86, -97, -58, -56, -43, -65, -25], [67, 12, 64, -83, 2, -33, -17]], [[-36, -93, -18, -100, -59, 36, 62], [46, -30, -29, -76, -78, 42, -29], [77, -39, 53, 18, -50, -32, 91], [84, -19, 86, 9, -17, -25, 49], [13, 23, -61, -69, 13, -81, -21], [-80, -61, -31, 96, -55, -42, 9], [-53, -92, 91, -60, 96, 33, -93]], [[-34, 18, -40, 72, -12, -80, 39], [-70, 29, -52, -47, -45, -36, 80], [-97, 77, 73, 42, 31, 79, 31], [-3, -13, 61, 78, 57, -34, 17], [-17, -54, -66, -33, -27, 11, -13], [61, 73, -64, -6, -30, -39, -48], [-99, 67, 53, 51, 67, -100, -39]]]
biases=[[-29, 18, 34, -30, 21, 31, 29], [59, -16, 3, -54, 12, 16, -97], [23, 25, -19, 21, 47, -71, -44], [-39, 25, -18, -9, 68, 61, 3]]
weights2=[[[33, 7, 46, 0, -60, -1, 10, 17, 54, 13, 73, 42, 2, 73, -8, 13, 44, 6, -78, 83, 70, 94, 45, -75, -86, -34, -91, -79, -12, -96, 11, 49, 31, 96, 80, -95, -10, 98, 11, 14, 63, -95], [-48, -39, 91, 72, 10, 34, -84, -72, 27, 89, -20, 16, 70, -24, -29, -47, 54, 87, 5, 10, 82, 54, 36, 93, -40, 55, 31, 91, -22, -37, 21, 41, 82, -12, -25, 75, 72, -29, -77, -37, 39, 95], [-57, -93, 64, 71, -49, -51, 48, 43, -99, 67, 31, -80, 94, 9, -96, 43, 90, 83, -50, -75, -79, -43, -58, -52, -71, 12, -55, -62, 12, -82, -21, -23, -51, 80, -62, 64, 25, 29, -69, -51, -53, 8], [54, -42, -16, -85, -54, 6, -76, 46, 73, -92, 13, 39, 15, -58, 90, -21, 99, 76, 79, -38, 82, 69, -39, -57, -68, -15, 33, -12, -78, -81, 44, -81, 17, -30, 3, 44, -3, 44, -96, -13, 47, -8], [71, -8, -16, 48, 88, -58, -21, -12, 32, -80, 17, 82, -47, 29, 88, 52, -60, 46, 85, -5, -15, 32, -42, -25, 33, -89, -66, -5, 44, 47, -18, 12, 16, -92, -56, 27, -40, 83, -10, -17, 5, 83], [-94, 14, -85, 82, -49, -61, -47, -94, -70, 64, 69, -76, 8, -94, 4, 51, 34, -75, 91, 18, 63, 69, -7, 89, -52, -34, 15, -52, 76, -11, 7, -46, -85, -73, -96, 15, 16, 35, -65, -73, 29, 49], [-4, 68, -49, 11, 19, -66, 36, 31, -5, 54, -85, 13, 33, -17, -28, 56, 37, -73, 68, 29, -53, 57, -63, 20, 38, -71, 75, 31, 29, 50, 29, 60, -83, -50, 4, 76, 56, 15, 18, 59, 15, -55]], [[-66, 11, -79, 63, 31, -64, 0], [-43, 87, 3, 65, -98, -1, 92], [-30, -26, -91, 17, 75, -32, 30], [42, 91, 0, 97, -87, 65, 13], [40, -55, -57, -84, 53, -55, -12], [17, -87, -27, 56, 72, 68, 97], [-76, 24, 26, -29, -17, -88, 80]], [[-50, 33, -45, 90, 2, 29, 67], [-19, 98, -68, -11, 74, -26, -50], [18, -36, 90, -42, 25, 61, 51], [40, 93, 8, -22, 21, 59, 20], [30, 60, 26, 42, 87, -17, 30], [79, 64, 65, 84, 41, 94, -98], [41, -25, -71, 91, 65, 83, -61]], [[-50, 59, -36, 27, 62, 43, 59], [34, 84, 97, 4, 90, 61, 16], [-57, -27, 13, -45, -13, -5, -33], [56, -84, 99, -86, 70, 12, -9], [39, 29, 65, 24, -42, 62, 46], [45, -5, 19, -79, 30, 94, -33], [-13, 62, 44, -45, -78, -38, 66]]]
biases2=[[-10, -8, 0, 4, 8, -5, 0], [-5, -10, 5, -2, 7, -9, 0], [-6, -5, -2, -1, 1, 7, 0], [-2, 6, 5, -8, -3, -7, 0]]



activations=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
activations2=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]


#- = blank
#x = red
#o = yellow

board=[["-","-","-","-","-","-","-"],
	   ["-","-","-","-","-","-","-"],
	   ["-","-","-","-","-","-","-"],
	   ["-","-","-","-","-","-","-"],
	   ["-","-","-","-","-","-","-"],
	   ["-","-","-","-","-","-","-"],]

#defs

########################################################################
def ai1(board,didIWin):
	


	#activation=sigmoid(weight*pastActivation added for every node +the bias)
	def runStep():
		global weights
		global biases
		global activations
		boardActivations=[]
		for row in range(len(board)):
			for column in range(len(board[row])):
				if board[row][column]=="-":
					boardActivations.append(0)
				if board[row][column]=="x":
					boardActivations.append(.5)
				if board[row][column]=="o":
					boardActivations.append(1)
		
		for node in range(7):
			x=0
			for weight in range(42):
				x=x+((weights[0][node][weight])*(boardActivations[weight]))
			activations[0][node]=x+biases[0][node]

		for layer in range(1,4):
			for node in range(7):
				x=0
				for weight in range(6):
					x=x+((weights[layer][node][weight])*(activations[layer-1][weight]))
				activations[layer][node]=x+biases[layer][node]

	def tweak(teakLevel):
		for i in range(100):
			layer=random.randrange(0,4)
			if layer==0:
				weights[layer][random.randrange(7)][random.randrange(42)]=random.randrange(-100,100)
			else:
				weights[layer][random.randrange(7)][random.randrange(7)]=random.randrange(-100,100)
			biases[random.randrange(4)][random.randrange(7)]=random.randrange(-100,100)

	
	if didIWin==1:
		pass
	elif didIWin==0:
		tweak(10)
	else:
		runStep()
		
	
	a=0
	for i in range(len(activations[3])):
		if int(activations[3][i])>a:
			a=activations[3][i]
	return(activations[3].index(a))

########################################################################

########################################################################
def ai2(board,didIWin):

	

	#board layer 
	


	#activation=sigmoid(weight*pastActivation added for every node +the bias)
	def runStep():
		global weights2
		global biases2
		global activations2
		boardActivations=[]
		for row in range(len(board)):
			for column in range(len(board[row])):
				if board[row][column]=="-":
					boardActivations.append(0)
				if board[row][column]=="x":
					boardActivations.append(.5)
				if board[row][column]=="o":
					boardActivations.append(1)
		
		for node in range(7):
			x=0
			for weight in range(42):
				x=x+((weights2[0][node][weight])*(boardActivations[weight]))
			activations2[0][node]=x+biases2[0][node]

		for layer in range(1,4):
			for node in range(7):
				x=0
				for weight in range(6):
					x=x+((weights2[layer][node][weight])*(activations2[layer-1][weight]))
				activations2[layer][node]=x+biases2[layer][node]

	def tweak(teakLevel):
		for i in range(100):
			layer=random.randrange(0,4)
			if layer==0:
				weights2[layer][random.randrange(7)][random.randrange(42)]=random.randrange(-100,100)
			else:
				weights2[layer][random.randrange(7)][random.randrange(7)]=random.randrange(-100,100)
			biases[random.randrange(4)][random.randrange(7)]=random.randrange(-100,100)

	
	if didIWin==1:
		pass
	elif didIWin==0:
		tweak(10)
	else:
		runStep()
	
	
	a=activations2[3][0]
	for i in range(len(activations2[3])):
		if int(activations2[3][i])>a:
			a=activations2[3][i]
	return(activations2[3].index(a))

########################################################################


def checkForWins():
	global win
	for word in ["xxxx","oooo"]: #pulls word to search for
		for row in range(len(board)): #imagin a pointer combing through every row and column of the word search.
			for column in range(len(board[row])):
				for scanDirection in [[1,0,"down"],[-1,0,"up"],[0,1,"right"],[0,-1,"left"],[1,1,"right down"],[-1,-1,"left up"],[1,-1,"left down"],[-1,1,"right up"]]: #the scan direction is the direction that the word is going
					checksum=0 #the checksum should equal the word length. if it does then the word was found.
					for i in range(len(word)):
						if (row+(i*scanDirection[0]))<0 or (row+(i*scanDirection[0]))>(len(board)-1) or (column+(i*scanDirection[1]))<0 or (column+(i*scanDirection[1]))>(len(board[row])-1): #makes sure the scanner doesn't go out of bounds
							pass
						elif word[i].lower()==board[row+(i*scanDirection[0])][column+(i*scanDirection[1])].lower():#each letter is thouroughly checked
							checksum+=1
					if checksum==len(word):
						win=True #makes a list of where the words are
	
	return(win)

def makeAMove():
	global win
	checksum=0
	global currentPlayer
	global checkForWins
	global winnerData
	gravity=5
	
	if currentPlayer=="red":
		currentPlayer="blue"
	else:
		currentPlayer="red"
	
	if currentPlayer=="red": 
		move=int(ai1(board,2))
	else:
		if humanisplaying==False:
			move=int(ai2(board,2))
		else:
			move=int(input())
	
	isitempty=0
	for row in range(len(board)):
		for column in range(len(board[row])):
			if board[row][column]=="-":
				isitempty=isitempty+1
	if isitempty==0:
		winnerData[2]+=1
		win=True
		return(0)
	else:
		while board[0][move-1] in ["x","o"]: #disallows putting peice in full column
			move=random.randint(0,6)
	
	while board[gravity][move-1] in ["x","o"]: #simulates gravity of peice
		gravity-=1
	
	if currentPlayer=="red": #swaps who the player is so they can make turns
		board[gravity][move-1]="x"
	else:
		board[gravity][move-1]="o"
	
#main operation
while True:
	repitition=int(input("how much to train "))
	doiend=0
	while doiend < repitition:
		#os.system('clear') #clears board
		#print("Welcome to 4 In A Row!\n\nType numbers 1 through 7 to drop a peice in their respective columns.\nTry to get 4 pieces to connect together to win.\n")
		if checkForWins()==False: 
			if humanisplaying==False:
				pass
			else:
				os.system('clear')
				print(board[0])
				print(board[1])
				print(board[2])
				print(board[3])
				print(board[4])
				print(board[5])
				
			makeAMove()
		else:
			if humanisplaying==False:
				pass
			else:
				os.system('clear')
				print(board[0])
				print(board[1])
				print(board[2])
				print(board[3])
				print(board[4])
				print(board[5])

			if (doiend%iterationsOfOut)==0:
				print(f"games:{doiend} red:{winnerData[0]} blue:{winnerData[1]} ties: {winnerData[2]}")

			if currentPlayer=="red":
				ai2(0,0)
				winnerData[0]+=1
			else:
				ai1(0,0)
				winnerData[1]+=1
				
			board=[["-","-","-","-","-","-","-"],
				["-","-","-","-","-","-","-"],
				["-","-","-","-","-","-","-"],
				["-","-","-","-","-","-","-"],
				["-","-","-","-","-","-","-"],
				["-","-","-","-","-","-","-"],]
			doiend=doiend+1
			win=False
	
	print(f"weights={weights}")
	print(f"biases={biases}")
	print(f"weights2={weights2}")
	print(f"biases2={biases2}")
	print(f"\n\nred won {winnerData[0]} times\nblue won {winnerData[1]} times\nthey tied {winnerData[2]} times")







