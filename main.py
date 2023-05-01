import json

class Local:
    def __init__(self):
        self.numero_local = "0"
        self.type_local = "X"
    def valider_technique(self):
        if self.type_local == "technique":
            return True
        else:
            return False

class Etudiant:
    def __init__(self, p_nom: str = "XXX", p_ls_locaux : Local = Local()):
        self.nom = p_nom
        self.Local = p_ls_locaux

# Instanciation
L1 = Local()
L2 = Local()
L1.numero_local = 100
L1.type_local = "technique"
L2.numero_local = 200
L2.type_local = "normal"
list_local = [L1, L2]
E1 = Etudiant("Etudiant1", L1)
print(E1.nom)
print(E1.Local[0].numero_local)
print(E1.Local[0].type_local)
print(E1.Local[1].numero_local)
print(E1.Local[1].type_local)
print("*********************")


#json
try:
    with open(".\serialiser\serialiser.json", "w") as F:
        json.dump(E1.__dict__, F)
except:
    print("Erreur d'écriture.")

# Json string
import jsonpickle
Json_string = jsonpickle.encode(E1)
print(Json_string)

# Sérialiser
# with open("test.json", "w") as F:
#     F.write(Json_string)

try:
    with open("./serialiser/" + "Etudiant_ :" + E1.nom + ".json", "w") as F:
        F.write(Json_string)
except :
    print("Erreur d'écriture.")

# Désérialiser
# with open("test.json", "r") as F:
#     Json_string1 = F.readline()


with open("./serialiser/" + "Local :" + L1.numero_local + ".json", "r") as F:
        Json_string1 = F.readline()
Mon_Local = Local()
Mon_Local = jsonpickle.decode(Json_string1)
print(Mon_Local.numero_local, Mon_Local.type_local)


E2 = jsonpickle.decode(Json_string1)
print(E2.nom, E2.Local[0].numero_local, E2.Local[1].numero_local)
