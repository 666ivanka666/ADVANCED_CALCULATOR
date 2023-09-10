import math


def get_numbers():
    try:
        num_count = int(input("Enter the number of numbers: "))
        numbers = []
        for _ in range(num_count):
            number = float(input("Enter a number: "))
            numbers.append(number)
        print(numbers)
        return numbers
    except:
        print("Please enter valid values.")

# 1 MNOZENJE
def action_multiply():
    numbers = get_numbers()
    result = 1
    for num in numbers:
        result *= num
    print(f"The multiplication result is: {result}")
    return result

# 2 ODUZIMANJE
def action_subtract():
    numbers = get_numbers()
    if len(numbers) < 2:
        print("Please enter at least two numbers.")
        return 
    result = numbers[0] - sum(numbers[1:])
    print(f"The subtraction result is: {result}")
    return result

# 3 ZBRAJANJE
def action_add():
    numbers = get_numbers()
    result = sum(numbers)
    print(f"The addition result is: {result}")
    return result

# 4 DJELJENJE
def action_divide():
    num1, num2 = get_numbers()
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        result = num1 / num2
        print(f"The division result is: {result}")
        return result

# 5 SINUS
def action_sine():
    angle = float(input("Enter the angle in degrees: "))
    if angle < 0 or angle > 360:
        print("Invalid angle. Please enter a value between 0 and 360.")
    else:
        result = math.sin(math.radians(angle))
        print(f"The sine of {angle} degrees is: {result}")
        return result

# 6 COSINUS
def action_cosine():
    angle = float(input("Enter the angle in degrees: "))
    result = math.cos(math.radians(angle))
    print(f"The cosine of {angle} degrees is: {result}")
    return result

# 7 TANGENT
def action_tangent():
    angle = float(input("Enter the angle in degrees: "))
    result = math.tan(math.radians(angle))
    print(f"The tangent of {angle} degrees is: {result}")
    return result

# 8 NA KVADRAT 2
def action_square():
    num = float(input("Enter a number: "))
    result = num ** 2
    print(f"The square of {num} is: {result}")
    return result

# 9 KORJEN IZ 2
def action_square_root():
    num = float(input("Enter a number: "))
    if num < 0:
        print("Cannot calculate square root of a negative number.")
    else:
        result = math.sqrt(num)
        print(f"The square root of {num} is: {result}")
        return result

## 10 N-KORJEN
def action_root():
    num = float(input("Enter a number: "))
    root = float(input("Enter the desired root: "))
    result = num ** (1 / root)
    print(f"The {root}th root of {num} is: {result}")
    return result

## 11 BROJ NA N-TU
def action_exponent():
    base = float(input("Enter the base number: "))
    exponent = float(input("Enter the exponent: "))
    result = base ** exponent
    print(f"The result of {base} raised to the power of {exponent} is: {result}")
    return result


## 12 LOGARITAM
def action_logarithm():
    base = float(input("Enter the base number: "))
    num = float(input("Enter the number: "))
    if base <= 0 or base == 1 or num <= 0:
        print("Invalid input. Please enter valid numbers.")
    else:
        result = math.log(num, base)
        print(f"The logarithm of {num} with base {base} is: {result}")
        return result
    

