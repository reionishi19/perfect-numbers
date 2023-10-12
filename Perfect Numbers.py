"""
Rei Onishi
September 14, 2023

This program will identify deficient numbers, perfect numbers, and abundant numbers.
"""

#PD: proper divisor
#deficient_numbers sum of PD < number
#perfect_numbers: sum of PD == number
#abundant_numbers: sum of PD> number
user_number = int(input("Enter an upper bound for a check:"))

deficient_count = 0
perfect_count = 0
abundant_count = 0

for number in range(1, user_number + 1):
    pd_sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            pd_sum += divisor

    if pd_sum < number:
        deficient_count += 1
    elif pd_sum == number:
        perfect_count += 1
    else:
        abundant_count += 1

print(f"{deficient_count} deficient numbers")
print(f"{perfect_count} perfect numbers")
print(f"{abundant_count} abundant numbers")
