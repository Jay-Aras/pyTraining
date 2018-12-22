# Assignment - Day 1
##################################################################

from math import pow
import math

while True:
	print("\nAssignments Day 1\n")
	print("1. String concatenation")
	print("2. Sum of two numbers")
	print("3. Max of two numbers")
	print("4. sqrt of a number using math - import math")
	print("5. sqrt of a number using math - from math import")
	print("6. Quit\n")

	opt = input("Please input your option : ")

	if (opt < 1 or opt > 6):
		opt = input("Please input valid option : ")

	if (opt == 6):
		break

	if (opt == 1):
		while True:
			name = raw_input("Your good name?  ")
			lastName = raw_input("your last name please.. ")
			if (name == "" or lastName == ""):
				print("Please enter a valid name")
			else:
				break
		fullName = name + " " + lastName
		print("\nHello! " + fullName)

	if (opt == 2):
		while True:
			num1 = raw_input("Enter number 1 : ")
			num2 = raw_input("Enter number 2 : ")
			try:
				int(num1)
				int(num2)
			except ValueError:
				print("Invalid input\n")
				continue
			result = int(num1) + int(num2)
			print("\nsum of "+num1+" and "+num2+" is "+str(result))
			break

	if (opt == 3):
		while True:
                        num1 = raw_input("Enter number 1 : ")
                        num2 = raw_input("Enter number 2 : ")
                        try:
                                int(num1)
                                int(num2)
                        except ValueError:
                                print("Invalid input\n")
                                continue
			if (int(num1) == int(num2)):
				print("The numbers are equal\n")
			elif (int(num1) > int(num2)):
				print(num1+" is larger than "+num2)
			else:
				print(num2+" is larger than "+num1)
			break

	if(opt == 4):
		while True:
			x = raw_input("Power of two integers (x^y) - Enter value of x : ")
			y = raw_input("Enter value of y : ")
			try:
				int(x)
				int(y)
			except ValueError:
				print("Invalid input\n")
				continue
			print(x+" ^ "+y+" is "+str(pow(int(x), int(y))))
			break

	if(opt == 5):
		while True:
			x = raw_input("Power of two integers (x^y) - Enter value of x : ")
			y = raw_input("Enter value of y : ")
			try:
				int(x)
				int(y)
			except ValueError:
 				print("Invalid input\n")
				continue
			print(x+" ^ "+y+" is "+str(math.pow(int(x), int(y))))
			break
