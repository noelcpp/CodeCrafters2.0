print("Hello World")
name: str = input("Enter yout name: ")
print(f"The name is {name}") 

number_1: int = float(input("enter a number 1: "))
number_2: int = float(input("enter the number 2: "))

if number_1==number_2:
    print("both are same")

elif number_1>number_2:
    print(f"{number_1} is greater than{number_2}") 
elif number_1<number_2:
    print(f"{number_1} is greater than{number_2}")     