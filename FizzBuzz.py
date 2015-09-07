# Python code for the FizzBuzz test

# Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print “Fizz” instead of the number 
# and for the multiples of five print “Buzz”. 
# For numbers which are multiples of both three and five print “FizzBuzz”."

for i in range(1, 101):
    multiple = 0
    printString = ""
    if i % 3 == 0:
        printString = "Fizz"
        multiple = 1
    if i % 5 == 0:
        printString += "Buzz"
        multiple = 1
    if multiple == 0:
        print i
    else:
        print printString
