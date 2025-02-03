def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 #Handle if all numbers are not int or float
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

# Example usage with a potential error
my_numbers = [1, 2, 3, 0]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = [1,2, 'a']
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = ['a', 'b', 'c']
average = calculate_average(my_numbers)
print(f"The average is: {average}") 