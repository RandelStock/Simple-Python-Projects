number = int(input("enter a number: "))

summation = 0

for i in range(1, number+1):
    summation += i

print("the summation of", number, "is", summation)