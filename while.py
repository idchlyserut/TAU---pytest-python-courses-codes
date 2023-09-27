    
"""
##loop controls##
Break - end the loop. go to the next statement in the program (outside the loop)
Continue - skips current part of the loop. moves to the next part of the loop
Pass - skips any part of the loop where "pass" appears. best used for testing code
"""

temp_f = 40

while temp_f > 32:
    print("The water is {} degrees".format(temp_f))
    temp_f -=1
    if temp_f==33:
        break

for number in range (1,11):
    if number == 7:
        print("We're skipping number 7.") #this is like a condition to get a specific car
        continue #like a policeman that says "ok we got the condition, u guys may pass"
    print("This is the number {}.".format(number)) #other cars are  able to continue to pass 




