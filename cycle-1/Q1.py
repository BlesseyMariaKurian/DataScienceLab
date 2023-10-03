def is_prime(num):
  if num <=1:
      return False
  for i in range (2,num):
      if num % i ==0:
          return False
      return True
print("SJC22MCA-2023-BLESSEY MARIA KURIAN\nS3MCA")
start=int(input("enter the starting number:"))
end=int(input("enter the end number:"))
print("non-prime numbers between {start} and {end} is:")
for num in range(start,end+1):
 if not is_prime(num):
   print(num,end=" ")
