num1=int(input("Enter first number:"))
num2=int(input("Enter secound number"))

print("\nSelect operation:")
print("1. Addition (+)")
print("2. Substraction (-)")
print("2. multiplication (*)")
print("4. Division (/)")

#user choice

choice =input("Enter choice (1/2/3/4:")
if choice =='1':
    result=num1+num2
    print(f"\nResult: {num1}+{num2}={result}")
    
elif choice=='2':
    result=num1 -num2
    print(f"\nResult:{num1}/{num2}={result}")
    
elif choice =='3':
    result=num1*num2
    print(f"\nResult:{num1}*{num2}={result}")
    
elif choice =='4':
    if num2 !=0:
        result=num1/num2
        print(f"\nResult:{num1}/{num2}={result}")
    else:
        print("\nEroor: Division by zero is not allowed.")
else:
    
     print("\nInvalid input! Please choose a valid operation (1/2/3/4).")
    