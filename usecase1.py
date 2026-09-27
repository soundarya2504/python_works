usecase1: Check room availability
    - If available:
        - If guest is VIP
            → Offer complimentary upgrade
        - Else if member 5+ years
            → Offer discount
        - Else
            → Standard price
    - Else:
        → Show: "No rooms available"


Room_available=input("Is the room available (yes/No)")
if Room_available == "yes":
    guest=input("Is the guest is vip (yes/no)")
    if guest == "yes":
        print("offer compilementary upgrage")
    else:
        member_years=int(input("how many years have you been a member:"))
        if member_years >= 5:
            print("offer discount")
        else:
            print("standard price")
else:
    print("No rooms available")




