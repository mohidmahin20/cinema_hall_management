class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)

    @classmethod
    def view_all_shows(cls):
        print("Shows in Star Cinema:")
        for hall in cls.hall_list:
            hall.view_show_list()

    @classmethod
    def view_available_seats(cls, show_id):
        for hall in cls.hall_list:
            hall.view_available_seats(show_id)

    @classmethod
    def book_tickets(cls, show_id, num_tickets, seat_list):
        for hall in cls.hall_list:
            if hall.book_seats(show_id, num_tickets, seat_list):
                return
        print(f"Show ID {show_id} not found.")

class Hall:
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)
        self.seats[id] = [[0] * self.cols for _ in range(self.rows)]

    def book_seats(self, show_id, num_tickets, seat_list):
        if show_id not in self.seats:
            print(f"Invalid show ID: {show_id}")
            return False

        show_seats = self.seats[show_id]
        booked_seats = 0

        for seat in seat_list:
            row, col = seat
            if 1 <= row <= self.rows and 1 <= col <= self.cols:
                if show_seats[row - 1][col - 1] == 0:
                    show_seats[row - 1][col - 1] = 1
                    booked_seats += 1
                else:
                    print(f"Seat ({row}, {col}) is already booked for show {show_id}.")
            else:
                print(f"Invalid seat ({row}, {col}) for show {show_id}.")

        if booked_seats == num_tickets:
            print(f"Successfully booked {num_tickets} ticket(s) for show {show_id}.")
            return True
        else:
            print(f"Could not book {num_tickets} ticket(s) for show {show_id}.")
            return False

    def view_show_list(self):
        print("Shows running in this hall:")
        for id, movie_name, time in self.show_list:
            print(f"Show ID: {id}, Movie: {movie_name}, Time: {time}")

    def view_available_seats(self, show_id):
        if show_id not in self.seats:
            print(f"Invalid show ID: {show_id}")
            return

        show_seats = self.seats[show_id]
        available_seats = []

        for row in range(self.rows):
            for col in range(self.cols):
                if show_seats[row][col] == 0:
                    available_seats.append((row + 1, col + 1))

        print(f"Available seats for show {show_id}:")
        for seat in available_seats:
            print(f"Seat: {seat[0]}, {seat[1]}")

def main():
    hall = Hall(5, 10, 1)
    

    cinema = Star_Cinema()
    cinema.entry_hall(hall)

    hall.entry_show(1, "Movie 1", "10:00 AM")

    while True:
        print("\nOptions:")
        print("1: View all shows today")
        print("2: Book available seats")
        print("3: Book ticket")
        print("4: Exit")

        option = input("Select an option: ")

        if option == "1":
            cinema.view_all_shows()
        elif option == "2":
            show_id = int(input("Enter the show ID: "))
            cinema.view_available_seats(show_id)
        elif option == "3":
            show_id = int(input("Enter the show ID: "))
            num_tickets = int(input("Enter the number of tickets to book: "))
            seat_list = []
            for _ in range(num_tickets):
                seat = tuple(map(int, input(f"Enter seat {len(seat_list) + 1} (e.g., '1,2'): ").split(',')))
                seat_list.append(seat)
            cinema.book_tickets(show_id, num_tickets, seat_list) 
        elif option == "4":
            print("Exited...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
