# ZADANIE 2 Sito Eratostenesa
# Program pozostawia liczby pierwsze z wpisanego zakresu
import math
 
zakres = int(input("Podaj górny zakres liczb do których będzie liczyć program: "))
lista = []

for i in range(2, zakres+1):
  lista.append(i) #tworzy listę liczb z podanego zakresu, zaczynając od 2

for n in lista:
    p = 2
    while p < math.sqrt(zakres):
        for i in range (p, zakres+1):
            if p*i in lista: #usuwa wielokrotności liczb pierwszych
                lista.remove(p*i)
        p += 1
    
print("Liczby pierwsze z podanego zakresu to: ", lista) #wypisuje listę z pozostawieniem tylko liczb pierwszych

input("Aby zakończyć naciśnij Enter")
