# Write a class train which has a method to book a ticket, get status(no. of sets) and get false information of trains running under Indian railways.
class Train:
    def __init__(self,seats,fair):
        self.seats=seats
        self.fair=fair

    def book(self):
        if self.seats==0:
            print("No tickets are left to book")
        print("The ticket have been booked") 
        self.seats=self.seats-1
    
    def status(self):
        print("The status of no. of tickets is-") 
        print(self.seats)
        
    def fairprice(self):
        print("The fair of tickets is-") 
        print(self.fair)
    
    
        
t=Train(45,899)
t.fairprice()
t.book()
t.status()
    

    