def count_digits(n):
    return len(str(n))

def is_armstrong_recursive(n, num_digits):
    if n == 0:
        return 0
    return (n % 10) ** num_digits + is_armstrong_recursive(n // 10, num_digits)

def is_armstrong_number(n):
    num_digits = count_digits(n)
    return is_armstrong_recursive(n, num_digits) == n
number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
