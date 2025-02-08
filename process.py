import sys
import random

# Retrieve command-line arguments
if len(sys.argv) != 3:
    print("Error: Please provide a number and a text message.")
    sys.exit(1)

number = int(sys.argv[1])
text = sys.argv[2]

# Task 1: Number Puzzle
if number % 2 == 0:
    number_result = f"The number {number} is even. Square root: {number ** 0.5:.2f}"
else:
    number_result = f"The number {number} is odd. Cube: {number ** 3}"

# Task 2: Text Puzzle
binary_text = ' '.join(format(ord(c), '08b') for c in text)
vowel_count = sum(1 for c in text.lower() if c in "aeiou")

text_result = f"Binary: {binary_text}\nVowel Count: {vowel_count}"

# Task 3: Treasure Hunt
target = random.randint(1, 100)
attempts = 0
found = False
guess_log = []

while attempts < 5:
    guess = random.randint(1, 100)  # Simulated guess
    attempts += 1
    if guess == target:
        guess_log.append(f"Attempt {attempts}: {guess} (Correct!)")
        found = True
        break
    elif guess > target:
        guess_log.append(f"Attempt {attempts}: {guess} (Too high!)")
    else:
        guess_log.append(f"Attempt {attempts}: {guess} (Too low!)")

treasure_result = "\n".join(guess_log)
if found:
    treasure_result += f"\nYou found the treasure in {attempts} attempts!"
else:
    treasure_result += "\nYou did not find the treasure."

# Print results for PHP to display
print(number_result)
print(text_result)
print(treasure_result)
