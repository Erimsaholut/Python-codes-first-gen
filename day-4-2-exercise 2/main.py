# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random 

a = len(names) 
b = random.randint(0,a-1) 
c = names[b]
print(f"hesabı {c} ödesin.")








