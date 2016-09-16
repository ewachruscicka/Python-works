# ZADANIE 2 Liczby Armstronga
# Program znajduje jak najwięcej liczb,
# które są sumą swoich cyfr podniesionych do potęgi.
 
zakres = int(input("Podaj górny zakres liczb do których będzie liczyć program: "))

for i in range(10, zakres):
    dlugosc = len(str(i))
    potega = int(dlugosc)     #określ potęgę
    suma_cyfr = 0             
    liczba = i
    while liczba > 0:         #wyodrębnij cyfrę
      cyfra = liczba % 10     
      suma_cyfr += pow(cyfra, potega) # podnieś do potęgi i dodaj do sumy
      liczba //= 10

    if i == suma_cyfr:      #jeśli warunek jest spełniony (jest to liczba Armstronga)
      print (i)             #wypisz tą liczbę
      
input("Aby zakończyć naciśnij Enter")
