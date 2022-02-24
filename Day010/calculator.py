import art



def add(n1,n2):
    return n1+n2
def substract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2    

operations = {
    "+" :  add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
}
def calculator():
    print(art.logo)
    num1 =  float(input("enter the first number: "))
    for key in operations:
        print(key)
    isTrue = True
    while isTrue:
        operation_symbol = input("select from the above operations, Enter the symbol: ")
        num2 =  float(input("enter the second number: "))
        function = operations[operation_symbol]
        answer = function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"type 'y' to continue calculation with {answer} or 'n' to start new calculation: ") == 'y':
            num1 = answer
        else:
            isTrue = False
            calculator()
calculator()