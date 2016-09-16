# ZADANIE 3: Palindrom
# Program szuka liczb tak samo czytanych od przodu i od tylu

def jestPalindromem(liczba=15):
#sprawdza, czy podana liczba jest palindromem
  slowo = str(liczba)
  j = len(slowo)
  i = 1
  while i < j:
    if slowo[i-1] == slowo[j-1]:
      i = i + 1
      j = j - 1
    else:
      print("Liczba ", liczba, " nie jest palindromem")
      return False
      break  
  else:
    print("Liczba", liczba, " jest palindromem")
    return True

def dodajOdwrotnosc(liczba):
#do podanej liczby dodaje jej odwrotność i zwraca nową liczbę
  noweSlowo = ""
  slowo = str(liczba)
  noweSlowo = slowo[::-1]
  nowaLiczba = liczba + int(noweSlowo)
  print(slowo, "+", noweSlowo, " =", nowaLiczba)
  return nowaLiczba

for i in range(10,201):
  print("Sprawdzenie liczby ", i, ": ")
  if i == 196 or i == 200:
    print("PALINDROM NIEZNALEZIONY!!!!!!!!!") #wykonywałaby się pętla nieskończona
    i += 2
  while jestPalindromem(i) == False: #dopóki iczba z nie jest palindromem
    i = dodajOdwrotnosc(i)           #dodaj jej odwrotność i sprawdź ponownie
  i += 1                          #przejdź do kolejnej wartości z zakresu

input("Aby zakończyć naciśnij Enter")


