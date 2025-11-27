from calculator import Calculator

def main():
    print("Demo of the Calculator class:\n")

    examples = [
        (10, 5, "+"),
        (10, 5, "-"),
        (10, 5, "*"),
        (10, 5, "/")
    ]

    for a, b, op in examples:
        calc = Calculator(a, b, op)
        result = calc.calculate()
        print(f"{a} {op} {b} = {result}")

    # Example with error handling
    try:
        calc = Calculator(10, 0, "/")
        calc.calculate()
    except ZeroDivisionError as e:
        print("\nCaught error:", e)


if __name__ == "__main__":
    main()
