print("SJC22MCA-2019-BLESSEY MARIA KURIAN-S3MCA")
def is_armstrong_number(num):
    num_str=str(num)
    num_digits=len(num_str)
    digit_sum=sum(int(digit) ** num_digits for digit in num_str)
    return num == digit_sum
print("Armstrong Numbers upto 1000:")
for i in range(1,1000):
    if is_armstrong_number(i):
     print(i,end=" ")