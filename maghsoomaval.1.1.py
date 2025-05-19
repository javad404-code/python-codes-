def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_divisors_count(n):
    count = 0
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            count += 1
    return count

numbers = []
for _ in range(10):
    numbers.append(int(input()))

max_count = -1
result_number = -1

for num in numbers:
    count = prime_divisors_count(num)
    if count > max_count or (count == max_count and num > result_number):
        max_count = count
        result_number = num

print(result_number,max_count)



        