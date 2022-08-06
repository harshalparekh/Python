from ast import If
from socket import if_nameindex


a = input("Enter Quiz(1) Marks: ")
b = input("Enter Mid-Term(2) Marks: ")
c = input("Enter Final(3) Marks: ")

a = float (a)
b = float (b)
c = float (c)

total = a + b + c
percentage = (total / 300) * 100

if (percentage > 90):
    print(f"Congretlations! You got A grade. With {percentage} %")
elif(percentage >=70 < 90):
    print(f"Congretlations! You got B grade. With {percentage} %")
elif(percentage>=50 <70):
    print(f"Congretlations! You got C grade. With {percentage} %")
else:
    print(f"Sorry to say, you got F grade With {percentage} %. Study well next time.")
