"""

Things covered:
    * Module
    * Funktionen
    * Klassen

Concepts:
    * alles ist ein dict!

Resources:
    * modules: https://docs.python.org/3/tutorial/modules.html
    * specialised: https://docs.python.org/3/library/datatypes.html
"""


# Module (alles, was ein .py file ist, heißt "modul") sind dictionaries! Alles was
# Module also effektiv tun, ist "namespaces" zu schaffen, so dass wir bessere Codestruktur erhalten
# beispiel: Variable a existert in my_module1 und in my_module2 => Wir können a als Namen mehrfach
# verwenden und über my_module1.a resp. my_module2.a  darauf zugreifen
import main

main.__dict__
# insbesondere wird hier deutlich, das ALLES, was im Rahmen eines moduls verwendet werden kann
# z.b. die built-in standard funktionen, doc-strings.. sich in diesem dict wiederfindet

# Klassendefinition
class MyClass:
    pass

# Klassen sind eigentlich nur "syntactic sugar" für dicts..
A = MyClass()  # instanziieren einer klasse.. A heißt "Instanz" bzw. instance
A.__dict__

A
class MyClass:

    name = "paul"  # klassenattribut

A = MyClass()
A.__getattribute__("name")  # kompliziert..
A.name  # einfach

class MyClass:

    name = "paul"

    def foo(self):  # funktionen auf klassen heißen "methoden"
                    # self ist eine Referenz auf die Instanz der klasse, auf der foo ausgeführt wird
                    # dabei ist der name self eine konvention - die zuweisung erfolgt über die parameter
                    # position (nämlich den erstgenannten)
        self.name = "dan"
        return "bar"

A = MyClass()
A.foo() # funktioniert
MyClass.foo()  # fehler: auf MyClass kann foo nicht ausgeführt werden, da keine Instanz der Klasse
               # als Parameter übergeben wurde 'foo() missing 1 required positional argument: 'self''

class Animal:

    alive = True

    # __init__ definiert, was nach der instanziierung der klasse ausgeführt werden soll
    # hier: instanz erhält attribut "legs" mit wert 2
    def __init__(self):
        self.legs = 2  # instanzattribut


timmy = Animal()
timmy.legs

# Unterschied Instanz und Klassenattribut
tina = Animal()
tina.alive == timmy.alive
tina.legs == timmy.legs

# ändern instanz attribut
tina.legs = 4
tina.legs == timmy.legs

# ändern klassenattribut
Animal.alive
tina.alive
Animal.alive = False
Animal.alive
tina.alive

# Achtung! bei Änderung auf der Instanz, statt auf der Klasse, ändern wir die Eigenschaft "Klassen"-
# attribut gleich mit!
tina.alive = True  # tina hat nun ein instanzattribut alive mit dem wert True
timmy.alive == tina.alive

# Timmy ist nicht betroffen
Animal.alive = True
timmy.alive == tina.alive

# Klassenmethoden
class Animal:

    alive = True

    def __init__(self):
        self.legs = 2

    # @classmethod ist ein decorator (später mehr), der anzeigt, dass hier nicht auf der
    # Instanz, sondern auf der Klasse operiert wird (daher die Konvention cls statt self)
    @classmethod
    def move(cls):
        return "okay, okay.."


# Vererbung
# Cat erbt von Animal alle Eigenschaften (Funktionen, Attribute)
class Cat(Animal):

    def jeff(self):
        return "BLAHABLAHBLAH"

jimbo = Cat()
jimbo.alive

timmy.jeff()  # fehler, hat timmy nicht!!
jimbo.jeff()  # jimbo kann den jeff machen..

# Magicmethods
# in python sind __funktionsname__ sog. magicmethods. Über sie können "Protokolle" implementiert werden
# Protokolle definieren, wie Objekte miteinander interagieren
# Beispiel:
# Wir wollen erreichen, dass der Operator "+" zwischen zwei Cat Objekten ein neues Catobjekt erzeugt
# also nachwuchs = jimbo + lisa , wobei nachwuchs und lisa ebenfalls Cat Instanzen sind

class Cat(Animal):

    def jeff(self):
        return "BLAHABLAHBLAH"

    def __add__(self, other):  # streng genommen müssten wir hier noch prüfen, ob "other" eine Cat ist..
        return self.__class__()

jimbo = Cat()
lisa = Cat()
nachwuchs = jimbo + lisa  # "+" ist also in wahrheit nur "syntactic sugar" für
                          # jimbo.__add__(tina)
type(nachwuchs)
# frage: was wird eigentlich durch <SomeClass>() aufgerufen?
# Antwort: das ist auch nur syntactic sugar! => google python magicmethods..


# Statische Methoden
class Foo:

    # statische methoden können ohne eine instanz der klasse und ohne referenz auf die klasse
    # verwendet werden
    @staticmethod
    def bar():  # beachte: erwartet nicht zwangsläufig einen parameter!
        return "hello world"

Foo.bar()


