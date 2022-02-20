class ParkingGarage():
    def __init__(self):
        self.tickets = []
        self.parking_spaces = []
        self.current_ticket = {}

    def takeTicket(self):
        # decrease the amount of tickets available by 1

        # decrease the amount of parking spaces available by 1

        pass

    def payForParking(self):
        # Display an input that waits for an amount from the user and stores it in a variable
        
        # if there has been payment, i.e. the payment variable is not empty, the ticket has been paid. Display message
        print("Payment successful. Please exit the parking garage in the next 15min.")

        # update currentTicket dictionary key "paid" to True

    def leaveGarage(self):
        # if ticket has been paid
        print("Thank you! Have a nice day!")
        
        # if ticket has not been paid, display an input prompt for payment

        # once paid, display thank you message from above ^^

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

#run code
