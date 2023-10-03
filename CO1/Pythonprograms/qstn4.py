import math

def calculate_sin_taylor(x, n):
    result = 0.0

    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        result += term

    return result

# Input values
x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms (n): "))

# Calculate sin(x) using Taylor series expansion
sin_x_approximation = calculate_sin_taylor(x, n)

# Compare with the actual sin(x) value
sin_x_actual = math.sin(x)

print(f"Approximated sin({x}) using {n} terms: {sin_x_approximation}")
print(f"Actual sin({x}): {sin_x_actual}")
