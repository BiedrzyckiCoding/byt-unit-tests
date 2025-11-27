class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        if self.operation == "+":
            return self.a + self.b

        elif self.operation == "-":
            return self.a - self.b

        elif self.operation == "*":
            return self.a * self.b

        elif self.operation == "/":
            if self.b == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return self.a / self.b

        else:
            raise ValueError(f"Invalid operation: {self.operation}")
