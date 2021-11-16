#Semesterarbeit Python & Friends Karin Timcke - Teil 1

#Arithmetisches Mittel

import statistics
Liste_ages = [19, 22, 34, 26, 32, 30, 24, 24]

def mean(Liste_ages): #Funktion arithmetisches Mittel
    return sum(Liste_ages) / len(Liste_ages) #Summer der einzelnen Elemente in der Liste dividiert durch die Anzahl der Elemente

print("Das arithmetische Mittel lautet : " + str(mean(Liste_ages))) #Ausgabe des Resultates


#Geometrisches Mittel für durchschnittliche Wachstumsfaktoren
#Berechnung: Um das ungewogene geometrische Mittel zu berechnen, multipliziert man zunächst alle gegebenen Elemente, dann die n-te Wurzel aus dem Produkt
#- Berechnung prozentualer Veränderungen

import numpy as np

import math

runners = [6, 7, 3, 9, 10, 15]

x = 1
for i in range(0, len(runners)):
    x = x * runners[i]
y = (float)(math.pow(x, (1 / len(runners)))) #The math. pow() method retourniert den Wert von x hoch y
result = (float)(y)

print("Das geometrische Mittel lautet : " + str(result))


#Harmonisches Mittel
#Mittelwerte von Verhältniszahlen berechnen

def harmMittel(a, b):
    a = float(a)
    b = float(b)

    return round(2 / ((1 / a) + (1 / b)), 2) #Formel Harmonisches Mittel - Anzahl Beob. / Dividiert durch Brüche - (Brüche, die eine Beziehung widerspiegeln)

print("Das harmonische Mittel lautet : " + str(harmMittel(440, 880)))


#Median

ITRA_Punkte_Läufer = [181, 187, 196, 196, 198, 203, 207, 211, 215]

def median(ITRA_Punkte_Läufer):
    x = sorted(ITRA_Punkte_Läufer)
    index = len(x) // 2

    # falls dataset ungerade ist
    if len(ITRA_Punkte_Läufer) % 2 != 0:
        return x[index]

    # falls das dataset gerade ist
    return (x[index - 1] + x[index]) / 2

print("Der Median der ITRA Punkte der Läufer lautet : " + str(median(ITRA_Punkte_Läufer)))


#Modus: Der Modus (auch Modalwert genannt) einer Datenreihe ist das Merkmal bzw. der Wert mit der größten Häufigkeit

points_per_run = [3, 15, 23, 42, 30, 10, 10, 10, 12]
trailruns = ['nendaz', 'verbier', 'eiger', 'transviamala',
               'utmb', 'chamonix', 'chamonix', 'davos']

def mode(points_per_run):
    frequency = {}

    for value in points_per_run:
        frequency[value] = frequency.get(value, 0) + 1

    most_frequent = max(frequency.values())

    modes = [key for key, value in frequency.items()
                      if value == most_frequent]

    return modes

print("Der Modus der Punkte pro Lauf lautet : " + str(mode(points_per_run))) #testen der Funktion
print("Der Name des Laufes wo sich der Modus befindet : " + str(mode(trailruns))) #testen der Funktion

#Varianz:
#Schritt 1 - Mittelwert aller Beobachtungswerte berechnen.
#Schritt 2 - Abweichungen der Beobachtungswerte vom Mittelwert bestimmen.
#Schritt 3- Abweichungen (aus Schritt 2) quadrieren.
#Schritt 4 - Quadrierte Abweichungen (aus Schritt 3) addieren.
#Schritt 5 - Summe (aus Schritt 4) durch Gesamtanzahl der Beobachtungen – 1 teilen

import math

from statistics import variance

from fractions import Fraction as fr

Liste_ages = [19, 22, 34, 26, 32, 30, 24, 24]

print("Variance der Altersliste is % s " %(variance(Liste_ages)))


#Standardabweichung:
#Wurzel aus Varianz

import numpy as np

läufer = {'a': 20, 'b': 32, 'c': 33, 'd': 43, 'e': 28}

listr = []

for value in läufer.values():
    listr.append(value)

mean = sum(listr) / len(listr)
variance = sum([((x - mean) ** 2) for x in listr]) / len(listr)
res = variance ** 0.5
print("Standardabweichung lautet : "+ str(res))

#Variationskoeffizient
#Standardabweichung geteilt durch Mittelwert

import numpy as np

läufer = {'a': 20, 'b': 32, 'c': 33, 'd': 43, 'e': 28}

listr = []

for value in läufer.values():
    listr.append(value)

mean = sum(listr) / len(listr)
variance = sum([((x - mean) ** 2) for x in listr]) / len(listr)
res = variance ** 0.5
varko = res / mean
print("Der Variationskoeffizient lautet : " + str(varko))





