class employee:
    company= "google"
    def getSalary(self):
        print(f"{self.company} and {self.Salary}")
harry=employee()
employee.Salary="65656"   #class attribute(obj)
harry.getSalary()