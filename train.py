class train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.setas=seats
    def getStatus(self):
        print(f"name of the customer is {self.name}")
        print(f"seats available is {self.setas}")
    def fareInfo(self):
        print(f"fare is {self.fare}")
    def ticketBook(self):
        if(self.setas>0):
            print(f"booked {self.setas}")
            self.setas=self.setas-1
        else:
            print("sorry!")
intercity=train("intercity-Express",90,2)
intercity.getStatus()
intercity.fareInfo()
intercity.ticketBook()
intercity.getStatus()
intercity.ticketBook()
intercity.getStatus()
intercity.ticketBook()

