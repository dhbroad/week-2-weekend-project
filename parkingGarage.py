class ParkingGarage():
    def __init__(self):
        self.tickets = 6
        self.parking_spaces = [1, 2, 3, 4, 5, 6]
        self.current_ticket = {"paid":False}

    def takeTicket(self):
        # decrease the amount of tickets available by 1

        # decrease the amount of parking spaces available by 1

        pass

    def payForParking(self):
        # Display an input that waits for an amount from the user and stores it in a variable
        payment = input("Please insert the amount 10.50 for your ticket. ")

        # if there has been payment, i.e. the payment variable is not empty, the ticket has been paid. Display message
        if payment == "10.50":
            print("Payment successful. Please exit the parking garage in the next 15min.")
            # update currentTicket dictionary key "paid" to True
            self.current_ticket["paid"] = True
        

    def leaveGarage(self):
        # if ticket has been paid
        if self.current_ticket["paid"] == True:
            print("Thank you! Have a nice day!")
        # if ticket has not been paid, display an input prompt for payment
        elif self.current_ticket["paid"] == False:
            self.payForParking()
            # once paid, display thank you message from above ^^
            self.leaveGarage()

        # update parkingSpaces list to increase by 1

        # update tickets list to increase by 1

    def run(self):
        while True:
            # add condition
            self.takeTicket()

            # add condition
            self.payForParking()

            # add condition
            self.leaveGarage()

parking_garage = ParkingGarage()
print(parking_garage.current_ticket)
