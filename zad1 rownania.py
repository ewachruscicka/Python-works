# '''ZADANIE 1
# Program rozwiązuje układ równań:
# Ax + By = C
# Dx + Ey = F

print(""""Aby rozwiązać układ równań typu
Ax + By = C
Dx + Ey = F
wprowadź kolejne współczynniki.""")

# Użytkownik wprowadza dane do równania
a = float(input("Podaj współczynnik A: "))
b = float(input("Podaj współczynnik B: "))
c = float(input("Podaj współczynnik C: "))
d = float(input("Podaj współczynnik D: "))
e = float(input("Podaj współczynnik E: "))
f = float(input("Podaj współczynnik F: "))

# Układ równań rozwiązujemy metodą wyznacznikową
# Liczymy wyznaczniki
w = a * e - b * d
wx = c * e - f * b
wy = a * f - d * c

# Jeśli wyznacznik W różny od 0:
if w != 0:
  x = wx / w
  y = wy / w
  print("Układ równań jest oznaczony i jego rozwiązanie to: ")
  print("x = ", x)
  print("y = ", y)

# Jeśli wszystkie wyznaczniki są równe 0:
elif  w == 0 and wx == 0 and wy == 0:
  print("Układ równań jest nieoznaczony - ma nieskończenie wiele rozwiązań")

# W pozostałych przypadkach:        
else:
  print("Układ równań jest sprzeczny - nie ma rozwiązania")

input("Aby zakończyć naciśnij Enter")    

        
