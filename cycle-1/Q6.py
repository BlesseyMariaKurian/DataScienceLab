print("SJC22MCA-2019-BLESSEY MARIA KURIAN-S3MCA")
def is_perfect_number(num):
    if num<=0:
        return False
    sum = 0
    for i in range(1,num):
      if num%i==0:
        sum += i
    print("sum of factors:",sum)
    return sum == num
num = int(input("Enter a number:"))
if is_perfect_number(num):
    print(f"{num} is a perfect number")
else:
  print(f"{num}is not a perfect number")