
import random
for i in range(10):
	lis=["stone","paper","sessior"]
	comp = random.choice(lis)

	print(comp)
	u_count=0
	c_count=0
	print("now its",i+1,"turn")
	user_ip=input("Please enter any of this \n stone,paper,sessior It's your turn:") 
	if (comp == "stone"):
		if (user_ip=="paper"):
			print("user wins")
			u_count=u_count+1
		elif(user_ip=="sessior"):
			print("computer wins")
			c_count=c_count+1
		elif(user_ip=="stone"):
			print("It's Tie")

	elif(comp == "paper"):
		if (user_ip=="paper"):
			print("It's Tie")
		elif(user_ip=="sessior"):
			print("user wins")
			u_count=u_count+1
		elif(user_ip=="stone"):
			print("computer winss")
			c_count=c_count+1

	elif(comp == "sessior"):
		if (user_ip=="paper"):
			print("Computer wins")
			c_count=c_count+1
		elif(user_ip=="sessior"):
			print("It's Tie")
		elif(user_ip=="stone"):
			u_count=u_count+1
			print("User wins")
	
if(u_count > c_count):
	print("You won")
else:
	print("Computer won")
