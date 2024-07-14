name=input("What is your name?:")
age=input("What is your age (NUMBERS ONLY)?:")
age=int(age)
if age<10:
    print("E")
elif age>=10 and age<13:
    print("E10+")
elif age>=13 and age<16:
    print("T")
elif age>=16 and age<18:
    print("M")
else:
    print("AO")
print(name+" the number stated above is your game rating.")
print("Thank you for using this program and enjoy!")