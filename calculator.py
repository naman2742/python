#Program to calculate 

#INPUT

first = input("enter first number : ");
operator = input("enter (+,-,/,*,%) : ");
second = input("enter second number :");

first = float(first);
second = float(second);

#PROCESS AND OUTPUT

if operator == "+":
    print(first + second);
elif operator == "-":
    print(first - second);
elif operator == "/":
    print(first / second);
elif operator == "*":
    print(first * second);
elif operator == "%":
    print(first % second);
else :
    print("INVALID OPERATOR");