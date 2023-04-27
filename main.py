import json

class Local:
    def __init__(self):
        self.numero_local = "0"
        self.type_local = "X"

class Etudiant:
    def __init__(self, p_nom: str = "", p_ls_locaux : Local = []):
        self.nom = p_nom
        self.Local = p_ls_locaux

# Instanciation
L1 = Local()
L2 = Local()
L1.numero_local = 100
L1.type_local = "Technique"
L2.numero_local = 200
L2.type_local = "Normal"
list_local = [L1, L2]
E = Etudiant("Hocini", list_local)
print(E.nom)
print(E.Local[0].numero_local)
print(E.Local[0].type_local)
print(E.Local[1].numero_local)
print(E.Local[1].type_local)
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

# Sérialiser
with open("test.json", "w") as F:
    F.write(Json_string)

# Désérialiser
with open("test.json", "r") as F:
    Json_string1 = F.readline()

E2 = jsonpickle.decode(Json_string1)
print(E2.nom, E2.Local[0].numero_local, E2.Local[1].numero_local)
