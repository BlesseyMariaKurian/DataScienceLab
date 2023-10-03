print("SJC22MCA-2019-BLESSEY MARIA KURIAN-S3MCA")
def sum_of_digits(n):

    digit_sum = 0
    while n > 0:
        digit_sum += n%10
        n //=10
    return digit_sum
num = int(input("Enter a positive number: "))

while num > 0:

    digit_sum = sum_of_digits(num)


    num -= digit_sum

    print(f"{num + digit_sum} - {digit_sum} = {num}")

print("The number is now positive or zero.")
