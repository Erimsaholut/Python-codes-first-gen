
b = 0
c = int(input("Boyun Kaç "))
if c >= 120:
  a = int(input("yaşın kaç "))
  if a >= 18:
    b = 12
  elif a <= 12:
    b = 5
  else:
    b = 7
  k= input("Suriyeli misin E ya da H ?") 
  if k == "E":
    b += 5
else:
  print("git")
print(b)

        