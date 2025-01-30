import CalFunc

a=int(input("Enter number1:"))

b=int(input("Enter number2:"))

c=input("Enter the operation to be perform(add/sub/mul/div/mod/sqr):")

if c == "add":
       print(CalFunc.add(a,b))

elif c == "sub":
       print(CalFunc.sub(a,b))

elif c == "mul":
       print(CalFunc.mul(a,b))   

elif c == "div":
       print(CalFunc.div(a,b))    
       
elif c == "mod":
       print(CalFunc.mod(a,b))    

elif c == "sqr":
       print(CalFunc.sqr(a,b))     

else:
       print("Please enter the valid operation-(add/sub/mul/div/mod/sqr)")               
