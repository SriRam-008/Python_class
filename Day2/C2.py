def is_str(x):
    if type(x) == str:
        return True
    return False

x = input("Enter the element:")

if is_str(x) and x.isalpha():
    print(ord(x[0])) 
else:
    print("Not a String")
