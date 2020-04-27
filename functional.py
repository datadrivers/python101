# funktionale elemente in python


# erstes beispiel: list comprehensions
names = ["dagmar", "sören"]
my_list = [name for name in names] # beispiel soll syntax verdeutlichen

# filtern auf "nicht sören"
my_list2 = [name for name in names if name != "sören"]

# range() funktion in python
my_list3 = [num for num in range(10)]

# beispiel: nur gerade zahlen
my_list4 = [_ for _ in range(10) if _ % 2 == 0]

# komplexeres beispiel: liste mit zehn listen die alle geraden quadrate zwischen 0 und 9^2 enthalten
my_list5 = [[_**2 for _ in range(10) if _ % 2 == 0] for i in range(10)]
