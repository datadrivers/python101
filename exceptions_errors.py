"""
Showcases for Python Workshop 5

keywords covered:
    * raise
    * try
    * except
    * finally

"""
def fraction(num, denom):
    return num / denom

fraction(1, 2)
fraction(1, 0)

#raise ZeroDivisionError  # explicitly raise exception by using the "raise" keyword
#raise ZeroDivisionError("you fool!")  # pass in a custom error message

### Exception for control flow
denominators = [5, 4, 3, 2, 1, 0, -1] # möchte gerne über die liste iterieren, egal, ob 0 drin

for denom in denominators:  # fails
    fraction(42, denom)

# möglichkeit 1 Beispiel 1
for denom in denominators:
    if denom != 0:
        fraction(42, denom)
    else:
        continue

# die lösung funktioniert. allerdings prüfen wir hier explizit jeden value, bevor wir die funktion ausführen
# das hat nachteile:
# was ist, wenn wir viele mögliche fehlerquellen haben? Dann müssen wir VOR der Laufzeit des Programms alle Möglichkeiten
# in Betracht ziehen und expizit durch checks (if statements" überprüfen)
# was ist, wenn es weitere fehlerquellen anderen typs gibt? Beispielsweise wird unsere denominator Liste selbst zur Laufzeit
# evaluiert und dies schlägt fehl!

# möglichkeit 1 Beispiel 2
denominators = [5, 4, 3, 2, 1, 0, '-1']  #  Liste enthält einen String!
for denom in denominators:
    if denom != 0:
        fraction(42, denom)
    else:
        continue

# unsere Fehlerbehandlung (denom != 0) hat uns nichts gebracht, es ist trotzdem eine Exception geworfen worden
# so dass unser Programm gecrasht ist


# möglichkeit 1 Beispiel 3
denominators = None  # Listengenerierung ist fehlgeschlagen
for denom in denominators:
    if denom != 0:
        fraction(42, denom)
    else:
        continue


### Exceptions und Errors catchen

# Möglichkeit 2 Beispiel 1
denominators = [5, 4, 3, 2, 1, 0, -1] # möchte gerne über die liste iterieren, egal, ob 0 drin
for denom in denominators:
    try:
        res = fraction(42, denom)
        print(res)
    except (ZeroDivisionError, ValueError):
        continue


# Möglichkeit 2 Beispiel 2
denominators = [5, 4, 3, 2, 1, 0, '-1']  # möchte gerne über die liste iterieren, egal, ob 0 drin
for denom in denominators:
    try:
        res = fraction(42, denom)
        print(res)
    except ZeroDivisionError as z:  # "as z" gibt referenz zur exception instance
        print(z)
    except TypeError as t:
        continue


# Möglichkeit 2 Beispiel 3
denominators = None  # Listengenerierung ist fehlgeschlagen
try:
    for denom in denominators:
        try:
            res = fraction(42, denom)
            print(res)
        except ZeroDivisionError:
            continue
        except TypeError:
            continue
except TypeError:
    print("was für ein häßliches konstrukt..")


# Beispiel für finally

denominators = [5, 4, 3, 2, 1, 0, -1] # möchte gerne über die liste iterieren, egal, ob 0 drin
print(denominators)
for denom in denominators:
    try:
        res = fraction(42, denom)
        print(res)
    except ZeroDivisionError as z:
        print(z)
        continue  # remove this for demonstration purposes
    finally:  # wird in jedem fall am ende des try - except konstrukts ausgeführt
        denominators = []
print(denominators)



### eigenen Fehler bauen
class MyError(Exception):
    """Base class for my custom errors"""
    pass

class ValueExceedsLengthError(MyError):
    """Raised when values exceeds length restriction"""
    pass


def my_demo_func(value: str):
    if len(value) > 10:
        raise ValueExceedsLengthError("Value should be less than 10 chars.")
    return value.upper()


my_demo_func("foo")
my_demo_func("foobarbazhameggs")






######
# wie uniques only raussammeln?
has_doubles = ["foo", "foo", "bar"]
has_doubles_2 = ["foo", "bar", "foo"]

import numpy as np
res, indizes = np.unique(has_doubles, return_index=True)

np.array(has_doubles)[indizes[::-1]]


def distinctify(list_):
    heap = set()
    output = []
    for s in list_:
        if s not in heap:
            output.append(s)
            heap.add(s)
    return output


heap = set()
heap_add = heap.add
[x for x in has_doubles if x not in heap and (heap_add(x) or True)]

distinctify(has_doubles)

