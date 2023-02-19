# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
yar = name1+name2
isim_son = yar.lower()
ask = isim_son.count('t')+isim_son.count('r')+isim_son.count('u') + isim_son.count('e')
kask = isim_son.count('l')+isim_son.count('o')+isim_son.count('v')+isim_son.count('e')
mask = str(ask)+str(kask)
a = int(mask)
if a >= 90 or a <= 10:
  print(f"Your score is {a}, you go together like coke and mentos.")
elif a > 40 and a < 50:
  print(f"Your score is {a} you are alright together.")
else:
  print(f"ask skorunuz {a}")



