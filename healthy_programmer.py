"""
Healthy Programmer need time to time exercise and enough amount of water to maintain their health. 
So hee is the program which will reminds the programmer to 1.Drink water after some amount of time lets say after 45 minutes
2. Do eyes exercise affter every 50 minutes
3. Do exercise after 55 minutes
"""
from pygame import mixer
from datetime import datetime
from time import time

def music_player(file,stopper):
	mixer.init()
	mixer.music.load(file)
	mixer.music.play
	
	while True:
		user_input = input("Enter the particular input as says to stop the music ")
		if user_input == stopper:
			mixer.music.stop
			break

def waterlog(msg):
	with open ("water_log.txt","a") as f:
		f.write(f"{msg} {datetime.now()} \n")

def eyelog(msg):
	with open("eye_ex_log.txt","a") as f:
		f.write(f"{msg}{datetime.now()} \n")

def exlog(msg):
	with open("ex_log.txt","a") as f:
		f.write(f"{msg}{datetime.now()} \n")

if __name__== '__main__':
	drink_water_after= 5
	eye_ex_after=10
	ex_after= 20
	done_water= time()
	done_ey_ex= time()
	done_ex= time()
	
	while True:
		if time() - done_water > drink_water_after:
			print("It is time to drink water. \n after drinking the water please Enter 'drank'")
			music_player('water.mp3','drank')
			done_water=time()
			waterlog("Drink water at :")

		if time() - done_ey_ex > eye_ex_after:
			print("It is time to do eye exercise. \n after exercising please Enter 'done'")
			music_player('eye.mp3','done')
			done_ey_ex =time()
			eyelog("Done eyes exercise at :")

		if time() - done_ex > ex_after:
			print("It is time to do exercise. \n after exercising please Enter 'completed'")
			music_player('exercise.mp3','completed')
			done_ex=time()
			exlog("Done eyes exercise at :")