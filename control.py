from models import Person

class Control:

    def __init__(self):
        self.personList = []
    
    def add(self, name, age):
        name = name.capitalize()
        newPerson = Person(name, age)
        self.personList.append(newPerson)
        print("Pessoa Adicionada")
        return newPerson

    def showName(self):
        alphaList = []
        for p in self.personList:
            alphaList.append((p.getName(), p.getAge()))
        return sorted(alphaList, key=lambda x: x[0]) 
    
    def showAge(self):
        ageList = []
        for p in self.personList:
            ageList.append((p.getName(), p.getAge()))
        return sorted(ageList, key=lambda x: x[1]) 

    def classify(self, person):
        age = person.getAge()
        if age in range(0,13):
            return "Criança"
        elif age in range(13,20):
            return "Adolescente"
        elif age in range(21, 66):
            return "Adulto"
        else:
            return "Idoso"
