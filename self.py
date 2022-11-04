class employe:
    company= "google"
    def getSalary(self):
        print(f"{self.company} and {self.Salary}")
harry=employe()
harry.Salary=1000   #instance attribute(obj)
harry.getSalary()