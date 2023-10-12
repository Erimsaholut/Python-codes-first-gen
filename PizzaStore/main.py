# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
hesaps = 0
kov = 0
if size == "S":
    hesaps += 15
    if add_pepperoni == "Y":
        hesaps += 2
        if extra_cheese == "Y":
            hesaps += 1
    else:
        if extra_cheese == "Y":
            hesaps += 1
elif size == "M":
    hesaps += 20
    if add_pepperoni == "Y":
        hesaps += 3
        if extra_cheese == "Y":
            hesaps += 1
    else:
        if extra_cheese == "Y":
            hesaps += 1
elif size == "L":
    hesaps += 25
    if add_pepperoni == "Y":
        hesaps += 3
        if extra_cheese == "Y":
            hesaps += 1
    else:
        if extra_cheese == "Y":
            hesaps += 1
else:
    kov += 1

if kov == 0:
    print(f"Hesabınız {hesaps}TL tuttu.\n   Yine bekleriz.")

