n = float(input("ENter a Number:"))

guess = n/2
while (guess != (guess + n / guess) / 2):
    guess = (guess + n / guess) / 2
    print(f"Guess:{guess}")
print(f"Square Root:{guess}")