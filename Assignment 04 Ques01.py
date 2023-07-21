# Question no. 1 Write a Python program to create a lambda function that adds 25 to a
                # given number passed in as an argument.

# sample input: 10
# sample output: 35


# Solution: 

a = int(input("Enter a number :\n"))
add_25 = lambda x:x+25
print(f"The value after adding 25 to the given number {a} is {add_25(a)}")