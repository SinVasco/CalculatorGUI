class CalculatorLogic:
    def __init__(self):
        self.current_expression = ""

    def append_expression(self, value):
        self.current_expression += str(value)

    def clear(self):
        self.current_expression = ""

    def calculate(self):
        try:
            # Evaluate the expression and return the result
            return str(eval(self.current_expression))
        except Exception as e:
            self.clear()
            return "Error"

    def get_current_expression(self):
        return self.current_expression
