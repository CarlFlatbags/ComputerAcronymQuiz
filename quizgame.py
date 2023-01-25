#!/bin/python3

print("Welcome to my Computer Quiz")

playing = input("Do you want to play? ")


if playing.upper() != "YES":
	quit()

print("Okay! Lets play :) ")

score = 0



answer = input("What does CPU stand for? ")

if answer.upper() == "CENTRAL PROCESSING UNIT":
	print("Correct!")
	score += 1
else:
	print("Sorry, that is incorrect...")

answer = input("What does GPU stand for? ")

if answer.upper() == "GRAPHICS PROCESSING UNIT":
	print("Correct!")
	score +=1
else:
	print("Sorry, that is incorrect...")

answer = input("What does RAM stand for? ")

if answer.upper() == "RANDOM ACCESS MEMORY":
	print("Correct!")
	score += 1
else:
	print("Sorry, that is incorrect...")

answer = input("What does NAS stand for? ")

if answer.upper() == "NETWORK ATTACHED STORAGE":
	print("Correct!")
	score += 1
else:
	print("Sorry, that is incorrect...")

print("You got " + str(score) + " questions correct!")

print("You got " + str((score / 4) * 100) + "%!")








