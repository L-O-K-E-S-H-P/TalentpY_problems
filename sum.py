''' Create a function to compute sum of digits. Call this sum of digits function 
to find the sum of digits of numbers ranges from 1001 to 22000'''


def sum_of_digits(num):
    num=str(num)
    sum=0
    for digit in num:
        sum=sum+int(digit)
    print(num,' ',sum)
print('N SUM')
for num in range(1001,22001):
    sum_of_digits(num)
