# Python interpreter

# Definition fibonacci funktion als anschauungsbeispiel
def fib(n):
    return n if n < 2 else fib(n-2) + fib(n-1)

# gucken, ob funktion das tut, was sie soll
fib(10)

# look at compiled byte code
# der bytecode "klebt" als argumen an jedem funktionsobjekt
fib.__code__.co_code

# wie liest man das nun? von links nach rechts, beginnend mit dem ersten operanden
# opcode modul enthält ein verzeichnis über alle operatoren, gelistet nach ordinalzahl
ord('|')
import opcode
opcode.opname[124]

# einfacher als nun den bytecode zu decheffrieren ist es, das modul dis (disassable) heranzuziehen
# das modul bietet eine vereinfachte darstellung
import dis
dis.dis(fib)


