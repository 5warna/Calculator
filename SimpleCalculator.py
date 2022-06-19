#Program to make a simple calculator with if else statements

#take inputs

n1 = float(input("Enter first number: "))

n2 = float(input("Enter second number: "))

#choice of operation

print("Operations: +, -, *, /")

choice = input("Select Operations: ")

#check operation and display result

if choice == '+':
    
    print(n1, '+', n2, '=', n1 + n2)

elif choice == '-':
    
    print(n1, '-', n2, '=', n1 - n2)

elif choice == '*':
    
    print(n1, '*', n2, '=', n1 * n2)

elif choice == '/':
    
    print(n1, '/', n2, '=', n1 / n2)

else:
    
    print("Invalid Input")
