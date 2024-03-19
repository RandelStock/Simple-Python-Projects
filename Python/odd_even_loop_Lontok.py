#initialize list and variables
int_list = []
odd_count = 0
even_count = 0
num_sum = 0

#ask user for input 
for _ in range(10):
    user_input = eval(input("Enter a number:"))
    int_list.append(user_input) #append user input to list
    if user_input % 2 == 0: #check for even numbers
        even_count += 1
    else: 
        odd_count += 1
    num_sum += user_input #add the number to the sum

#print the results 
print("The list contains: ", int_list)
print("Number of odd numbers: ", odd_count)
print("Number of even numbers: ", even_count)
print("The sum of all the numbers in the list is: ", num_sum)