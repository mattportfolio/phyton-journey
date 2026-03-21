#Mateusz Drozdz, made on Phyton Online IDE.

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: We dont divide by zero lad!"
    return a / b
    
# Get their numbers

n1 = int(input("Enter 1st number:  "))
n2 = int(input("Enter 2nd number:  "))

# What to do with them

print("\nChoose an operation")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")
choice = input("(1/2/3/4):  ")

if choice == '1':
    print(f"Result: {n1} + {n2} = {add(n1, n2)}")
if choice == '2':
    print(f"Result: {n1} - {n2} = {subtract(n1, n2)}")
elif choice == '3':
    print(f"Result: {n1} * {n2} = {multiply(n1, n2)}")
if choice == '4':
    print(f"Result: {n1} / {n2} = {divide(n1, n2)}")
    
