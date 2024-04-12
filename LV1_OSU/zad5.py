#Zadatak 1.4.5 Napišite Python skriptu koja ce ucitati tekstualnu datoteku naziva ˇ SMSSpamCollection.txt
#[1]. Ova datoteka sadrži 5574 SMS poruka pri cemu su neke oznacene kao ˇ spam, a neke kao ham.
#Primjer dijela datoteke:
#ham Yup next stop.
#ham Ok lar... Joking wif u oni...
#spam Did you hear about the new "Divorce Barbie"? It comes with all of Ken’s stuff!
#12 Poglavlje 1. Uvod u programski jezik Python
#a) Izracunajte koliki je prosje ˇ can broj rijeci u SMS porukama koje su tipa ham, a koliko je ˇ
#prosjecan broj rijeci u porukama koje su tipa spam. ˇ
#b) Koliko SMS poruka koje su tipa spam završava usklicnikom ?

list = []

file = open("SMSSpamCollection.txt")
for line in file:
    words = line.split()
    list.append(words)

ham_counter=0
spam_counter=0
spam_exclamation=0
ham_len=0
spam_len=0

for element in list:
    if element[0]=="ham":
        ham_counter+=1
        ham_len+=len(element[0])
    if element[0]=="spam":
        spam_counter+=1
        spam_len+=len(element[0])
        if element[-1]=="!":
            spam_exclamation+=1

print("a) Ham word average: ",ham_len/ham_counter ,"Spam word average: ",spam_len/spam_counter)

print("b) Spam ending with exclamation mark: ",spam_exclamation)

file.close
