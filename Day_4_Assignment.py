#You all are pilots, you have to land a plane, the altitude required for landing a plane is 1000ft,
#if it is less than that tell pilot to land the plane,or 
#it is more than but less than 5000ft ask the pilot to "come down to 1000ft"
#,else if it is more than 5000ft ask the pilot to "go around and try later".
#Example:Input-1000
#        Output:Safe to land
#        Input-4500
#        Output-bring down to 1000
#        Input -6500
#        Ouput-turn arounds

print("Welcome to Airway\n")

print("Hello pilot,please give the flight details.")
curht=int(input("What is the current height of the flight in air:"))
height=1000
print("Since,the Present height of the flight is "+str(curht)+".Pilot,we request you to")
if(curht<=height):
    print("Safe to land.")
elif (curht>height and curht<5000):
     print("Bring down to 1000ft.") 
else:
    print("Turn around and try later.")

print("Thank you...")
