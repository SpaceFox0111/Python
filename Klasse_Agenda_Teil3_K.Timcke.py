#Semesterarbeit Python & Friends Karin Timcke - Teil 2

# create a class in python for an agenda
# each entry has an index number
# the following methods have to be part of it:
# • add_entry(DateTime, String)
# • get_all_entries()
# • get_entries(DateTime from DateTime to)
# • remove_entry(int)


import datetime

class Agenda:
    def __init__(self):
        self.entries = []

    def add_entry(self, datum, kommentar):
        # convert human readable datum into DateTime
        # datetime.strptime(datum)
        entry = (datetime.datetime.strptime(datum,"%d.%m.%y"), kommentar)
        self.entries.append(entry)

    # list of "dd.mm.yy: kommentar"
    def get_all_entries(self):
        result = []
        for entry in self.entries:
            result.append(entry[0].strftime("%d.%m.%y") + ": " + entry[1])
        return result

    def get_entries(self, datum_from, datum_to): #DateTime from DateTime to
        for entry in self.entries:
            if datetime.datetime.strptime(datum_from, "%d.%m.%y") <= entry[0] <= datetime.datetime.strptime(datum_to,"%d.%m.%y"):
                result.append(entry[0].strftime("%d.%m.%y") + ": " + entry[1]) #convert DateTime into human readable datum
        return result

    def remove_entry(self, x):
        self.entries.pop(x)

agenda = Agenda()

agenda.add_entry("21.11.21", "Hello World") 
agenda.add_entry("11.11.21", "concert")
agenda.add_entry("10.11.21", "school")
agenda.add_entry("12.11.21", "office")

print(agenda.get_all_entries()) #testen der Funktion
agenda.remove_entry(0) #testen der Funktion
print(agenda.get_all_entries()) #testen der Funktion





