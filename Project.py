class FlightBookingSystem:
    def __init__(self):
        self.users = []  # List to store registered users
        self.flights = [  # List to store available flights
            {"id": "F101", "destination": "New York", "seats": 5, "bookings": []},
            {"id": "F202", "destination": "London", "seats": 5, "bookings": []},
            {"id": "F303", "destination": "Paris", "seats": 5, "bookings": []}
        ]
    
    def register_user(self, username):
        if username in self.users:
            print("User already exists.")
        else:
            self.users.append(username)
            print(f"User '{username}' registered successfully!")

    def search_flights(self):
        print("\nAvailable Flights:")
        for flight in self.flights:
            print(f"{flight['id']}: {flight['destination']} (Seats Available: {flight['seats']})")

    def book_flight(self, username):
        if username not in self.users:
            print("User not registered.")
            return

        self.search_flights()
        flight_id = input("Enter Flight ID to book: ")
        
        for flight in self.flights:
            if flight["id"] == flight_id and flight["seats"] > 0:
                flight["seats"] -= 1
                flight["bookings"].append(username)
                print(f"Flight {flight_id} booked successfully for {username}.")
                return
        
        print("Invalid selection or no seats available.")
    
    def cancel_booking(self, username):
        if username not in self.users:
            print("User not registered.")
            return

        print(f"\nYour Bookings:")
        user_bookings = [flight for flight in self.flights if username in flight["bookings"]]
        
        if not user_bookings:
            print("No bookings found.")
            return

        for flight in user_bookings:
            print(f"{flight['id']} - {flight['destination']}")
        
        flight_id = input("Enter Flight ID to cancel: ")
        
        for flight in self.flights:
            if flight["id"] == flight_id and username in flight["bookings"]:
                flight["bookings"].remove(username)
                flight["seats"] += 1
                print(f"Booking for flight {flight_id} canceled successfully.")
                return
        
        print("Invalid selection or no such booking found.")
    
    def manage_bookings(self, username):
        if username not in self.users:
            print("User not registered.")
            return

        print(f"\nBookings for {username}:")
        has_booking = False
        for flight in self.flights:
            if username in flight["bookings"]:
                print(f"{flight['id']} - {flight['destination']}")
                has_booking = True
        
        if not has_booking:
            print("No bookings found.")

    def main(self):
        while True:
            print("\n1. Register\n2. Search Flights\n3. Book Flight\n4. Manage Bookings\n5. Cancel Booking\n6. Exit")
            choice = input("Select an option: ")
            
            if choice == "1":
                username = input("Enter username: ")
                self.register_user(username)
            elif choice == "2":
                self.search_flights()
            elif choice == "3":
                username = input("Enter username: ")
                self.book_flight(username)
            elif choice == "4":
                username = input("Enter username: ")
                self.manage_bookings(username)
            elif choice == "5":
                username = input("Enter username: ")
                self.cancel_booking(username)
            elif choice == "6":
                print("Exiting system.")
                break
            else:
                print("Invalid choice.")

# Run the system
system = FlightBookingSystem()
system.main()
