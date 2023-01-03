import random

x = random.randrange(1, 101)

text = """Hej och välkommen till detta spel.
Här skall du lista ut vilket nummer jag tänker på.
Låt oss börja! 
Du kan börja med att tala om vad du heter."""



print(text)
name = input("Sååå... vad är ditt namn:")
funny = "Jasså, så ditt namn är {}prutt välkommen till mitt spel {}prutt! "
print(funny.format(name,name))
userNumber = 0

while userNumber == 0:
    try:
        userNumber = int(input("Vilket nummer gissar du på (1-100)?"))
        if userNumber < 1 or userNumber > 100:
            userNumber = 0
            print("Oj oj, lite svåra instruktioner för dig... låt mig förtydliga... NUMRET JAG TÄNKER PÅ ÄR MELLAN 1 och 100!")
    except:
        print("Oj då din amatör,det där var inte riktigt ett nummer va!")
        print("Försök igen ärthjärna!")
        userNumber = 0
    



    


while userNumber != x:
    if userNumber < x:
        print("Det nummer jag tänker på är högre än", userNumber)
        userNumber = 0
        
        while userNumber == 0:
            try:
                userNumber = int(input("Försök igen... Gissa högre HÖgre HÖGRE!"))
                if userNumber < 1 or userNumber > 100:
                    userNumber = 0
                    print("Oj oj, lite svåra instruktioner för dig... låt mig förtydliga... NUMRET JAG TÄNKER PÅ ÄR MELLAN 1 och 100!")
            except:
                print("Oj då din amatör,det där var inte riktigt ett nummer va!")
                print("Försök igen ärthjärna!")
                userNumber = 0

        
    elif userNumber > x:
        print("Det nummer jag tänker på är lägre än", userNumber)
        userNumber = 0
        while userNumber == 0:
            try:
                userNumber = int(input("Försök igen... testa ett lägre nummer!"))
                if userNumber < 1 or userNumber > 100:
                        userNumber = 0
                        print("Oj oj, lite svåra instruktioner för dig... låt mig förtydliga... NUMRET JAG TÄNKER PÅ ÄR MELLAN 1 och 100!")
            except:
                print("Oj då din amatör,det där var inte riktigt ett nummer va!")
                print("Försök igen ärthjärna!")
                userNumber = 0
            
        

print("Grattis din lilla tönt du har hittat det rätta numret som var", userNumber, "skaffa dig nu ett liv!")