class Star_Cinema:
    _hall_list = []

    def _entry_hall(self, hall):
        self._hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []
        super()._entry_hall(self)

    def entry_show(self, id, movie_name, time):
        seats = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        show = {"id": id, "movie_name": movie_name, "time": time, "seats": seats}
        self.__show_list.append(show)

    def book_seats(self):
        m_id = input("Enter Movie id: ")

        selected_show = None
        for show in self.__show_list:
            if show["id"] == m_id:
                selected_show = show
                break

        if selected_show is None:
            print(f"Movie ID {m_id} not available...")
            return

        seats = selected_show["seats"]
        if all(1 in row for row in seats):
            print(f"{m_id} is housefull...")
            return

        quantity = int(input("How many tickets do you want: "))
        booked = 0
        while booked < quantity:
            while True:
                row = int(input("Enter the row: "))
                col = int(input("Enter the column: "))

                if row >= self.__rows or col >= self.__cols:
                    print("Invalid Row or Column..")
                else:
                    break

            if seats[row][col] != 1:
                seats[row][col] = 1
                print(f"Row: {row}, Column: {col} Booked Successfully!!")
                booked += 1
            else:
                print(f"Row: {row}, Column: {col} already booked...")

    def view_show_list(self):
        for show in self.__show_list:
            print(f"ID: {show['id']}, Movie: {show['movie_name']}, Time: {show['time']}.")

    def view_available_seats(self):
        m_id = input("Enter Movie id to view seats: ")

        selected_show = None
        for show in self.__show_list:
            if show["id"] == m_id:
                selected_show = show
                break

        if selected_show is None:
            print(f"Movie ID {m_id} not available...")
            return

        seats = selected_show["seats"]
        for row in seats:
            print(row)


hall = Hall(5, 6, 2001)
hall.entry_show("101", "Jawan (2023)", "5:00PM, October 6, 2023")
hall.entry_show("102", "Salaar: Part 1 - Ceasefire (2023)", "8:00PM, October 6, 2024")
hall.entry_show("103","Mission: Impossible - Dead Reckoning Part One (2023)","7:00PM, October 7, 2024",)

while True:
    print("1. View All Shows ")
    print("2. View Available Seats")
    print("3. Book Ticket")
    print("4. Exit")
    check = int(input("Enter Option: "))

    if check == 1:
        hall.view_show_list()
        print("\n")
    elif check == 2:
        hall.view_available_seats()
        print("\n")
    elif check == 3:
        hall.book_seats()
        print("\n")
    elif check == 4:
        print("\n")
        break
    else:
        print("Press Right Key")
        print("\n")
