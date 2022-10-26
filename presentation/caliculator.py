number1= int(input("First number : "))
number2=int(input("Second number : "))
op=input("write operator : ")
answer=0
if op=="+":
    answer=f"{number1} {op} {number2} = {number1+number2}"
elif op=="-":
    answer=f"{number1} {op} {number2} = {number1-number2}"
elif op=="x"  or op=="X":
    answer=f"{number1} {op} {number2} = {number1*number2}" 
elif op=="/":
    answer=f"{number1} {op} {number2} = {number1/number2}"
elif op=="%":
    answer=f"{number1} {op} {number2} = {number1%number2}"
else:
    print("InputError: Invalid operator")
    






print(answer)
