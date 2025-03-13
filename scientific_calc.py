import math

def calculator():
    print("Scientific Calculator")
    print("Type 'exit' to quit")
    while True:
        expr = input("Enter expression: ")
        if expr.lower() == 'exit':
            print("Exiting")
            break
        try:
            result = eval(expr, {"__builtins__": None, "math": math})
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator()
