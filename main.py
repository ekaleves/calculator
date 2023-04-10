from replit import clear
import art
print(art.logo)


def calculator():
    result = 0
    cont_calc = False
    first_number = float(input("What's the first number? "))
    operator = input("+\n-\n*\n/\nPick an operator: ")
    second_number = float(input("What's the next number? "))

    def add(number1, number2):
        return number1 + number2
    def subtract(number1, number2):
        return number1 - number2
    def multiple(number1, number2):
        return number1 * number2
    def division(number1, number2):
        return number1 / number2
    

    if operator == "+":
        result = add(first_number, second_number)
    elif operator == "-":
        result = subtract(first_number, second_number)
    elif operator == "*":
        result = multiple(first_number, second_number)
    elif operator == "/":
        result = division(first_number, second_number)
    else:
        print("Wrong operator, you have to type + for adding, - for subtract, * for multiple or / for division.")

    text = input(f"{first_number} {operator} {second_number} = {result}. Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if text == "y":
        cont_calc = True
    elif text == "n":
        cont_calc = False
        clear()
        print(art.logo)
        calculator()

    if cont_calc == True:
    
        while cont_calc == True:
            first_answer = result
            operator1 = input("+\n-\n*\n/\nPick an operator: ")
            next_number = int(input("What's the next number? "))
            if operator1 == "+":
                result += next_number
            elif operator1 == "-":
                result -= next_number
            elif operator1 == "*":
                result *= next_number
            elif operator1 == "/":
                result /= next_number
            else:
                print("Wrong operator, you have to type + for adding, - for subtract, * for multiple or / for division.")
            
            text = input(f"{first_answer} {operator1} {next_number} = {result}. Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
            if text == "y":
                cont_calc = True
            elif text == "n":
                cont_calc = False
                clear()
                print(art.logo)
                calculator()
calculator()       