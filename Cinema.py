class Star_Cinema:
    _hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls._hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._seats = {}
        self._show_list = []

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                self._seats[(i, j)] = 0 

        Star_Cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)

    def book_seats(self, show_id, seat_list):
        if show_id not in [show[0] for show in self._show_list]:
            print("Show not found.")
            return

        for seat in seat_list:
            if seat not in self._seats:
                print(f"Seat {seat} does not exist in this hall.")
            elif self._seats[seat] == 1:
                print(f"Seat {seat} is already booked.")
            else:
                self._seats[seat] = 1  
                print(f"Seat {seat} booked successfully.")

    def view_show_list(self):
        print("Show List:")
        for show in self._show_list:
            print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id not in [show[0] for show in self._show_list]:
            print("Show not found.")
            return

        print(f"Seat Matrix for Show ID {show_id} (0: Empty, 1: Booked):")
        for i in range(1, self._rows + 1):
            row_str = ""
            for j in range(1, self._cols + 1):
                row_str += str(self._seats[(i, j)]) + " "
            print(row_str)


hall1 = Hall(10, 10, 1)
hall1.entry_show("333", "Titanic", "24/9/23 10:00 AM")
hall1.entry_show("444","50 shades of phitron","24/9/23 02:00 PM")
hall1.entry_show("555","Lord of the Programming","24/9/23 06:00 PM")

while(True):
    print("---------------------------------\n")
    print("1. VIEW ALL SHOW TODAY\n")
    print("2. VIEW AVAILABLE SEATS\n")
    print("3. BOOK TICKET\n")
    print("4. EXIT\n")
    print("---------------------------------\n")

    option = int(input("\nEnter an option: "))
    if(option == 1):
        hall1.view_show_list()
    elif(option == 2):
        choice = input("\nFor which show? Type Show ID: ")
        hall1.view_available_seats(choice)
    elif(option == 3):
        chooseID = input("\nFor which show? Type Show ID: ")
        ticket = int(input("\nHow many tickets? Enter the number: "))
        seat_list_to_book = []
        for i in range(1,ticket+1):
            rowno = int(input("\nEnter the row no. for the seat no. : "))
            colno = int(input("\nEnter the column no. for the seat no. : "))
            seat_list_to_book.append((rowno,colno))
        hall1.book_seats(chooseID, seat_list_to_book)

    else:
        break    

    