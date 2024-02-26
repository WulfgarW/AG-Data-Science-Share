# Dies ist eine Programmieraufgabe zum Thema eigener Funktionen

# Gegeben ist eine Liste von Würfelergebnissen
# Schreibt dazu ein Programm, das den Durchschnittswert für alle Würfelergebnisse und den für die ersten 10
# und für die zweiten 10 (11 bis 20) berechnet und ausgibt

def Mittelwert(wertListe):
    if len(wertListe)==0:
        return 0
    else:
        return sum(wertListe)/len(wertListe)

listeWürfelergebnisse = [6, 2, 1, 4, 6, 1, 1, 1, 1, 1, 4, 4, 4, 2, 5, 4, 1, 3, 1, 1, 4, 4, 2, 1, 5, 4, 4, 4, 2, 5, 4, 4, 6, 6, 2, 6, 3, 4, 6, 6, 5, 3, 2, 4, 4, 3, 2, 6, 2, 3]
print("Mittelwert Gesamtliste: ",Mittelwert(listeWürfelergebnisse))
print("Mittelwert erste 10 Werte: ",Mittelwert(listeWürfelergebnisse[0:10]))
print("Mittelwert zweite 10 Werte (11 bis 20): ",Mittelwert(listeWürfelergebnisse[10:20]))

