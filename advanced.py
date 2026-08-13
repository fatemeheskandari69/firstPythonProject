import math


def power(base, exponent):
    return base ** exponent


def square_root(value):
    if value < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(value)


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(int(n))


def absolute(value):
    return abs(value)


def main():
    print("Advanced Calculator")
    print("Operations: power (^), sqrt, factorial (!), abs")
    print()

    op = input("Enter operation (^, sqrt, !, abs): ").strip().lower()

    try:
        if op == "^":
            base = float(input("Enter base: "))
            exponent = float(input("Enter exponent: "))
            result = power(base, exponent)
        elif op == "sqrt":
            value = float(input("Enter value: "))
            result = square_root(value)
        elif op == "!":
            n = float(input("Enter a non-negative integer: "))
            result = factorial(n)
        elif op == "abs":
            value = float(input("Enter value: "))
            result = absolute(value)
        else:
            print("Invalid operation.")
            return
    except ValueError as exc:
        print(f"Error: {exc}")
        return

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
