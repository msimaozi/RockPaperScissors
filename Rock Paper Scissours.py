import random

Lose = "Computer wins"
Win = "You Win"
lives = 3
score = 0
pc_lives = 3
while True:
	username = input("Enter your username: ")
	while True:
		rps = input("Rock, Paper, Scissors?\n")
		computer_rps = ("Rock", "Paper", "Scissors")
		computer_rps = random.choice(computer_rps)
		if rps == "Rock" and computer_rps == "Paper":
			print("The computer choose: ",computer_rps)
			print("\n\n --",Lose,"-- \n\n")
			lives -= 1
		if rps == "Paper" and computer_rps == "Scissors":
			print("The computer choose: ",computer_rps)
			print("\n\n --",Lose,"-- \n\n")
			lives -= 1
		if rps == "Scissors" and computer_rps == "Rock":
			print("The computer choose: ",computer_rps)
			print("\n\n --",Lose,"-- \n\n")
			lives -= 1     
		if rps == "Rock" and computer_rps == "Scissors":
			print("The computer choose: ",computer_rps)
			print("\n\n --",Win,"-- \n\n")
			score += 1
			pc_lives -= 1
		if rps == "Paper" and computer_rps == "Rock":
			print("The computer choose: ",computer_rps)
			print("\n\n --",Win,"-- \n\n")
			score += 1
			pc_lives -= 1
		if rps == "Scissors" and computer_rps == "Paper":
			print("The computer choose: ",computer_rps)
			print("\n\n --",Win,"-- \n\n")
			score += 1
			pc_lives -= 1
		if rps == computer_rps:
			print("The computer choose: ",computer_rps)
			print("\n\n --Draw-- \n\n")

		if rps == "rules":
			print("rules: ")
		if rps == "lives":
			print("Your lives", lives)
			print("Computer lives", pc_lives)

		if lives == 0:
			print("-------------------------------------\n")
			print("You have lost all your lives\n Thanks for playing \n You got ",score," right\n")
		if pc_lives == 0:
			print("-------------------------------------\n")
			print("Congrats, ",username,"you have won\n Thanks for playing \n You got ",score," right\n")