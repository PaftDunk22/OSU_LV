#Zadatak 1.4.1 Napišite program koji od korisnika zahtijeva unos radnih sati te koliko je placen ´
#po radnom satu. Koristite ugradenu Python metodu ¯ input(). Nakon toga izracunajte koliko ˇ
#je korisnik zaradio i ispišite na ekran. Na kraju prepravite rješenje na nacin da ukupni iznos ˇ
#izracunavate u zasebnoj funkciji naziva ˇ total_euro.
#Primjer:
#Radni sati: 35 h
#eura/h: 8.5
#Ukupno: 297.5 eura

print("Enter work hours:")
work_hrs = float(input())

print("Enter payment per hour:")
payment_hrs = float(input())

print("You have earned:",work_hrs*payment_hrs)

def total_euro(work_hrs,payment_hrs):
    final_payment=work_hrs*payment_hrs
    print("You have earned(function):",final_payment)

total_euro(work_hrs,payment_hrs)
