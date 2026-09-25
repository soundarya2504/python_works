Conditional Structure
Use Case 0: Banking Eligibility Check
Write a program that asks the user for:
Age
Monthly income

Conditions:
If age < 18: print "Not eligible for a bank account."
If age >= 18 and income < 15000: print "Eligible for basic savings account."
If age >= 18 and income between 15000 and 50000: print "Eligible for savings + salary account."
If age >= 18 and income > 50000: print "Eligible for premium account."

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
