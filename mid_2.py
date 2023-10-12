class Star_Cinema:
    hall_list = []
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)

    
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

    def book_seats(self, show_id, seat_list):
        if show_id not in self.seats:
            print(f"Invalid show ID: {show_id}")
            return

        show_seats = self.seats[show_id]

        for row, col in seat_list:
            if 1 <= row <= self.rows and 1 <= col <= self.cols:
                if show_seats[row - 1][col - 1] == 0:
                    show_seats[row - 1][col - 1] = 1
                else:
                    print(f"Seat ({row}, {col}) is already booked for show {show_id}.")
            else:
                print(f"Invalid seat ({row}, {col}) for show {show_id}.")

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
    hall1 = Hall(5, 10, 1)
    hall2 = Hall(7, 12, 2)

    cinema = Star_Cinema()
    cinema.entry_hall(hall1)
    cinema.entry_hall(hall2)

    hall1.entry_show(1, "Movie 1", "10:00 AM")
    hall2.entry_show(2, "Movie 2", "2:00 PM")

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
            hall_no = int(input("Enter the hall number: "))
            show_id = int(input("Enter the show ID: "))
            cinema.view_available_seats(hall_no, show_id)
        elif option == "3":
            hall_no = int(input("Enter the hall number: "))
            show_id = int(input("Enter the show ID: "))
            seats_str = input("Enter the seats (e.g., '1,2 3,4'): ")
            seat_list = [tuple(map(int, seat.split(',')) for seat in seats_str.split())]
            cinema.book_tickets(hall_no, show_id, seat_list)
        elif option == "4":
            print("Exited...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
