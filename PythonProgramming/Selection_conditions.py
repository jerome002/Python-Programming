grade = int(input("Enter your grade: "))
# Check the grade and print the corresponding letter grade
if (grade < 0 or grade > 100):
    print ("Invalid grade")
else:
    print("Your letter grade is: ", end="")
if (grade >= 90):
	print("A")
elif(grade >=80 and grade <90):
	print ("B")
elif(grade >=70 and grade <80):
	print ("C")
elif(grade >=60 and grade <70):
	print ("D") 
else:
	print ("F")