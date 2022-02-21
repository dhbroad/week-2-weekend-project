class ParkingGarage():
    def __init__(self):
        self.occupancy = [1, 2, 3, 4, 5, 6]
        self.currentTicket = {
            "1": False,
            "2" : False,
            "3" : False,
            "4" : False,
            "5" : False,
            "6" : False
            }
        self.maxOccupancy = 6

    def takeTicket(self):
        if len(self.occupancy) > 0:
            print(f"Your ticket number is {self.occupancy[len(self.occupancy)-1]}. Please retain this ticket number as it will be needed for payment.")
            self.occupancy.pop()
        else:
            print("The parking garage is full. Please come back later.")

    def payForParking(self):
        while True:
            ticket_number = input("Please enter your ticket number: ")
            payment = input("Your cost is $10 for your ticket, please type 10 in the prompt: ")
            if payment == "10":
                print("Payment successful. Please exit the parking garage in the next 15 minutes. Thank you and see you soon!")
                self.currentTicket[ticket_number] = True
                break
            else:
                print(f"Insufficient Funds. Please enter the amount of 10 : ")

    def leaveGarage(self):
        ticket_number = input("Please enter your ticket number: ")
        if self.currentTicket[ticket_number] == True:
            print("Thank you! Have a nice day!")
            self.currentTicket[ticket_number] = False
            self.occupancy.append(int(ticket_number))
            self.occupancy.sort()
        elif self.currentTicket[ticket_number] == False:
            print("Sorry, but this ticket hasn't been paid for. Please enter 'pay' in the prompt to begin the payment process.")

        
    def run(self):
        while True:
            user_input = input("Welcome to the Parking Garage. Please type 'ticket' to take a ticket, 'pay' to pay for your ticket, 'leave' to leave the garage, or 'quit' to exit the prompt. (ticket/pay/leave/quit): ")
            if user_input.lower() == "ticket":
                self.takeTicket()
            elif user_input.lower() == "pay":
                self.payForParking()
            elif user_input.lower() == "leave":
                self.leaveGarage()
            elif user_input.lower() == "quit":
                print("Thank you and goodbye!")
                break
            else:
                print("Invalid Response. Please type one of the following options. (ticket/pay/leave/quit): ")

PG = ParkingGarage()
PG.run()