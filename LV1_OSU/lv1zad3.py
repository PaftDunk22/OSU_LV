#Zadatak 1.4.3 Napišite program koji od korisnika zahtijeva unos brojeva u beskonacnoj petlji ˇ
#sve dok korisnik ne upiše „Done“ (bez navodnika). Pri tome brojeve spremajte u listu. Nakon toga
#potrebno je ispisati koliko brojeva je korisnik unio, njihovu srednju, minimalnu i maksimalnu
#vrijednost. Sortirajte listu i ispišite je na ekran. Dodatno: osigurajte program od pogrešnog unosa
#(npr. slovo umjesto brojke) na nacin da program zanemari taj unos i ispiše odgovaraju ˇ cu poruku.

list = []
while(True):
    print("input a number or 'Done' ")
    number = input()
    if number.isnumeric():
        x=float(number)
        list.append(x)
    if(number == "Done"):
        break

list.sort()
print(list)

min = list[0]
max = list[-1]

list_sum=sum(list)
el=len(list)

print("Ammount of elements:",el)
print("Sum of the elements:",list_sum)

print("Min:",min ,"Max:",max)