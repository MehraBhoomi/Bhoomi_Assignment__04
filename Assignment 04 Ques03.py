# Write a Python program to square the elements of a list using map() function.

# Sample List: [4, 5, 2, 9]

# Square the elements of the list:

# [16, 25, 4, 81]

sample_list = [4,5,2,9]
square_list = list(map(lambda x:x**2 , sample_list))
print("The sample list is ",sample_list)
print("The updated list is ",square_list)