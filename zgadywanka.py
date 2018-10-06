import random
liczba = random.randint(1,10)
for i in range(6):
        print("Podejscie: ", i+1)
        
        odp = int(input("podaj liczbe : "))
        
       
        if liczba == odp:
                print("Brawo, prawidlowa liczba to : ",odp)
                break
        elif liczba > odp:
				print("Za malo")
        elif liczba < odp: 
                print("Za duzo")
        else:
				print("You lose")

        
				

        
