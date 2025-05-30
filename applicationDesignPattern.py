from exercices.design_patterns.ex_singleton.contact import Contact


contact1 = Contact("Doe", "john@test.fr","John")

identifint1 = id(contact1)
contact2 = Contact("Doe", "john@test.fr","John")
identifint2 = id(contact2)

contact3 = Contact("Dupont",  "paul@test.fr","Paul")
identifint3 = id(contact3)

print(f"Contact 1: {contact1}, ID: {identifint1}")
print(f"Contact 2: {contact2}, ID: {identifint2}")
print(f"Contact 3: {contact3}, ID: {identifint3}")


contact1 is contact2  # True, car c'est le même objet
print(f"Contact 1 is Contact 2: {contact1 is contact2}")  # True, car c'est le même objet