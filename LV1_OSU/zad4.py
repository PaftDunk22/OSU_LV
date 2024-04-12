#Zadatak 1.4.4 Napišite Python skriptu koja ce ucitati tekstualnu datoteku naziva ˇ song.txt.
#Potrebno je napraviti rjecnik koji kao kljuceve koristi sve razlicite rijeci koje se pojavljuju u ˇ
#datoteci, dok su vrijednosti jednake broju puta koliko se svaka rijec (kljuc) pojavljuje u datoteci. ˇ
#Koliko je rijeci koje se pojavljuju samo jednom u datoteci? Ispišite ih.

list = []

file = open("song.txt")
for line in file:
    words = line.split()
    for word in words:
        list.append(word)

dict = {}

for element in list:
    if element not in dict:
        dict[element]=0
    dict[element] += 1

print("Dictionary: ",dict)

Once= []

for element in dict:
    if dict[element]==1:
        Once.append(element)

print("Shows up once:",Once)


file.close
