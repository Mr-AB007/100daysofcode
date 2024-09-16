from art import logo
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

operations = {"+":add,"-":sub,"*":mul,"/":div}

while True:
    print(logo)
    fnumber = float(input("Enter First Number: "))
    con = "y"
    while con == "y":
        snumber = float(input("Enter next Number: "))
        operation = input("Enter the Operation(+ , - , * , / : ")
        result = operations[operation](fnumber,snumber)
        print(f"{fnumber} {operation} {snumber} : {result} ")
        con = input("continue working with the previous result? y/n : ")
        if con == "y":
            fnumber = result
        else:
            print("\n"*20)




