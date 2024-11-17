numbers = []
print("Enter 5 numbers: ")
for i in range(5):
  num = float(input(f"Enter number {i+1}: "))
  numbers.append(num)

average = sum(numbers) / len(numbers)
print(f"The average of 5 numbers is: {average}")
