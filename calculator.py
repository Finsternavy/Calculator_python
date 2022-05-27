# Calculator.py
# Extreme calculator
# Christopher Finster

def add(num1, num2):
    result = num1 + num2
    return result

def subtract(num1, num2):
    result = num1 - num2
    return result

def multiply(num1, num2):
    result = num1 * num2
    return result

def divide(num1, num2):
    if num2 != 0:
        result = num1 / num2
        return result
    print("Sorry! Can't divide by zero!")

# function to print the header each time
def menu():
    print("="*100)
    print("Extreme Calculator\nby Chris")
    print("="*100)
    print("[1] Sum\n[2] Subtract\n[3] Multiply\n[4] Divide\n[5] Exit")

# Make sure the user is entering a number
def enterValidNum():
    num = (input("Enter a number: "))
    try: 
        val = int(num)
        print("Input is an integer. Number = ", num)
        return val
    except ValueError:
        try: 
            val = float(num)
            print("Input is a float. Number = ", num)
            return val  
        except ValueError:
            print("Input was a string = ", num) 
            calculate()

def calculate():
    menu()
    option = (input("Enter the number of the operation you wish to perform: "))
    print(f"[{option}]")

    result = 0

    if option == '1':
        print("SUM")
        num1 = enterValidNum()
        num2 = enterValidNum()
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
        
    elif option == '2':
        print("SUBTRACT")
        num1 = enterValidNum()
        num2 = enterValidNum()
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")

    elif option == '3':
        print("MULTIPLY")
        num1 = enterValidNum()
        num2 = enterValidNum()
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")

    elif option == '4':
        print("DIVIDE")
        num1 = enterValidNum()
        num2 = enterValidNum()
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")

    elif option == '5':
        print("Exiting now...\n\n\n")
        exit()

    else:
        print("Invalid entry.  Try again!\n\n\n")
        calculate()

    again = input("New calculation? Type 'yes' or anything else to exit:")

    if again.upper() == 'YES':
        print("\n\n\n")
        calculate()

    else:
        print("Exiting now...\n\n\n")
        exit()
    
    
calculate()