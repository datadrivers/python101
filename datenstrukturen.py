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
dict2 = {}
set1 = set()
set2 = {}

list1.append(1)
list1.pop(0)
list1
list1[0]

dict2 = {'key': 1, 'key2': 2.2, 'key3': list1}
dict2
dict2.items()

# immutable
t1 = tuple()
t2 = ()

# unpacking
t3 = [1, 3, 8]
a, b, c = t3
t3[1]


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


## TODO: das hier mal ausarbeiten..
a = 1337
b = a
a = 10000
b


# warum das alles? A common bug prone python anti-pattern:
def append_buggy(number, number_list=[]):
    number_list.append(number)
    return number_list


def append_alternative(number):
    number_list = []
    number_list.append(number)
    return number_list

append_alternative(6)
append_alternative(9)
append(9)
append(5)

append(1)
append(5)  # !
# Begründung: die liste als default argument wird beim erstmaligen laden des codes als
# objekt im speicher erzeugt ("gecached"). jeder weitere aufruf der funktion operiert
# auf dem bereits existenten objekt
# Lösung:


def append_correct(number, number_list=None):
    if number_list is None:  # man beachte "is" !
        number_list = []
    number_list.append(number)
    return number_list


list1 = append_buggy(1)
list1 = append_buggy(2, [])
list1


list13 = append_correct(1)
list13 = append_correct(1, None)
list13

del list13

append(1)
append(5)
