Age=int(input("Age"))
Monthly_income=int(input("Monthly income:"))
if Age<18:
    print("Not eligible for a bank account")
elif Age>=18 and Monthly_income<15000:
    print("eligible for basic savings account")
elif Age>=18 and Monthly_income >=15000 and Monthly_income<=50000:
    print("eligible for savings + salary account")
elif Age>=18 and Monthly_income>50000:
    print("eligible for preimum account")