# ZADANIE 7 TURTLE
# Program rysuje wykres funkcji jednej zmiennej
from turtle import*
from math import*

def wczytajZakres():
  zakres = int(input("Podaj min zakres rysowania: "))
  return zakres

def wczytajZakres2():
  zakres = int(input("Podaj max zakres rysowania: "))
  return zakres

def wczytajFunkcje():
  funkcja = input("y = ")
  return funkcja

def rysujUklad():
  #rysuje układ współrzędnych
  speed(0)
  setworldcoordinates(-17,-17,17,17)
  setpos(0,0)
  clear()
  setheading(0)
  rysujMiaryUkladu()
  setpos(0,0)
  pd()
  color("black")
  for i in range (4):
    setpos(0,0)
    fd(17)
    rt(90)
  pu()

def rysujMiaryUkladu():
  #rysuje podział na jednostki (siatkę)
  speed(0)
  color("yellow")
  for i in range(35):
    pu()
    goto(-17+i,-17)
    pd()
    goto(-17+i,17)
    pu()
  for j in range(35):
    pu()
    goto(-17,-17+j)
    pd()
    goto(17,-17+j)
    pu()
  
def main():
  min = int(wczytajZakres())
  max = int(wczytajZakres2())
  f = wczytajFunkcje()
  rysujUklad()

  w = Screen()
  w.title("Rysowanie wykresu funkcji 1 zmiennej")
  w.setup(1280,720)
  speed(2)
  pu()
  goto(0,0)
  pu()
  pensize(2)
  color("red")
  for x in range (min, max+1):
    y = f
    goto(x,eval(f))
    pd()

main()

