rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random 
hareket = [rock,paper,scissors]
#bizim haraketler
a = int(input("Taş Kağıt Makas Oyununa Hoş Gelmişsen\nTaş için 1, Kağıt için 2, Makas için 3 yaz\n"))
if a>3 or a<1:
  print("Adam gibi yaz yavşak")

print("Sen:")
print(hareket[a-1])
print("Bilgisayar:")
#çavoooooo
pc = random.randint(1,3)
print(hareket[pc-1])
if a == 1:
  if pc == 1:
    print("Berabere")
  if pc == 2:
    print("Kaybettin :(")
  if pc == 3:
    print("Kazandın!")
    
if a == 2:
  if pc == 1:
    print("Kazandın!")
  if pc == 2:
    print("berabere")
  if pc == 3:
    print("Kaybettin :(")
if a == 3:
  if pc == 1:
    print("Kaybettin :( ")
  if pc == 2:
    print("Kazandın!")
  if pc == 3:
    print("Berabere")
