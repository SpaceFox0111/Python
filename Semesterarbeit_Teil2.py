def collatz(n):
    x=1
    for a in (0,n) :
        n = a
    while n > 1 :
        if n % 2 == 0 :#testen, ob n eine ganze Zahl ist
            n = n //2 #wenn n eine ganze zahl ist durch 2 teilen
            x+=1
            print(n)
        else :
            n = 3 * n + 1 #sonst wird n mit 3 multipliziert und 1 addiert
            x+=1
            print(n)
    print("------------")
    return(x)
collatz(7) #testen der Funktion bei n=9, dh die Länge ist 20


def pw_check(pw):
    """Check Password-Gültigkeit:

Checks:
Die Länge ist mindestens 8
In pw kommen sowohl Großbuchstaben, Kleinbuchstaben, Ziffern und Spezialsymbole vor
(ein Spezialsymbol sei ein beliebiges Symbol, das weder Großbuchstabe, Kleinbuchstabe noch Ziffer sei).

    """
    SpecialSym=['$','@','#']
    return_val=True #die obigen Sonderzeichen sind erlaubt
    if len(passwd) < 8: #das Password muss mind 8 Einheiten haben
        print('die Länge ist mind 8')
        return_val=False
    if not any(char.isdigit() for char in passwd): #und muss mindestens eine Ziffer enthalten
        print('Mind eine Ziffer')
        return_val=False
    if not any(char.isupper() for char in passwd): #und muss mindestens einen Grossbuchstaben enthalten
        print('mind einen Grossbuchstaben')
        return_val=False
    if not any(char.islower() for char in passwd): #und muss mindestens einen Kleinbuchstaben enthalten
        print('mind einen Kleinbuchstaben')
        return_val=False
    if not any(char in SpecialSym for char in passwd): #und ein Spezialsymbol muss auch noch enthalten sein
        print('mind Spezialsymbol')
        return_val=False
    if return_val:
        print('Ok')
    return return_val

print(pw_check.__doc__) #Eingabefunktion
pw = input('enter the password : ')
print(pw_check(pw))


class Date:

    def __init__(self, year, month, day):  # Funktion und Variablen definieren
        self.year = year
        self.month = month
        self.day = day

    def is_correct(self):  # genereller Datumscheck
        # 30: 11, 4, 6, 9
        # 28: 2
        if self.month in [4, 6, 9, 11]:  # für April, Juni, Sept, Nov
            return self.day <= 30  # der Monat hat nur 30 Tage
        elif self.month == 2:
            return self.day <= 28  # der Februar hat 28 Tage
        else:
            return self.day <= 31  # alle anderen Monate haben 31 Tage

    def tomorrow(self):  # Funktion Morgen
        new_day = self.day + 1  # plus ein Tag
        new_month = self.month
        new_year = self.year

        if new_month == 4 or new_month == 6 or new_month == 9 or new_month == 11:
            if new_day == 31:  # bei Tag 31
                new_day = 1  # zähle ein Tag hinzu
                new_month += 1  # und wechsle zum nächsten Monat
        elif self.month == 2:
            if self.ist_schaltjahr():
                if self_tag == 29:  # bei einem Schaltjahr bei Tag 29
                    new_day = 1  # zähle einen Tag hinzu
                    new_month = 3  # wechsle vom Februar zum März
            else:
                if self.day == 28:  # wenn kein Schaltjahr hat der Monat nur 28 Tage
                    new_day = 1  # dann ist der nächste Tag 1
                    new_month = 3  # und der nächste Monat ist März

        else:
            if self.day == 31:  # ansonsten haben alle anderen Monate 31 Tage
                new_day = 1  # dann ist der nächste Tag 1
                new_month = new_month + 1  # und der nächste Tag liegt im nächsten Monat
                if self.month == 12:  # bei Jahreswechsel, dh wenn der Monat Dezember ist
                    new_month = 1  # dann ist der nächste Monat Januar
                    new_jahr += 1  # und die Jahreszahl wechselt auch um 1

        return Date(new_year, new_month, new_day)

    def yesterday(self):  # Funktion yesterday
        new_day = self.day - 1  # minus ein Tag
        new_month = self.month
        new_year = self.year

        if new_month == 4 or new_month == 6 or new_month == 9 or new_month == 11:  # die Monate, welche nur 30 Tage haben
            if new_day == 1:  # bei Monatserster
                new_day = 30  # ist der gesterige Tag der 30ste
                new_month += -1  # und der Monat der Vormonat
        elif self.month == 2:  # im Februar
            if self.ist_schaltjahr():
                if self_tag == 29:  # im Fall eines Schaltjahres hat der Februar nur 29 Tage
                    new_day = -1  # dann ein Tag abziehen
                    new_month = 2  # und der Monat bleibt der gleiche
            else:
                if self.day == 28:  # sonst hat der Februar nur 28 tage
                    new_day = -1
                    new_month = 2

        else:
            if self.day == 1:  # generell bei allen anderen Monaten hat der Monat 31 Tage
                new_day = 31
                if self.month == 12:  # bei Jahreswechsel im Dezember
                    new_month = 12  # der Monat bleibt der gleiche

        return Date(new_year, new_month, new_day)  # Ausgabefunktion

    def ist_schaltjahr(self):  # Bedingungen für Schaltjahr
        if self.year % 400 == 0:  # durch 400 teilbar
            return True
        if self.year % 100 == 0:  # durch 100 teilbar
            return False
        if self.year % 4 == 0:  # durch 4 teilbar
            return True
        return False

    def __repr__(self):
        return '{}-{}-{}'.format(self.year, self.month, self.day)  # Ausgabe


Datumseingabe = Date(2021, 2, 15).tomorrow()  # Test Funktion


def cäsar(text, n):
    secrettext = ""

    for letters in text:
        number = ord(letters) #umwandlung der buchstaben in ascii

        #Check Kleinbuchstaben
        if number in range (ord("a"), ord("z") + 1): #ist Zahl Kleinbuchstabe?
            newnumber = number + n #verschiebung um n stellen
            if newnumber > ord("z"):
                newnumber -= (ord("z") - ord("a") + 1) #neues zeichen um alphabet länge verschieben (wenn bei z angelangt wieder bei a anfangen)
            if newnumber < ord("a"):
                newnumber += (ord("z") - ord("a") + 1)

        #Check Grossbuchstaben
        elif number in range(ord("A"), ord("Z")+1): #ist Zahl Grossbuchstabe?
            newnumber = number + n  # verschiebung um n stellen
            if newnumber > ord("Z"):
                newnumber -= (ord("Z") - ord("A") + 1) #neues zeichen um alphabet länge verschieben (wenn bei z angelangt wieder bei a anfangen)
            if newnumber < ord("A"):
                newnumber += (ord("Z") - ord("A") + 1)

        #Check ob Zahl
        elif number in range(ord("0"), ord("9") + 1):  # ist Zahl nummerisch?
            newnumber = number + n  # verschiebung um n stellen
            if newnumber > ord("9"):
                newnumber -= (ord("9") - ord("0") + 1) #neues zeichen im turnus verschieben (wenn am ende angelangt)
            if newnumber < ord("0"):
                newnumber += (ord("9") - ord("0") + 1)

        #check ob Sonderzeichen
        else:
            newnumber = number

        #Umwandlung Ascii in ursprüngliche Formatierung
        newdigit = chr(newnumber)
        secrettext = secrettext + newdigit #neue verschlüsselung definieren

    return secrettext #neuer verschlüsselter text

print(cäsar("hello world", -1))