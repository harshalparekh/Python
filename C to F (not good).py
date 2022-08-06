def farh(cel):
    return (cel *(9/5)) + 32

c = input("Enter temperature in celcius: ")
f = farh(c)
print("Fahreheit Temperature is " + str(f))
