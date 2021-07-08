# get random names of the people in the list using For loop, Maxmium participant variable and input() function
# and then get your lottery run 
maxTicketsAvalibale = 5
participants = [ "Balakrishna", "Jagadeesh Sai", "Krishna", "Chari",  "Hari "  ]
import random
n = random.randint(0,maxTicketsAvalibale-1)
participants[n]

#Lottery running
maxTicketsAvalibale = int(input("Enter the maximum tickets avaiable "))

participants = [] 

for temp in range(maxTicketsAvalibale):
  
  name = input("Ënter the participant name - "+ str(temp + 1) + " - " )
  participants.append(name)

print("All our participants - ",participants)

n = random.randint(0,maxTicketsAvalibale-1)

print("Winner of the lottery - ",participants[n])
