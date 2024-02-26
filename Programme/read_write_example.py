# Dieses Programm zeigt, wie man mit Python aus Dateien liest und in Dateien schreibt

def Durchschnitt(ergListe):
    if len(ergListe)>0:
        return sum(ergListe)/len(ergListe)
    else:
        return 0
    

# Öffnen und Einlesen der Datei wuerfelergebnisse.txt
readFile = open("Daten/Wuerfelergebnisse.txt")
dateiInhalt = readFile.read() # Mit der read()-Funktion wird die gesamte Datei auf einmal gelesen. (Für große Datei ist das nicht ratsam)
print("Das Ergebnis der read()-Funktion ist vom Typ", type(dateiInhalt))  

umgewandelterInhalt = eval(dateiInhalt) # Mit der eval()-Funktion wird ein Textausdruck ausgewertet und das Ergebnis zurückgegeben 
print("Die eval()-Funktion wandelt den Dateiinhalt um in", type(umgewandelterInhalt))  

print("Die Datei enthält {0:d} Werte mit einem Mittelwert von {1:.3f}".format(len(umgewandelterInhalt), Durchschnitt(umgewandelterInhalt)))
readFile.close() # Wenn man eine Datei nicht mehr im Zugriff braucht, sollte man sie schließen

print("Nun schreiben wir die eingelesenen Daten in eine andere Datei")
writeFile = open("./Daten/Ausgabe_Wuerfelergebnisse.txt",mode="w") # Der mode "w" öffnet die Datei zum Schreiben. Existiert sie schon, wird der alte Inhalt gelöscht.
n=0
while len(umgewandelterInhalt)>n:
    writeFile.write("Im {0:d}. Wurf war das Ergebnis {1:d}\n".format(n+1,umgewandelterInhalt[n]))
    n=n+1
writeFile.close()
