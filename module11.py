import random

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

def generate_random_numbers(n):
    # Generate `n` random numbers between 1 and 100 (inclusive)
    numbers = []
    for i in range(n):
        number = random.randint(1, 100)  # ✅ FIXED: upper bound changed from 101 to 100
        numbers.append(number)
    return numbers

def filter_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]  # ✅ FIXED: only include even numbers

def main():
    # Generate 10 random numbers and calculate the average.
    numbers = generate_random_numbers(10)
    print("Generated numbers:", numbers)

    # Calculate average of numbers.
    average = calculate_average(numbers)
    print("Average of numbers:", average)

    # Filter even numbers from the list.
    even_numbers = filter_even_numbers(numbers)
    print("Even numbers:", even_numbers)

if __name__ == "__main__":
    main()
