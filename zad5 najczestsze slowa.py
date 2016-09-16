# ZADANIE 5 Najczęstsze słowa
# Program wczytuje tekst z pliku i wypisuje 20 najczęściej występujących słó

def rozbijWiersz(tekst):
  wyrazy = tekst.split()
  return wyrazy
  #for slowo in slowa:
   # print(slowo)

def sprawdzSlowo(wyraz):
  ilosc = 0
  if slowo in slownikSlow:
    ilosc = slownikSlow.get(slowo)
    slownikSlow[slowo] = ilosc + 1
  else:
    slownikSlow[slowo] = int(1)

def sortuj():
  posortowane = sorted(slownikSlow.items(), key = lambda t: t[1], reverse=True)
  print(posortowane[:20])
    
      
slownikSlow = {}  #inicjalizacja pustego słownika

plik = open("panTadeusz.txt", "r")  
wiersze = plik.readlines()  #Oczytaj plik po 1 wierszu naraz

for wiersz in wiersze:
  slowa = rozbijWiersz(wiersz) #Rozbij na pojedyncze słowa
  for slowo in slowa:
    slowo = slowo.lower()
    sprawdzSlowo(slowo)
    
sortuj()
#print(slownikSlow)

plik.close()
input("\n\nAby zakończyć program, naciśnij klawisz Enter")
 

