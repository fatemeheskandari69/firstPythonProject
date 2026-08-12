def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def modulo(a, b):
    return a % b


def main():
    print("Simple Calculator")
    print("Operations: +  -  *  %")
    print()

    op = input("Enter operation (+, -, *, %): ")
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number.")
        return

    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = subtract(a, b)
    elif op == "*":
        result = multiply(a, b)
    elif op == "%":
        if b == 0:
            print("Error: modulo by zero.")
            return
        result = modulo(a, b)
    else:
        print("Invalid operation.")
        return

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
