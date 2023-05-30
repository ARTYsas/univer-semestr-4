def find_missing_digits(n):
    all_digits = set('0123456789')
    digits_in_number = set(str(n))
    missing_digits = sorted(all_digits - digits_in_number, reverse=True)
    return missing_digits

# Get input from the user
n = int(input("Enter a natural number: "))

# Find and print the missing digits
print("Missing digits:", ', '.join(find_missing_digits(n)))
