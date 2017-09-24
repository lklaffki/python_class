#this program prints a random numnber
#import random 
#number = random.randint (1,25)
#print ("The random number is ", number)

#this is the "random number guess game"
#guessing 1-100, feedback, 5 trials, times needed to guess
import random
number = random.randint (1,10)

print ("Please guess a number between 1 and 100. You have 5 trials in total.")

for i in range(0,5,1):
	x=float(input("Guess the number: "))
	x=round(x)

	#Ausgabe der Versuche
	myTrials=5
	while myTrials<=5:
		if myTrials==1:
			print ("Game over!")
			break
		else:
			myTrials=myTrials-1
			continue
	
	# Counter stimmt nicht, "game over" wird jedes Mal ausgegeben; 
	#nach 5 Versuchen erfolgt aber korrekt Abbruch

	if x < number:
		print ("Guess a bigger number!") 
			#You have ", myTrials, trials left. Try again!")
		
	if x > number:
		print ("Guess a smaller number!") 
			#You have ", myTrials, trials left. Try again!")

	if x == number:
	# kann es hier if heißen oder muss es ein else geben?
		print ("Congratulations!") 
		#You have needed", myTrials, "trials to succeed.")
		break	