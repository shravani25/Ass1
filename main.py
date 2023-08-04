
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes


prime_numbers = find_primes(50)

print(prime_numbers)

def table(num):
    for i in range(1,11):
        print(num,"*",i,"=",num*i)

table(2)

def is_palindrome(s):
    return s == s[::-1]

str = input("Enter a string: ")

if is_palindrome(str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


str = input("Enter a string: ")
reverse = str[::-1]
print("Reversed string:", reverse)