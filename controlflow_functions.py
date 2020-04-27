"""

Things covered:
    * if, else
    * looping

Concepts:
    * basic controlflow
    * function definitions

Resources:
    * controlflow: https://docs.python.org/3/tutorial/controlflow.html
"""

if False:
    print("hello world")
else:
    print("hello whatever")


teilnehmer = {"Timo", "Sylvia", "Daniel"}
for index, name in enumerate(teilnehmer):
    print(name)
    if index == 1:
        break


teilnehmer_id = {"Timo": 3, "Sylvia": 17, "Daniel": 21}
for name, id_ in teilnehmer_id.items():
    print(name)
    print(id_)


strafe = "timo schreibt die hausordnung ab!"
for zeile in range(500, 510, 3):
    print(strafe)


