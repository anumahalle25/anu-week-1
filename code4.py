# 4. Write a program to take a student's marks as input and calculate the total, percentage, and grade based on the following criteria: A for 90+, B for 80–89, C for 70–79, D for 60–69, and F below 60.

#maths, physics, chemistry
maths = int(input( "90" ))
physics = int(input( "85" ))
chemistry = int(input( "70" ))

total = ((maths + physics + chemistry)/300)*100
percentage = ( total/300 )*100

if percentage >= 90:
    print("A")
elif  percentage >= 85:
percentage >= 85:
    print("B")
elif percentage >= 70:
    print("C")
else:
    print("Fail")