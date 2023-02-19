#Write your code below this line 👇
def prime_checker(number):
    sınır = number
    prime_number = True
    while not sınır == 2:
        böl = number % (sınır-1)
        sınır -= 1
        if böl == 0:
            print(f"{number} is not prime number.")
            sınır = 2
            prime_number = False
    if not prime_number == False:
        print(f"{number} is prime number")    
        
    
        
    
    
    





#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



