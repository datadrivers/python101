"""

Things covered:
    * Listen, Sets, Dictionaries, Tuples

Concepts:
    * mutability / immutabilty

Resources:
    * built-ins: https://docs.python.org/3/library/stdtypes.html
    * specialised: https://docs.python.org/3/library/datatypes.html
"""

# Wichtige Datenstrukturen


# mutable
list1 = []
list2 = list()
dict1 = dict()
dict2 = {'key': 'value'}
set1 = set()
set2 = {}

# immutable
t1 = tuple()
t2 = ()

# Datenstrukturen sind Objekte
# Beispiel mit Listen
list1 = []
list2 = []
list3 = list1

list1 == list2  # Wert gleich (leere Liste)
list1 is list2  # aber unterschiedliche Objekte (zwei Listen an unterschiedlichen Speicherorten)
list3 == list1
list3 is list1  # list3 ist nur Referenz auf list1 => selbes Objekt

# Folge:
list3.append(1)
list3
list1  # !

# "Echte", physische Kopie der liste erzwingen:
list3 = list1.copy()
list3 is list1


# warum das alles? A common bug prone python anti-pattern:
def append(number, number_list=[]):
    number_list.append(number)
    return number_list


append(1)
append(5)  # !
# Begründung: die liste als default argument wird beim erstmaligen laden des codes als
# objekt im speicher erzeugt ("gecached"). jeder weitere aufruf der funktion operiert
# auf dem bereits existenten objekt
# Lösung:

def append(number, number_list=None):
    if number_list is None:  # man beachte "is" !
        number_list = []
    number_list.append(number)
    return number_list


append(1)
append(5)
