n = int(input("Enter a positive integer: "))

even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("Sum of all even numbers from 1 to", n, ":", even_sum)
print("Sum of all odd numbers from 1 to", n, ":", odd_sum)