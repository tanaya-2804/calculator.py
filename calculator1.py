def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

def calculator():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        # ... other operations
        print("q. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == 'q':
            break
            
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"Result: {add(num1, num2)}")
          
        except ValueError:
            print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    calculator()
