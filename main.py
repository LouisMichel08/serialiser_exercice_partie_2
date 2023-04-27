import json

class Local:
    def __init__(self):
        self.numero_local = "0"
        self.type_local = "X"

class Etudiant:
    def __init__(self, p_nom: str = "", p_local: Local = Local()):
        self.nom = p_nom
        self.Local = p_local

# Instanciation
L1 = Local()
L2 = Local()
L1.numero_local = 100
L1.type_local = "Technique"
L2.numero_local = 200
L2.type_local = "Normal"
list_local = [L1, L2]
E = Etudiant("Hocini", L1)
print(E.nom)
print(E.Local.numero_local, E.Local.type_local)
print("*********************")


#json
try:
    with open(".\serialiser\serialiser.json", "w") as F:
        json.dump(E.__dict__, F)
except:
    print("Erreur d'écriture.")

# Json string
import jsonpickle
Json_string = jsonpickle.encode(E)
print(Json_string)

with open("test.json", "w") as F:
    F.write(Json_string)
