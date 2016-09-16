# ZADANIE 6 SZYFROWANIE
# Program szyfruje i deszyfruje plik tekstowy zadanym kluczem

# zakładamy że tekst będzie napisanyw języku polskim
alfabet = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUVWYZŹŻ"
klucz = "31206"

def szyfruj(tekst):
  tekstZaszyfrowany = ""
  lKlucza = len(klucz)
  lAlfabetu = len(alfabet)
  licznik = 0 # inicjalizacja licznika pętli
  for i in tekst: #dla każdego znaku w tekście
    if i in alfabet: #jeśli znak jest literą alfabetu
      licznik += 1 
      a = alfabet.index(i) #a=indeks litery w alfabecie (kolejny numer pozycji)
      b = int(klucz[licznik % lKlucza - 1]) #b=pozycja z klucza która ma być użyta do zaszyfrowania litery
      tekstZaszyfrowany += alfabet[(a + b) % lAlfabetu] #znajdź zaszyfrowaną literę i dopisz do wyniku
    else: #jeśli znak nie jest literą alfabetu (np. liczba albo znak interpunkcyjny)
      tekstZaszyfrowany += i #dopisz ją do wyniku
  return tekstZaszyfrowany 

def odszyfruj(tekst):
  tekstOdszyfrowany = ""
  lKlucza = len(klucz)
  lAlfabetu = len(alfabet)
  licznik = 0
  for i in tekst:
    if i in alfabet:
      licznik += 1 
      a = alfabet.index(i) #a=indeks litery w alfabecie (kolejny numer pozycji)
      b = int(klucz[licznik % lKlucza - 1]) #b=pozycja z klucza która ma być użyta do odszyfrowania litery
      tekstOdszyfrowany += alfabet[(a - b) % lAlfabetu] #znajdź odszyfrowaną literę i dopisz do wyniku
    else: #jeśli znak nie jest literą alfabetu (np. liczba albo znak interpunkcyjny)
      tekstOdszyfrowany += i #dopisz ją do wyniku
  return tekstOdszyfrowany

def rozbijWiersz(tekst): #rozbij (tekst) na wiersze
  wyrazy = tekst.split() 
  return wyrazy

def rozbijNaSlowa(wiersze): #rozbij (wiersz) na pojedyncze słowa
  tekst = ""
  for wiersz in wiersze:
    slowa = rozbijWiersz(wiersz) 
    for slowo in slowa:
      slowo = slowo.upper()
      tekst += slowo

def zapiszPlik(wynik):
  plik = open("mojNowyTekst.txt", "w")
  plik.write(wynik)
  plik.close()
  plik = open("mojNowyTekst.txt", "r")
  print("\nZapisywany tekst: \n" + plik.read())
  plik.close()

def main(): #definicja głównej pętla programu oparta na menu wyboru
  wybor = None
  while wybor != "0":
    print \
    ("""
    SZYFROWANIE I ODSZYFROWYWANIE
    
    1 - szyfrowanie
    2 - odszyfrowywanie

    0 - zakończ program
        
    """)
    wybor = input("Wybierz czynność: ")
    print()

    if wybor == "1":
      plik = open("mojTekst.txt", "r") 
      wiersze = plik.read() 
      tekst=wiersze.upper() 
      print("Tekst wczytany: \n" + tekst)
      wynik = szyfruj(tekst)
      print("\nTekst zaszyfrowany: \n" + wynik)
      plik.close()
      zapiszPlik(wynik)
    elif wybor == "2":
      plik = open("mojTekst.txt", "r")  
      wiersze = plik.read()
      tekst=wiersze.upper()
      print("\nTekst zaszyfrowany: \n" + tekst)
      wynik = odszyfruj(tekst)
      print("\nTekst odszyfrowany: \n" + wynik)
      plik.close()
      zapiszPlik(wynik)
    elif wybor == "0":
      input("\n\nAby zakończyć program, naciśnij klawisz Enter.") 
    else:
      print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")

#wywołanie głównej pętli programu      
main()

     








