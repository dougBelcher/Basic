# module person.py

def creds():
    name = "Sarah"
    age = 26
    print("person details {}, {}".format(name, age))


print("top-level in person module")

if __name__ == "__main__":
    print("person mod is run directly")
else:
    print("person mod is imported into another module")