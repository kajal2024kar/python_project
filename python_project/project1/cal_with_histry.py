class CalculatorWithHistory:
    def __init__(self):
        self.history = []  # Stack to store history

    def calculate(self, expression):
        try:
            result = eval(expression)
            self.history.append((expression, result))
            return result
        except Exception as e:
            return f"Error: {e}"

    def show_history(self):
        if not self.history:
            print("No history yet.")
        else:
            print("Calculation History:")
            for idx, (expr, res) in enumerate(reversed(self.history), 1):
                print(f"{idx}: {expr} = {res}")

    def undo(self):
        if self.history:
            removed = self.history.pop()
            print(f"Removed: {removed[0]} = {removed[1]}")
        else:
            print("No history to undo.")

if __name__ == "__main__":
    calc = CalculatorWithHistory()
    while True:
        print("\nOptions: [1] Calculate  [2] Show History  [3] Undo  [4] Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            expr = input("Enter expression (e.g., 2+3*4): ")
            result = calc.calculate(expr)
            print("Result:", result)
        elif choice == "2":
            calc.show_history()
        elif choice == "3":
            calc.undo()
        elif choice == "4":
            print("Exiting calculator.")
            break
        else:
            print("Invalid option. Try again.")