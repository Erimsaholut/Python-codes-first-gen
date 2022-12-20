from time import sleep
letters= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','W','V','X','Y','Z','.',',','?','!'," "]
word = "Hello World !"
letter = ""
for j in word:    # H
    for i in letters:
        sleep(0.05)
        print(letter+i)
        if j==i:
            letter += i
            break
        
        
    