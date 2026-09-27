temp=float(input("Enter body temperature in celsius:"))
if temp < 37:
    print("Normal temperature")
elif temp > 37 and temp < 39:
    print("Fever")
else:
    print("High fever") 