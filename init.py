class employe:
    company= "google"
    def __init__(self,name,salary,company):
        self.name=name
        self.salary=salary
        self.company=company
        print("employee is created!")
    def getDetails(self):
        print(f"name={self.name}")
        print(f"salary={self.salary}")
        print(f"company={self.company}")
        
harry=employe("Harry",100,"YouTube")
harry.getDetails()