import random

maxTicketsAvalibale = int(input("Enter the maximum tickets avaiable "))

participants = [] 

for temp in range(maxTicketsAvalibale): 
  name = input("Enter the participant name - "+ str(temp + 1) + " - ")
  participants.append(name)

print("All our participants - ",participants)

n = random.randint(0,maxTicketsAvalibale-1)

print("The Winner of the lottery is - ",participants[n])
