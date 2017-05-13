def fizzBuzz():
	limit = input("Enter a number:")
	for i in range(1,int(limit)):
		outString = str(i)
		if i % 3 == 0:
			outString = outString + " Fizz"
		if i % 5 == 0:
			outString = outString + " Buzz"
		print(outString)