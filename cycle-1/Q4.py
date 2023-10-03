print("SJC22MCA-2019-BLESSEY MARIA KURIAN\nS3MCA")
def are_coprime(a,b):
  while b:
     a,b = b,a % b
  return a == 1

# input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Check if they are coprime
if are_coprime(num1, num2):
 print(f"{num1} and {num2} are coprime.")
else:
 print(f"{num1} and {num2} are not coprime.")

