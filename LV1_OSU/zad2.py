#Zadatak 1.4.2 Napišite program koji od korisnika zahtijeva upis jednog broja koji predstavlja
#nekakvu ocjenu i nalazi se izmedu 0.0 i 1.0. Ispišite kojoj kategoriji pripada ocjena na temelju ¯
#sljedecih uvjeta:
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#Ako korisnik nije utipkao broj, ispišite na ekran poruku o grešci (koristite try i except naredbe).
#Takoder, ako je broj izvan intervala [0.0 i 1.0] potrebno je ispisati odgovaraju ¯ cu poruku.

print("Input a grade(range from 0 to 1)")

try:
    grade = float(input())

    if(grade < 0 or grade > 1):
        print("Number out of range")
    elif(grade >= 0.9 and grade <= 1):
        print("your grade: A")
    elif(grade >= 0.8):
        print("your grade: B")
    elif(grade >= 0.7):
        print("your grade: C")
    elif(grade >= 0.6):
        print("your grade: D")
    elif(grade < 0.6):
        print("your grade: F")

except:
    print("You did not input a number")

