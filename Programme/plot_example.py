# Dieses Programm zeigt eine erste Datenvisualisierung mit PyPlot
import math
import matplotlib.pyplot as plt

def GedämpfteSchwingung(x):
    # Eine gedämpfte Schwingung mit der Frequenz 5 Hz und einer Dämpfungskonstanten von 0,5 
    return math.cos(x*2*math.pi)*10*math.e**(-0.5*x)

x=[]
y=[]
for n in range(100):
    # Wir erzeugen eine Liste mit x-Koordinaten und eine korrespondierende mit y-Koordinaten
    x.append(n/20)
    y.append(GedämpfteSchwingung(x[len(x)-1]))
plt.plot(x, y,'ro') # Es sollen die erzeugten Datenpaare (x[i],y[i]) als rote Kreise (='ro') geplottet werden
plt.xlim(0,5) # Hiermit legen wir fest, dass die dargestellte x-Achse von 0 bis 5 gehen soll
plt.show()

print("Programmende erreicht")
