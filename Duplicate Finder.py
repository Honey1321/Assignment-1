numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
seen = set()
duplicates = set()
for number in numbers:
    if number in seen:
        duplicates.add(number)
    else:
        seen.add(number)
print("Original list:", numbers)
print("Unique numbers:", seen)
print("Duplicates:", duplicates)
