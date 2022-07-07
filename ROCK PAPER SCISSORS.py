##Got bored and rewrote the rock paper scissors game
from random import randint
player_win = 0
computer_wins = 0
winning_counts = 5

while player_wins + computer_wins < winning_counts:
	print(f"PLayer score: {player_wins}, \n computer score: {computer_wins}" )
	print ("...rock...")
	print ("....paper....")
	print ("...scissors...")

	choice = input("enter player 1's choice").lower()
	if choice == "quit" or choice == "q":
		break
	rand_num = randint(0,2)
	if rand_num == 0:
		computer =  "paper"
	elif rand_num == 1:
		computer = "rock"
	else: 
		computer = "scissors"
	print (f"Computer plays {computer}")

	if choice and computer:
			if (choice == "paper" and computer == "scissors") or (choice == "scissors" and computer == "rock") or  (choice == "rock" and computer == "paper"):
				print ("COMPUTER wins")
				computer_wins += 1
			elif (computer == "paper" and choice == "scissors") or (computer == "scissors" and choice == "rock") or  (computer == "rock" and choice == "paper"):
				print ("PLAYER 1 wins")
				player_wins += 1
			elif (computer == "paper" and choice == "paper") or (computer == "scissors" and choice == "scissors") or  (computer == "rock" and choice == "rock"):
				print ("DRAW")
			else:
				print("enter a correct term or CHECK THAT TERM IS IN LOWER CASE")
	else:
		print ("please enter a valid option")
if player_wins > computer_wins:
	print ("CONGRATS YOU WON!!")
elif player_wins == computer_wins:
	print("IT'S A TIE")
else:
	print("COMPUTER WINS")
print(f"FINAL SCORES: \n PLayer score: {player_wins}, \n computer score: {computer_wins}")















#paper > rock 2. rock > scissors 3. scissors > paper

# choice = input("enter player 1's choice")
# print ("\n" * 10)
# choice1 = input ("enter player 2's choice")

# if choice and choice1:
# 		if (choice == "paper" and choice1 == "scissors") or (choice == "scissors" and choice1 == "rock") or  (choice == "rock" and choice1 == "paper"):
# 			print ("PLAYER 2 wins")
# 		elif (choice1 == "paper" and choice == "scissors") or (choice1 == "scissors" and choice == "rock") or  (choice1 == "rock" and choice == "paper"):
# 			print ("PLAYER 1 wins")
# 		elif (choice1 == "paper" and choice == "paper") or (choice1 == "scissors" and choice == "scissors") or  (choice1 == "rock" and choice == "rock"):
# 			print ("DRAW")
# 		else:
# 			print("enter a correct term or CHECK THAT TERM IS IN LOWER CASE")
# else:
# 	print ("please enter a valid option")


