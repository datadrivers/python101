"""

Things covered:
    * int, float, str, bool, None, complex
    * is vs. ==
    * for loop

Concepts:
    * everything is an object
    * comparisions


Resources:
    * built-ins: https://docs.python.org/3/library/stdtypes.html
    * specialised: https://docs.python.org/3/library/datatypes.html
"""

# Grundsätzlich gilt: Alles in Python ist ein Objekt
# einige wichtige datentypen
a = 0
type(a)
a == True

b = 2.2
type(b)
b == True

c = "string"
type(c)
c == True

d = False    # other: True
type(d)
d == True

e = None
type(e)
e == True

f = complex(1, 3)
type(f)
f == True

# unterschied zwischen is und ==
# == vergleicht die werte der operanden, is  vergleicht die objekte selbst ("object identity")
a = 42
b = 42

a == b
a is b

a = 1337
b = 1337
b is a

a = b
b is a

# ebenso: != und is not
a != b
a is not b

# weiteres beispiel..
a = 1336
b = 1336

# erwartung: sollte wie oben laufen
a == b
a is b

# warum anders?
# der python interpreter erzeugt beim erstmaligen start die integerwerte von -255 bis 256 und legt diese
# in einem global verfügbaren speicherraum ab. Diese Objekte sind Singletons (es gibt sie nur genau einmal)
# Wann immer also ein int in diesem Wertebereich genutzt wird, erzeugen wir kein neues Objekt, sondern
# wir arbeiten mit einer Referenz auf ein bestehendes Objekt
#
am_i_singleton = b - 1334
am_i_singleton == 2
am_i_singleton is 2

# None ist Singleton!
foo = None
bar = None
foo is bar



# weitere vergleiche
a > b
b >= a
b <= a
a != b


# warum brauche ich überhaupt "is" ?
