def book_seat(booked_seats, seat):
    if seat not in booked_seats:
        booked_seats.append(seat)

def cancel_seat(booked_seats, seat):
    if seat in booked_seats:
        booked_seats.remove(seat)

def available_seats(total, booked):
    return [seat for seat in range(1, total+1) if seat not in booked]

total_seats = int(input("Enter total seats: "))
booked_seats = list(map(int, input("Enter initially booked seats separated by space: ").split()))
book_seat(booked_seats, int(input("Enter seat to book: ")))
cancel_seat(booked_seats, int(input("Enter seat to cancel: ")))
print("Available seats:", available_seats(total_seats, booked_seats))
