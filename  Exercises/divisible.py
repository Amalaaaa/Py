#Divisibility of number
num = int(input("Enter a number: "))

divisible_by_2 = num % 2 == 0
divisible_by_3 = num % 3 == 0
divisible_by_5 = num % 5 == 0

print(f"The number {num} is divisible by:")
if divisible_by_2:
    print("2")
if divisible_by_3:
    print("3")
if divisible_by_5:
    print("5")

else:
    print("None of the above")

