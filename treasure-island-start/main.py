print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Hazine Adasına Hoş Geldiniz.")
print("Göreviniz Hazineyi Bulmak.")
print("Not:Oyun büyük küçük harfe duyarlıdır. Yanlış seçim yapmamak için dikkatli yazınız.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("Yıllardır yaptığınız araştırmalardan sonra hazine adasının yerini buldunuz. Uçakla adaya vardıktan sonra karşınıza bir yol ayrımı çıktı")
bir = input("Sağdan mı gideceksiniz soldan mı ? (seçenekler: sağ , sol)\n")
if bir == "sağ" :
  print('''Sağa adımızı atar atmaz son hızla gelen bir araba sizi eziyor\n
               .---------------.
              /       oLo       \
            O/_____/________/____\O
            /__________+__________\
           /    (#############)    \
           |[**](#############)[**]|
           \_______________________/
            |_""__|_,-----,_|__""_|
            | |     '-----'     | |  
            '-'                 '-'\n OYUN BİTTİ''')
               
  



else:
  print("Deniz kıyısına ulaştınız.")
  iki = input("Karşıya geçmek için yüzecek misiniz bir tekne mi bekleyeceksiniz.(seçenekler: yüz , bekle )\n")
  if iki == "bekle":
    uc = input("""5 dakika sonra teknesi olan bir yerli sizi cüzzi bir ücret karşılığında karşıya geçiriyor \n Biraz ilerledikten sonra karanlık bir mağaraya geliyorsunuz \n ********************************************************************************
*                    /   \              /'\       _                              *
*\_..           /'.,/     \_         .,'   \     / \_                            *
*    \         /            \      _/       \_  /    \     _                     *
*     \__,.   /              \    /           \/.,   _|  _/ \                    *
*          \_/                \  /',.,''\      \_ \_/  \/    \                   *
*                           _  \/   /    ',../',.\    _/      \                  *
*             /           _/m\  \  /    |         \  /.,/'\   _\                 *
*           _/           /MMmm\  \_     |          \/      \_/  \                *
*          /      \     |MMMMmm|   \__   \          \_       \   \_              *
*                  \   /MMMMMMm|      \   \           \       \    \             *
*                   \  |MMMMMMmm\      \___            \_      \_   \            *
*                    \|MMMMMMMMmm|____.'  /\_            \       \   \_          *
*                    /'.,___________...,,'   \            \   \        \         *
*                   /       \          |      \    |__     \   \_       \        *
*                 _/        |           \      \_     \     \    \       \_      *
*                /                               \     \     \_   \        \     *
*                                                 \     \      \   \__      \    *
*                                                  \     \_     \     \      \   *
*                                                   |      \     \     \      \  *
*                                                    \ms          |            \ *
 ******************************************************************************** \n
 karşınızda 3 adet kapı var hangisinden gideceksiniz.(seçenekler: a , b , c )\n """)
    if uc == "a":
      print("""A kapısından geçip biraz ilerledikten sonra nefes alma sesleri duyuyorsunuz. El fenerinizi sesin geldiği yöne tuttuğunuzda bir canavar üzerinize atlayıp sizi öldürüyor.\n 
                                              ,--,  ,.-.
                ,                   \,       '-,-`,'-.' | ._
               /|           \    ,   |\         }  )/  / `-,',
               [ '          |\  /|   | |        /  \|  |/`  ,`
               | |       ,.`  `,` `, | |  _,...(   (      _',
   -ART BY-    \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L\
    -ZEUS-      \  \_\,``,   ` , ,  /  |         )         _,/
                 \  '  `  ,_ _`_,-,<._.<        /         /
                  ', `>.,`  `  `   ,., |_      |         /
                    \/`  `,   `   ,`  | /__,.-`    _,   `\
                -,-..\  _  \  `  /  ,  / `._) _,-\`       \
                 \_,,.) /\    ` /  / ) (-,, ``    ,        |
                ,` )  | \_\       '-`  |  `(               \
               /  /```(   , --, ,' \   |`<`    ,            |
              /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
        ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
       (-, \           ) \ ('_.-._)/ /,`    /
       | /  `          `/ \\ V   V, /`     /
    ,--\(        ,     <_/`\\     ||      /
   (   ,``-     \/|         \-A.A-`|     /
  ,>,_ )_,..(    )\          -,,_-`  _--`
 (_ \|`   _,/_  /  \_            ,--`
  \( `   <.,../`     `-.._   _,-`
   `                      ```\n OYUN BİTTİ
 """)
    if uc == "b":
      print(""""B kapısından ilerlerken ayağınız takılıyor ve yükseklikten düşüyorsunuz.\n
                                      +---+
                                      |\   \
  +-----------------------------+     | +---+
   \                      +-----------+ |   |
    \                      \            |   |
     \                 |/   +-----------+   |
      \                (c_      |   \ | |   |
       \                \       |    \| |   |
        \                       |     | |   |
         \                      |     + |   |
          \                     |      \| DM|
           \--------------------+       +---+
            \                    \        \
             \                    \        \
              +-----------------------------+\n OYUN BİTTİ""")
    if uc == "c":
      print("""" C kapısını geçip ilerlerken önünüze büyük ve eski bir sandık çıkıyor.\n   __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|\n Sandığı açtığınızda içinden 'Gerçek hazine çıktığın bu macerada esnasında öğrendiklerin ve hayallerinin peşinden gitmenin veridiği mutluluk' yazıyor.""")
      print("""

               _..._
             ,'     `.
           ,'         `.
         ,'    _   ,-.  `.
         |    (_)  `-'   |
         |        >      |
         |     ,----.    |
         |    /,-""-.\   |
         `.  |/      "  ,'
           `.         ,'
             `._____,'\n OYUN BİTTİ TEBRİKLER """)

  if iki == "yüz":
    print("""Yüzerken bir köpek balığı kafanızı ısırdı.\n 

                     ^`.                     o
     ^_              \  \                  o  o
     \ \             {   \                 o
     {  \           /     `~~~--__
     {   \___----~~'              `~~-_     ______          _____
      \                         /// a  `~._(_||___)________/___
      / /~~~~-, ,__.    ,      ///  __,,,,)      o  ______/    \
      \/      \/    `~~~;   ,---~~-_`~= \ \------o-'            \
                       /   /            / /
                      '._.'           _/_/
                                      ';|\n OYUN BİTTİ""")
    

  