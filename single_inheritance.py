class Employee:
    company="google"
    def showDetails(self):
        print("this is an Employe")
class Programmer(Employee):
    language="Python"
    def getLanguage(self):
        print(f"language is {self.language}")
    def showDetails(self):
        print("programmer!")
e=Employee()
e.showDetails()
p=Programmer()
p.showDetails()
p.getLanguage()