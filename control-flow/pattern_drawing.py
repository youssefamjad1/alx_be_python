# pattern_drawing.py
# Draw a square pattern of asterisks (*) using nested loops.

size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:
    for _ in range(size):
        print("*", end="")
    print()  # Newline after each row
    row += 1
